import sys
import platform
from PySide import QtCore, QtGui

import Animacion.Maya_animation_rigsExplorer.UI.Win_Explorer
reload(Animacion.Maya_animation_rigsExplorer.UI.Win_Explorer)
from Animacion.Maya_animation_rigsExplorer.UI.Win_Explorer import *

# TODO ***************************
import Lighting.ReconnectShaders.Core.Bridge_reconnectShaders
reload(Lighting.ReconnectShaders.Core.Bridge_reconnectShaders)
from Lighting.ReconnectShaders.Core.Bridge_reconnectShaders import *


class MyApplication(QtGui.QMainWindow, Ui_Win_RigExplorer):

    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)

if __name__ != "__main__":
    try:
        app = QtGui.QApplication(sys.argv)
    except:
        app = QtCore.QCoreApplication.instance()
    
    window = MyApplication()
    
    """
    window.setWindowFlags(
        window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    """

    window.setWindowFlags(window.windowFlags())

    bridge = Bridge_reconnectShaders(window=window)

    window.show()

    try:
        sys.exit(app.exec_())
    except:
        "error al intentar salir"
