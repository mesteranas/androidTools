import sys
from custome_errors import *
sys.excepthook = my_excepthook
import subprocess
import gui
import guiTools
from webbrowser import open as openLink
import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        layout=qt.QVBoxLayout()
        self.select=qt.QComboBox()
        self.select.setAccessibleName(_("select service"))
        self.select.addItems([_("install"),_("uninstall"),_("more tools")])
        layout.addWidget(self.select)
        self.com=qt.QPushButton(_("next"))
        self.com.setDefault(True)
        self.com.clicked.connect(self.oncom)
        layout.addWidget(self.com)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:openLink("https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:openLink("https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:openLink("https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def oncom(self):
        result = subprocess.run("cd data/platform-tools && adb devices", shell=True, capture_output=True, text=True)
        if result.stdout=="""List of devices attached
\n""":
            qt.QMessageBox.information(self,_("error"),_("no android device found"))
        else:
            if self.select.currentIndex()==0:
                gui.install(self).exec()
            elif self.select.currentIndex()==1:
                gui.uninstall(self).exec()
            elif self.select.currentIndex()==2:
                gui.moreTools(self).exec()
App=qt.QApplication([])
w=main()
w.show()
App.exec()