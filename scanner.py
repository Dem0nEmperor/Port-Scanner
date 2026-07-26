from concurrent.futures import ThreadPoolExecutor, as_completed
from PySide6.QtWidgets import QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
import socket
import time
import struct
import random

class IPScan:
    def __init__(self, host, portRange1, portRange2):
        self.host = host
        self.portRange1 = portRange1
        self.portRange2 = portRange2
        self.progress = self.portRange1
        self.executor = ThreadPoolExecutor(max_workers=800)
        self.threads = []
        self.stopped = False

    SERVICE_BANNERS = [
        (b"SSH-", "SSH"),
        (b"FTP", "FTP"),
        (b"SMTP", "SMTP"),
        (b"POP3", "POP3"),
        (b"IMAP", "IMAP"),
        (b"HTTP/", "HTTP"),
        (b"HTTP", "HTTP"),
        (b"Redis", "REDIS"),
        (b"MySQL", "MySQL"),
        (b"PostgreSQL", "PostgreSQL"),
        (b"RTSP", "RTSP"),
        (b"Telnet", "Telnet"),
        (b"LDAP", "LDAP"),
        (b"RFB", "VNC"),
        (b"AMQP", "AMQP"),
        (b"SMB", "SMB"),
    ]

    def active_check(self, sock: socket.socket):
        try:
            data = sock.recv(512)

            for id, name in self.SERVICE_BANNERS:
                if id in data:
                    return name

        except socket.timeout:
            return "None"

    def dns_check(self, sock: socket.socket):
        tid = random.randint(0, 65535)

        query = struct.pack(">H", tid)
        query += b"\x01\x00"
        query += b"\x00\x01"
        query += b"\x00\x00\x00\x00\x00\x00"

        for part in "example.com".split("."):
            query += bytes([len(part)]) + part.encode()

        query += b"\x00"
        query += b"\x00\x01"
        query += b"\x00\x01"

        packet = struct.pack(">H", len(query)) + query

        try:
            sock.sendall(packet)

            length = struct.unpack(">H", sock.recv(2))[0]
            response = sock.recv(length)

            if response[:2] == struct.pack(">H", tid):
                return True
        except socket.timeout:
            pass

        return False

    def port_check(self, port):
        if self.stopped:
            return
        try:
            with socket.create_connection((self.host, port), timeout=0.5) as sock:

                active_result = self.active_check(sock)
                if active_result != "None":
                    return [port, active_result]

                try:
                    sock.sendall(b"\r\n\r\n")
                    sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")

                    response = sock.recv(512)

                    if response.startswith(b"HTTP"):
                        return [port, "HTTP"]

                    return [port, "Unknown"]

                except socket.timeout:
                    pass
        except Exception as e:
            return
        with socket.create_connection((self.host, port), timeout=0.5) as sock:
            if self.dns_check(sock):
                return [port, "DNS"]
            else:
                return [port, "Unknown"]

    def start_scan(self):
        for i in range(self.portRange1, self.portRange2 + 1):
            thr = self.executor.submit(self.port_check, i)
            self.threads.append(thr)

    def stop(self):
        self.stopped = True

    def completed(self, model, ports):
        lastIndex = 0
        for g in as_completed(self.threads):
            result = g.result()

            if self.stopped:
                self.progress = 1
                self.executor.shutdown(wait=False, cancel_futures=True)
                return

            if result:
                time.sleep(0.2)
                model.setItem(lastIndex, 0, QStandardItem(str(result[0])))
                model.setItem(lastIndex, 1, QStandardItem(result[1]))
                model.setItem(lastIndex, 2, QStandardItem("Yes"))

                ports.append([str(result[0]), result[1], "Opened"])
                lastIndex += 1

            self.progress += 1