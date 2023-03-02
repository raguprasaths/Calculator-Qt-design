from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup
import sys
# To load the UI file
Ui_MainWindow, QtBaseClass = uic.loadUiType("calculator.ui")
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Button_Group = QButtonGroup()
        self.Button_Group.addButton(self.ui.Button_0)
        self.Button_Group.addButton(self.ui.Button_1)
        self.Button_Group.addButton(self.ui.Button_2)
        self.Button_Group.addButton(self.ui.Button_3)
        self.Button_Group.addButton(self.ui.Button_4)
        self.Button_Group.addButton(self.ui.Button_5)
        self.Button_Group.addButton(self.ui.Button_6)
        self.Button_Group.addButton(self.ui.Button_7)
        self.Button_Group.addButton(self.ui.Button_8)
        self.Button_Group.addButton(self.ui.Button_9)
        self.Button_Group.addButton(self.ui.Button_add)
        self.Button_Group.addButton(self.ui.Button_subtract)
        self.Button_Group.addButton(self.ui.Button_multiply)
        self.Button_Group.addButton(self.ui.Button_divide)
        self.Button_Group.buttonClicked.connect(
                          self.Button_clicked)
        self.ui.Button_equals.clicked.connect(
                          self.calculate_output)
        self.ui.Button_clear.clicked.connect(self.clear_output)
        self.INPUT = ""
    def Button_clicked(self, btn):
        val = btn.text()
        if val.lower() == 'x':
            val = '*'
        self.INPUT = self.INPUT + val
        self.display_on_screen(self.INPUT)
    def display_on_screen(self, val_to_display):
        self.ui.output.setText(str(val_to_display))
    def calculate_output(self):
        try:
            result = str(eval(self.INPUT))
        except:
            result = "Error"
        self.display_on_screen(result)
        self.INPUT = ""
    def clear_output(self):
        self.INPUT = ""
        self.ui.output.setText("")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
