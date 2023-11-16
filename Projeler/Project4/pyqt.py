import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal, pyqtSlot

from main import Ui_MainWindow  # UI dosyasından oluşturulan Python kodunu içe aktarın

class MyWindow(QMainWindow):
    my_signal = pyqtSignal(int) # pyqtSignal ile bir sinyal tanımlıyoruz
 
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Tasarladığınız arayüz sınıfını oluşturun
        self.ui.setupUi(self)       # Arayüzü pencereye bağlayın

        self.ui.horizontalSlider.valueChanged[int].connect(self.mySlot2) # slider'ın değeri değiştiğinde tetiklenecek fonksiyonu bağlıyoruz
        #SİGNAL İÇİNDE SİGNAL
        self.ui.horizontalSlider.valueChanged[int].connect(self.my_signal[int]) # slider'ın değeri değiştiğinde tetiklenecek fonksiyonu bağlıyoruz  
        self.my_signal[int].connect(self.mySlot3) # tanımladığımız sinyali tetiklendiğinde tetiklenecek fonksiyonu bağlıyoruz

        #emit ile sinyal tetikleme
        self.ui.horizontalSlider.valueChanged[int].connect(self.kaydirici_slot) # slider'ın değeri değiştiğinde tetiklenecek fonksiyonu bağlıyoruz

    
    #DESİGNER TANIMLI SIGNAL
    def mySlot(self,index): # tanımladığımız slot fonksiyonu ve signal designerden verildi
        self.ui.label.setText(f"değer: {index}") # label'ın textini değiştiriyoruz 
        #return 0
    #KOD İLE TANIMLI SIGNAL
    def mySlot2(self,index): # tanımladığımız slot fonksiyonu ve signal kod ile verildi
        self.ui.label.setText(f"değer: {index}")

    #SİGNAL İÇİNDE SİGNAL Kod ile tanımlı    
    def mySlot3(self,index):
        self.ui.label.setText(f"değer: {index}")
        #print(index)
    #emit ile sinyal tetikleme
    def kaydirici_slot(self,index):
        self.my_signal[int].emit(index) # tanımladığımız sinyali tetikliyoruz
        #signal iptal etme disconnect
        self.ui.horizontalSlider.valueChanged[int].disconnect(self.mySlotİptal) # slider'ın değeri değiştiğinde tetiklenecek fonksiyonu bağlıyoruz


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = MyWindow()
    pencere.setWindowTitle("PyQt6 ile Arayüz Oluşturma")
    pencere.show()
    sys.exit(uygulama.exec())
