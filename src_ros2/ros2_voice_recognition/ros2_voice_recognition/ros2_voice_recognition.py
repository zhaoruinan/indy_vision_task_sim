
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

class Ui_examples_widget(object):
    def setupUi(self, examples_widget):
        examples_widget.setObjectName("examples_widget")
        examples_widget.resize(593, 137)
        self.label = QtWidgets.QLabel(examples_widget)
        self.label.setGeometry(QtCore.QRect(400, 20, 91, 25))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(examples_widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 91, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(examples_widget)
        self.comboBox.setGeometry(QtCore.QRect(480, 20, 111, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.progressBar = QtWidgets.QProgressBar(examples_widget)
        self.progressBar.setGeometry(QtCore.QRect(240, 20, 141, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(examples_widget)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 91, 25))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(examples_widget)
        self.textBrowser.setGeometry(QtCore.QRect(130, 50, 461, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(examples_widget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 91, 25))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(examples_widget)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 20, 71, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(examples_widget)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 51, 25))
        self.label_4.setObjectName("label_4")
        self.pushButton.pressed.connect(self.enable_voice)

        self.retranslateUi(examples_widget)
        QtCore.QMetaObject.connectSlotsByName(examples_widget)

    def retranslateUi(self, examples_widget):
        _translate = QtCore.QCoreApplication.translate
        examples_widget.setWindowTitle(_translate("examples_widget", "RQT Example"))
        self.label.setText(_translate("examples_widget", "Language:"))
        self.pushButton.setText(_translate("examples_widget", "Enable"))
        self.comboBox.setItemText(0, _translate("examples_widget", "English"))
        self.comboBox.setItemText(1, _translate("examples_widget", "Korean"))
        self.comboBox.setItemText(2, _translate("examples_widget", "Chinese"))
        self.label_2.setText(_translate("examples_widget", "wait for voice:"))
        self.label_3.setText(_translate("examples_widget", "vocie input:"))
        self.comboBox_2.setItemText(0, _translate("examples_widget", "Auto"))
        self.comboBox_2.setItemText(1, _translate("examples_widget", "Manual"))
        self.label_4.setText(_translate("examples_widget", "Mode:"))
    def enable_voice(self):
        print("enable voice input")
        language_set=self.comboBox.currentIndex()
        print(language_set)
        #t_voice = threading.Thread(target=voice_process,args=(language_set,))
        #t_voice.start()
        voice_process(language_set)
    def set_textBrowser(self,text):
        print("textBrowser output")
        self.textBrowser.setText(text)
def voice_process(language_set):
    import speech_recognition as sr
    #import pyttsx3
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("now start voice")
        audio = r.listen(source)
    if language_set == 1:
        result = r.recognize_google(audio, language='ko-KR')
    elif language_set ==2:
        result = r.recognize_google(audio, language='zh')
    else :
        result = r.recognize_google(audio)
    if result!= None:
        print(result)
    else:
        result="no voice, please speak loundly"
    ui.set_textBrowser(result)


def main():
    print('Hi from ros2_voice_recognition.')
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_examples_widget()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
