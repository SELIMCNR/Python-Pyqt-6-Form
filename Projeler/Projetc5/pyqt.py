import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from main import Ui_MainWindow  # UI dosyasından oluşturulan Python kodunu içe aktarın

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()  # Tasarladığınız arayüz sınıfını oluşturun
        self.ui.setupUi(self)       # Arayüzü pencereye bağlayın
        #menü bağlantıları
        self.ui.actionKategori11.triggered.connect(self.kategori11)
        self.ui.actionKategori12.triggered.connect(self.kategori12)
        self.ui.actionKategori13.triggered.connect(self.kategori13)
        self.ui.actionKategori21.triggered.connect(self.kategori21)
        self.ui.actionKategori22.triggered.connect(self.kategori22)
        self.ui.actionKategori23.triggered.connect(self.kategori23)
        self.ui.actionKategori31.triggered.connect(self.kategori31)
        self.ui.actionKategori32.triggered.connect(self.kategori32)
        self.ui.actionKategori33.triggered.connect(self.kategori33)

    #menü bağlantı fonksiyonları
    def kategori11(self):
        print("Kategori 1. seçildi")  
        self.ui.label.setText("Kategori 1.1 seçildi")
        self.ui.menuKategori1.setStyleSheet("background-color:blue;")
    def kategori12(self):
        print("Kategori 1.2 seçildi") 
        self.ui.label_2.setText("Kategori 1.2 seçildi")
    def kategori13(self):
        print("Kategori 1.3 seçildi")
        self.ui.label_3.setText("Kategori 1.3 seçildi")   
    def kategori21(self):
        print("Kategori 2.1 seçildi")  
        self.ui.label.setText("Kategori 2.1 seçildi")
        self.ui.menuKategori2.setStyleSheet("background-color:yellow;")
    def kategori22(self):
        print("Kategori 2.2 seçildi") 
        self.ui.label_2.setText("Kategori 2.2 seçildi")
    def kategori23(self):
        print("Kategori 2.3 seçildi")
        self.ui.label_3.setText("Kategori 2.3 seçildi")
    def kategori31(self):
        print("Kategori 3.1 seçildi")  
        self.ui.label.setText("Kategori 3.1 seçildi")
        self.ui.menuKategori3.setStyleSheet("background-color:green;")
    def kategori32(self):
        print("Kategori 3.2 seçildi") 
        self.ui.label_2.setText("Kategori 3.2 seçildi")
    def kategori33(self):
        print("Kategori 3.3 seçildi")
        self.ui.label_3.setText("Kategori 3.3 seçildi")



              
if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = MyWindow()
    pencere.setWindowTitle("PyQt6 ile Arayüz Oluşturma")
    pencere.show()
    sys.exit(uygulama.exec())
