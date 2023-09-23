import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QFormLayout

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import numpy as np


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('My small app in Qt')

        # create a layout
        layout = QFormLayout()
        self.setLayout(layout)


        label = QLabel('Click the button to change me')
        label.setStyleSheet("background-color : white; color : darkblue")
        # Přidáním do layoutu se nápis automaticky stane potomkem hlavního okna
        layout.addWidget(label)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # self.plot_sin(sc)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        layout.addWidget(sc)

        # create buttons and add them to the layout
        titles = ['Change', 'Plot', 'Exit']
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        buttons[0].setToolTip("Press button change text!!!")
        buttons[0].clicked.connect(lambda: self.change_text(label))
        buttons[0].setStyleSheet("background-color : darkblue; color : white")

        buttons[1].setStyleSheet("background-color : darkblue; color : white")
        buttons[1].clicked.connect(lambda: self.plot_sin(sc))

        buttons[2].setToolTip("Press button for closing app!!!")
        buttons[2].setStyleSheet("background-color : darkblue; color : white")
        buttons[2].clicked.connect(app.exit)

        
        self.setStyleSheet('''QToolTip { 
                           background-color: darkblue; 
                           color: white; 
                           border: white solid 1px
                           }''')
        
        # show the window
        self.show()

    def change_text(self, label):
        label.setText('Hi, nice to meet you!!!')
        label.setStyleSheet("background-color : white; color : red")

    def plot_sin(self, sin_plot):
        sin_plot.axes.plot([0,1,2,3,4], [5,0,5,0,5])
        sin_plot.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())