# We require a canvas class
import platform
import pandas as pd
# Use NSURL as a workaround to pyside/Qt4 behaviour for dragging and dropping on OSx
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic.properties import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

op_sys = platform.system()
if op_sys == 'Darwin':
    from Foundation import NSURL


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=120):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        fig.tight_layout()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_csv_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_csv_file.setObjectName("actionOpen_csv_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_csv_file)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.filename = ''
        self.canv = MatplotlibCanvas(self)
        self.df = []

        self.toolbar = Navi(self.canv, self.centralwidget)
        self.horizontalLayout.addWidget(self.toolbar)

        self.themes = ['bmh', 'classic', 'dark_background', 'fast',
                       'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright',
                       'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
                       'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
                       'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
                       'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn',
                       'Solarize_Light2', 'tableau-colorblind10']

        self.comboBox.addItems(self.themes)

        self.pushButton.clicked.connect(self.getFile)
        self.comboBox.currentIndexChanged['QString'].connect(self.Update)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionOpen_csv_file.triggered.connect(self.getFile)

    def Update(self, value):
        print("Value from Combo Box:", value)
        plt.clf()
        plt.style.use(value)
        try:
            self.horizontalLayout.removeWidget(self.toolbar)
            self.verticalLayout.removeWidget(self.canv)

            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None
            self.verticalLayout.removeItem(self.spacerItem1)
        except Exception as e:
            print(e)
            pass
        self.canv = MatplotlibCanvas(self)
        self.toolbar = Navi(self.canv, self.centralwidget)

        self.horizontalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canv)

        self.canv.axes.cla()
        ax = self.canv.axes
        self.df.plot(ax=self.canv.axes)
        legend = ax.legend()
        legend.set_draggable(True)

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title(self.Title)

        self.canv.draw()

    def getFile(self):
        """ This function will get the address of the csv file location
            also calls a readData function
        """
        self.filename = QFileDialog.getOpenFileName(filter="csv (*.csv)")[0]
        print("File :", self.filename)
        self.readData()

    def readData(self):
        """ This function will read the data using pandas and call the update
            function to plot
        """
        import os
        base_name = os.path.basename(self.filename)
        self.Title = os.path.splitext(base_name)[0]
        print('FILE', self.Title)
        self.df = pd.read_csv(self.filename, encoding='utf-8').fillna(0)
        self.Update(self.themes[0])  # lets 0th theme be the default : bmh

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Theme"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_csv_file.setText(_translate("MainWindow", "Open csv file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())