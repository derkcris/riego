#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

"""
Archivo principal de ejecucion
Instancia los elementos necesarios para ejecutar la aplicacion
"""

import wx
import gettext
from ui import Ventana

class Aplicacion(wx.App):
    def OnInit(self):
        ventana = Ventana(None, wx.ID_ANY, "")
        self.SetTopWindow(ventana)
        ventana.Show()
        return True


if __name__ == "__main__":
    gettext.install("Riego") # replace with the appropriate catalog name

    app = Aplicacion(0)
    app.MainLoop()