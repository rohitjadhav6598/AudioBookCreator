import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import pyttsx3
from PyQt5 import QtCore, QtGui, QtWidgets


class Audio():
    def __init__(self):
        self.engine = pyttsx3.init() # object creation
        self.voices = self.engine.getProperty('voices')       #getting details of current voice


    def adjust(self,r,v,g):
        self.engine.setProperty('rate', r)     # setting up new voice rate
        self.engine.setProperty('volume',0.01*v)    # setting up volume level  between 0 and 1
        try:
            self.engine.setProperty('voice', self.voices[g].id)   #changing index, changes voices. 1 for female
        except IndexError:
            return "voice not available"
        return 0

    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()

    def save(self,text,fpath):
        self.engine.save_to_file(text, fpath )
        self.engine.runAndWait()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.vol = QtWidgets.QLabel(self.centralwidget)
        self.vol.setObjectName("vol")
        self.verticalLayout.addWidget(self.vol)
        self.VolumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.VolumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.volume = 1
        self.VolumeSlider.valueChanged.connect(self.changevolume)


        self.verticalLayout.addWidget(self.VolumeSlider)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonF = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonF.setChecked(True)
        self.radioButtonF.setObjectName("radioButtonF")
        self.verticalLayout_2.addWidget(self.radioButtonF)
        self.radioButtonM = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonM.setObjectName("radioButtonM")
        self.verticalLayout_2.addWidget(self.radioButtonM)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.SpeedSlider = QtWidgets.QSlider(self.centralwidget)
        self.SpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SpeedSlider.setObjectName("SpeedSlider")
        self.horizontalLayout_2.addWidget(self.SpeedSlider)
        self.speed = QtWidgets.QLabel(self.centralwidget)
        self.speed.setObjectName("speed")
        self.sp = 1
        self.SpeedSlider.valueChanged.connect(self.changespeed) 


        self.horizontalLayout_2.addWidget(self.speed)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setObjectName("Button")
        self.horizontalLayout_3.addWidget(self.Button)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.A = Audio()
        #self.f = App()

        self.voice = 0

        self.radioButtonM.toggled.connect(self.mselected)
        self.radioButtonF.toggled.connect(self.fselected) 

        self.actionOpen.triggered.connect(self.fileopen)
        self.actionSave.triggered.connect(self.filesave)
        
        self.Button.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio Book Creator"))
        self.vol.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Volume"))
        self.radioButtonF.setText(_translate("MainWindow", "Female"))
        self.radioButtonM.setText(_translate("MainWindow", "Male"))
        self.label_3.setText(_translate("MainWindow", "Speed"))
        self.speed.setText(_translate("MainWindow", "0"))
        self.Button.setText(_translate("MainWindow", "Speak"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open text file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save as mp3"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def fileopen(self):
        path, _ = QFileDialog.getOpenFileName(MainWindow, "Open file", "", 
                            "Text documents (*.txt);All files (*.*)") 
        if path:
            try: 
                with open(path, 'rU') as f:
                    text = f.read() 
            except Exception as e: 
                self.dialog_critical(str(e)) 
            else: 
                self.path = path 
                self.textEdit.setPlainText(text) 

    def filesave(self):
        filename, _ = QFileDialog.getSaveFileName(MainWindow, "Save file", "", 
                            "Audio file (*.mp3);;All files (*.*)")
        if filename:
            text = self.textEdit.toPlainText()
            msg = self.A.adjust(self.sp,self.volume,self.voice)
            if(msg):
                dlg = QtWidgets.QMessageBox() 
                dlg.setText(msg)
                dlg.setIcon(QtWidgets.QMessageBox.Critical)
                dlg.exec_() 
            else:
                self.A.save(text,filename)

    def pressed(self):
        text = self.textEdit.toPlainText()
        msg = self.A.adjust(self.sp,self.volume,self.voice)
        if(msg):
            dlg = QtWidgets.QMessageBox() 
            dlg.setText(msg)
            dlg.setIcon(QtWidgets.QMessageBox.Critical)
            dlg.exec_() 
        else:
            self.A.speak(text)

    def changespeed(self, sp): 
        self.speed.setText(str(sp))
        self.sp = sp*3
        
    def changevolume(self, volume): 
        self.vol.setText(str(volume))
        self.volume = volume
        
    def mselected(self, selected): 
        if selected: 
            self.voice = 1
            
    def fselected(self, selected): 
        if selected: 
            self.voice = 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
