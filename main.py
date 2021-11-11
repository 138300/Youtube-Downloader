from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from youtube import Ui_MainWindow
from pytube import *
from winreg import *


class YouTubeWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.you = Ui_MainWindow()
        self.you.setupUi(self)  

        # control buttons connection
        self.you.stackedWidget.setCurrentWidget(self.you.welcome_page)
        self.you.btn_c.clicked.connect(lambda : self.you.stackedWidget.setCurrentWidget(self.you.download_page))
        self.you.btn_e.clicked.connect(self.finished_page)
        self.you.btn_dg.clicked.connect(self.download_again)
        self.you.btn_f.clicked.connect(self.choose_folder)
        self.you.btn_d.clicked.connect(self.download)
        
        # get Download directory path
        with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
            downloads_path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
            self.you.path_input.setText(downloads_path)

    def choose_folder(self):
        self.dir_path=QFileDialog.getExistingDirectory(self,"Choose Directory")
        self.you.path_input.setText(self.dir_path)

    def download(self):
        save_path = self.you.path_input.text()
        link = self.you.link_input.text()
        try:            
            youtube = YouTube(link)
            video = youtube.streams.get_highest_resolution()
            video.download(save_path)
            
            self.setStyleSheet(("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #025955, stop:1 #29BB89);"))
            self.you.title_2.setText("Download Completed")
        except:
            QMessageBox.warning(self,'Error','Something went wrong!')

    def download_again(self):
        self.you.link_input.setText('')
        self.setStyleSheet(("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #93291E, stop:1 #ED213A);"))
        self.you.title_2.setText("Enter path and Link to download video")
        self.you.stackedWidget.setCurrentWidget(self.you.download_page)

    def finished_page(self):
        self.you.stackedWidget.setCurrentWidget(self.you.finished_page)
        self.you.finished_page.setStyleSheet(("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #93291E, stop:1 #ED213A);"))
        self.you.centralwidget.setStyleSheet(("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #93291E, stop:1 #ED213A);"))

if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    window = YouTubeWindow()
    window.show()
    sys.exit(app.exec_())

