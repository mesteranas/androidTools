import subprocess
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
import language
language.init_translation()
class uninstall(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("uninstall"))
        self.ba=qt.QComboBox()
        self.ba.setAccessibleName(_("select app"))
        self.com=qt.QPushButton(_("delete app"))
        self.com.setDefault(True)
        self.com.clicked.connect(self.com1)
        layout=qt.QVBoxLayout()
        layout.addWidget(self.ba)
        layout.addWidget(self.com)
        self.setLayout(layout)
        self.get()
    def get(self):
        result = subprocess.run('cd data/platform-tools && adb shell pm list packages', shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            package_names = result.stdout.strip().split('\n')
            package_names = [pkg.split(':')[-1] for pkg in package_names]
            self.ba.addItems(package_names)
    def com1(self):
        result = subprocess.run("cd data/platform-tools && adb uninstall " + self.ba.currentText(), shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            qt.QMessageBox.information(self,_("done"),_("Successfully uninstalled"))
        else:
            qt.QMessageBox.information(self,_("error"),_("Uninstallation failed"))