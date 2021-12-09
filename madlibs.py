import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

aux = 0

def delete_form(form):
   for i in reversed(range(form.rowCount())):
      form.removeRow(i)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("madlibs")
        self.resize(400,200)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # create the layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # create the tab widget
        tabs = QTabWidget()
        tabs.addTab(self.titanic_UI(), "titanic")
        tabs.addTab(self.spiderman_UI(), "spiderman")
        tabs.addTab(self.meangirls_UI(), "mean girls")
        layout.addWidget(tabs)

    def clear_form(self, layout):
        for i in range(layout.rowCount() * 2):
            if("QLineEdit" in str(layout.itemAt(i).widget())):
                layout.itemAt(i).widget().clear()

# set up the titanic tab
    def titanic_UI(self):
        titanic_tab = QWidget()
        layout = QFormLayout()

        layout.name_line = QLineEdit(self)
        layout.verb_line = QLineEdit(self)
        layout.adj_line = QLineEdit(self)
        layout.noun_line = QLineEdit(self)

        layout.addRow("name", layout.name_line)
        layout.addRow("verb", layout.verb_line)
        layout.addRow("adjective", layout.adj_line)
        layout.addRow("noun (plural)", layout.noun_line)

        layout.addRow(QPushButton('clear', clicked = lambda: self.clear_form(layout)), QPushButton('generate', clicked = lambda: self.titanic_btn(layout)))

        titanic_tab.setLayout(layout)
        return titanic_tab
    
# set up the titanic button
    def titanic_btn(self, layout):
        if(self.checkIfEmpty(layout) != -1):
            dialog = QDialog()
            dialog.resize(300,150)
            dialog.setWindowTitle("titanic madlib")
            dialog.setWindowIcon(QtGui.QIcon('logo.png'))
            dialog.setWindowModality(Qt.ApplicationModal)

            lbl = QLabel(dialog)
            name = layout.name_line.text()
            verb = layout.verb_line.text()
            adj = layout.adj_line.text()
            noun = layout.noun_line.text()

            lbl.setText(f"{name} i want you to {verb} me like one of your {adj} {noun}.")
            lbl.setWordWrap(True)
            lbl.resize(265,100)
            lbl.move(20,0)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
            close = QPushButton("Close", dialog, clicked = lambda: dialog.close())
            close.move(105,100)

            dialog.exec_()

# set up the spiderman tab
    def spiderman_UI(self):
        spiderman_tab = QWidget()
        layout = QFormLayout()

        layout.adj1_line = QLineEdit(self)
        layout.noun1_line = QLineEdit(self)
        layout.adj2_line = QLineEdit(self)
        layout.noun2_line = QLineEdit(self)

        layout.addRow("adjective", layout.adj1_line)
        layout.addRow("noun", layout.noun1_line)
        layout.addRow("adjective", layout.adj2_line)
        layout.addRow("noun", layout.noun2_line)

        layout.addRow(QPushButton('clear', clicked = lambda: self.clear_form(layout)), QPushButton('generate', clicked = lambda: self.spiderman_btn(layout)))

        spiderman_tab.setLayout(layout)
        return spiderman_tab

# set up the spiderman button
    def spiderman_btn(self, layout):
        if(self.checkIfEmpty(layout) != -1):
            dialog = QDialog()
            dialog.resize(300,150)
            dialog.setWindowTitle("spiderman madlib")
            dialog.setWindowIcon(QtGui.QIcon('logo.png'))
            dialog.setWindowModality(Qt.ApplicationModal)

            lbl = QLabel(dialog)
            adj1 = layout.adj1_line.text()
            noun1 = layout.noun1_line.text()
            adj2 = layout.adj2_line.text()
            noun2 = layout.noun2_line.text()

            lbl.setText(f"remember, with {adj1} {noun1}, comes {adj2} {noun2}.")
            lbl.setWordWrap(True)
            lbl.resize(265,100)
            lbl.move(20,0)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
            close = QPushButton("Close", dialog, clicked = lambda: dialog.close())
            close.move(105,100)

            dialog.exec_()

# set up the mean girls tab
    def meangirls_UI(self):
        meangirls_tab = QWidget()
        layout = QFormLayout()

        layout.number_line = QLineEdit(self)
        layout.noun1_line = QLineEdit(self)
        layout.noun2_line = QLineEdit(self)
        layout.verb_line = QLineEdit(self)

        layout.addRow("number (ordinal)", layout.number_line)
        layout.addRow("noun", layout.noun1_line)
        layout.addRow("noun", layout.noun2_line)
        layout.addRow("verb", layout.verb_line)

        layout.addRow(QPushButton('clear', clicked = lambda: self.clear_form(layout)), QPushButton('generate', clicked = lambda: self.meangirls_btn(layout)))
        
        meangirls_tab.setLayout(layout)
        return meangirls_tab

# set up the mean girls button
    def meangirls_btn(self, layout):
        if(self.checkIfEmpty(layout) != -1):
            dialog = QDialog()
            dialog.resize(300,150)
            dialog.setWindowTitle("mean girls madlib")
            dialog.setWindowIcon(QtGui.QIcon('logo.png'))
            dialog.setWindowModality(Qt.ApplicationModal)

            lbl = QLabel(dialog)
            number = layout.number_line.text()
            noun1 = layout.noun1_line.text()
            noun2 = layout.noun2_line.text()
            verb = layout.verb_line.text()

            lbl.setText(f"i have a {number} sense. it's like i have {noun1} or something. my {noun2} can always tell when it's going to {verb}.")
            lbl.setWordWrap(True)
            lbl.resize(265,100)
            lbl.move(20,0)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
            close = QPushButton("Close", dialog, clicked = lambda: dialog.close())
            close.move(105,100)

            dialog.exec_()     

# checks if any of the arguments are missing
    def checkIfEmpty(self, layout):
        missing_args = 0
        for i in range(layout.rowCount() * 2):
            if("QLineEdit" in str(layout.itemAt(i).widget())):
                if not layout.itemAt(i).widget().text():
                    missing_args = 1

        if(missing_args == 1):
            errordialog = QDialog()
            errordialog.resize(150,100)
            errordialog.setWindowTitle("error")
            errordialog.setWindowIcon(QtGui.QIcon('logo.png'))
            errordialog.setWindowModality(Qt.ApplicationModal)
                        
            lbl = QLabel(errordialog)
            lbl.setText("missing arguments!")
            lbl.move(20,20)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
            close = QPushButton("Close", errordialog, clicked = lambda: errordialog.close())
            close.move(30,50)

            errordialog.exec_()

            return -1;   

                          
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
