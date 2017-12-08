from PySide import QtCore, QtGui


import Animacion.Maya_animation_rigsExplorer.Core.Core_RigExplorer
reload(Animacion.Maya_animation_rigsExplorer.Core.Core_RigExplorer)
from Animacion.Maya_animation_rigsExplorer.Core.Core_RigExplorer import *


class Bridge_RigsExplorer(object):
    def __init__(self, window):
        '''
        '''
        self.window = window

     
        # Fill blank spaces from UI
        self.PopulateUI()

    def PopulateUI(self):
        '''
        Fill empty field

        Create initial save and load paths from the current scene information.
        '''