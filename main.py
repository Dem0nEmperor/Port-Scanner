import csv
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6 import QtGui
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import *
from tkinter import Tk, filedialog, messagebox
import threading
import time

from scanner import IPScan

from ui import Ui_Form

scan = None
running = False

ports = []

class TimerWorker(QThread):
    sig = Signal(str)

    def run(self):
        timer = 0.0
        while running:
            self.sig.emit(f"Sec: {timer:.1f}")
            timer += 0.1
            time.sleep(0.1)

class ProgressBarWorker(QThread):
    progress_changed = Signal(int)

    def run(self):
        while True:
            if scan != None:
                self.progress_changed.emit(scan.progress)

def save():
    root = Tk()
    root.withdraw()

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("csv", "*.csv")])

    if file_path:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(ports)
            messagebox.showinfo("", "Export complete!")
    

def scan_handler():
    global scan
    global running
    global ports

    ports = []

    minPort = int(ui.lineEdit_2.text())
    maxPort = int(ui.lineEdit_3.text())

    ui.progressBar.setMaximum(maxPort)
    ui.progressBar.setMinimum(minPort)

    scan = IPScan(ui.lineEdit.text(), minPort, maxPort)
    scan.start_scan()
    scan.completed(model, ports)
    
    print(ports)
    ui.pushButton_3.setEnabled(True)

    ui.pushButton.setText("Start")
    ui.setgreen()

    running = False

    time.sleep(1)

    scan.progress = minPort
    time.sleep(0.1)

    scan = None

def stop_button():
    global scan
    scan.stop()

def start_button():
    global model
    global running

    if ui.lineEdit.text() != "" and ui.lineEdit_2.text() != "" and ui.lineEdit_3.text() != "":

        for s in ui.lineEdit_2.text():
            if s not in "0123456789":
                messagebox.showerror("", "Error")
                return

        for s in ui.lineEdit_3.text():
            if s not in "0123456789":
                messagebox.showerror("", "Error")
                return

        if int(ui.lineEdit_2.text()) >= int(ui.lineEdit_3.text()):
            messagebox.showerror("", "Error")
            return

        running = True

        ui.pushButton.setText("Stop")
        ui.setred()

        ui.pushButton_3.setEnabled(False)

        model.clear()

        model = QStandardItemModel()
        model.setColumnCount(3)
        model.setHorizontalHeaderLabels(["Port", "Service", "Opened"])

        ui.tableView.setModel(model)
        ui.tableView.setColumnWidth(0, 115)
        ui.tableView.setColumnWidth(1, 115)
        ui.tableView.setColumnWidth(2, 115)

        timer.start()

        tz = threading.Thread(target=scan_handler)
        tz.start()
    else:
        messagebox.showerror("", "Error")

def main_button():
    if running:
        stop_button()
    else:
        start_button()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(window)

    window.setFixedSize(405, 455)
    window.setWindowTitle("Port Scanner by Dem0nEmperor")
    window.show()

    ui.pushButton_2.setVisible(False)
    ui.pushButton_3.clicked.connect(save)

    ui.pushButton.clicked.connect(main_button)

    model = QStandardItemModel()
    model.setColumnCount(3)
    model.setHorizontalHeaderLabels(["Port", "Service", "Opened"])

    ui.tableView.setModel(model)
    ui.tableView.setColumnWidth(0, 115)
    ui.tableView.setColumnWidth(1, 115)
    ui.tableView.setColumnWidth(2, 115)
    ui.tableView.verticalHeader().setVisible(False)
    ui.tableView.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)

    worker = ProgressBarWorker()
    worker.progress_changed.connect(ui.progressBar.setValue)
    worker.start()

    timer = TimerWorker()
    timer.sig.connect(ui.label_5.setText)

    sys.exit(app.exec())