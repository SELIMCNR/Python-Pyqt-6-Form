from PyQt6.QtWidgets import *


class first_GUI(QWidget):
    def __init__(self):
        super().__init__()
   
        etiket = QLabel("Merhaba PyQt6")
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(etiket)
        self.setLayout(vertical_layout)
        etiket.show()

uygulama = QApplication([])
pencere=first_GUI()
pencere.resize(400,400)
pencere.setWindowTitle("PyQt6 Ders 1")
pencere.show()
uygulama.exec()

