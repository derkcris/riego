# !/usr/bin/env python
import wx

app = wx.App(False)  # Crear la ventana
frame = wx.Frame(None, wx.ID_ANY, "Riego")  # Configurar la ventana con el titulo
frame.Show(True)  # Mostrar la ventana
app.MainLoop()