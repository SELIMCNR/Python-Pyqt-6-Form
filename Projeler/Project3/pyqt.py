import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from main import Ui_MainWindow  # UI dosyasından oluşturulan Python kodunu içe aktarın
from PyQt6 import QtGui
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()  # Tasarladığınız arayüz sınıfını oluşturun
        self.ui.setupUi(self)       # Arayüzü pencereye bağlayın
        self.ui.pushButton.clicked.connect(self.renkDegistir)
        self.ui.centralwidget.setStyleSheet("background-color: blue;font: bold 25px; color:white;")
        self.ui.formFrame.setStyleSheet("background-color: green;font: bold 25px; color:white;")
    def renkDegistir(self):
        self.ui.pushButton.setStyleSheet("background-color: yellow;font: bold 25px; color:white;")    
       

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = MyWindow()
    pencere.setWindowTitle("PyQt6 ile Arayüz Oluşturma")
    pencere.show()
    sys.exit(uygulama.exec())
