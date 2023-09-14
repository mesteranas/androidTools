import subprocess
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
import language
language.init_translation()
class moreTools(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("More tools"))
        self.call=qt.QPushButton(_("call"))
        self.call.setDefault(True)
        self.call.clicked.connect(self.fcall)
        layout=qt.QVBoxLayout()
        layout.addWidget(self.call)
        a={
            "take a screenshot":"120",
            "go back":"4",
            "home screen":"3",
            "over view":"187"}
        for key,value in a.items():
            b=qt.QPushButton(key)
            b.setDefault(True)
            b.clicked.connect(lambda _, val=value:subprocess.run("cd data/platform-tools && adb shell input keyevent " + val, shell=True))
            layout.addWidget(b)
        self.setLayout(layout)
    def fcall(self):
        text,ok=qt.QInputDialog.getText(self,_("phone number"),_("type the phone number"))
        if ok:
            result = subprocess.run("cd data/platform-tools && adb shell am start -a android.intent.action.CALL -d tel:" + text, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                qt.QMessageBox.information(self,_("done"),_("call started"))
            else:
                qt.QMessageBox.information(self,_("error"),_("call not started"))