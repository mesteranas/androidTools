import subprocess
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
import language
language.init_translation()
class install(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("install"))
        self.path=qt.QLineEdit()
        self.path.setAccessibleName(_("app path"))
        self.path.setReadOnly(True)
        self.brows=qt.QPushButton(_("brows"))
        self.brows.setDefault(True)
        self.brows.clicked.connect(self.fbrows)
        self.com=qt.QPushButton(_("install"))
        self.com.setDefault(True)
        self.com.clicked.connect(self.oncom)
        layout=qt.QVBoxLayout()
        layout.addWidget(self.path)
        layout.addWidget(self.brows)
        layout.addWidget(self.com)
        self.setLayout(layout)
    def fbrows(self):
        file=qt.QFileDialog(self)
        file.setDefaultSuffix("apk")
        file.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptOpen)
        file.setNameFilters(["apk files(*.apk)"])
        if file.exec() == qt.QFileDialog.DialogCode.Accepted:
            self.path.setText(file.selectedFiles()[0])
    def oncom(self):
        result = subprocess.run("cd data/platform-tools && adb install " + self.path.text(), shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            qt.QMessageBox.information(self,_("done"),_("Successfully installed"))
        else:
            qt.QMessageBox.information(self,_("error"),_("installation failed"))