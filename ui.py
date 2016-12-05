#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import sys

class Ventana(wx.Frame):
    ingredientes = ["CaO - Nitrato de Calcio (26)",
               "N - Nitrato de Calcio (15.5)",
               "P205 - Fosfato Monopotasico (52)",
               "K20 - Fosfato Monopotasico (34)",
               "MgO - Nitrato de Magnesio (16)",
               "N - Nitrato de Magnesio (11)",
               "N - Acido Nitrico (15.5)",
               "K2O - Sultato de Potasio (50)"]
    ingredientesValor = [26, 15.5, 52, 34, 16, 11, 15.5, 50]

    def __init__(self, *args, **kwds):
        # begin wxGlade: Ventana.__init__
        kwds["style"] = wx.BORDER_SIMPLE | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.labelTitulo = wx.StaticText(self, wx.ID_ANY, _("Riego en flores"))
        self.panelCentral = wx.Panel(self, wx.ID_ANY)
        self.panelIzquierda = wx.Panel(self.panelCentral, wx.ID_ANY)
        self.labelDatos = wx.StaticText(self.panelIzquierda, wx.ID_ANY, _("Datos"))
        self.panelDatos = wx.Panel(self.panelIzquierda, wx.ID_ANY)
        self.labelVSuministrado = wx.StaticText(self.panelDatos, wx.ID_ANY, _("Volumen suministrado (L):"))
        self.textVSuministrado = wx.TextCtrl(self.panelDatos, wx.ID_ANY, "", style=wx.TE_CENTRE)
        self.labelVDrenado = wx.StaticText(self.panelDatos, wx.ID_ANY, _("Volumen drenado (L):"))
        self.textVDrenado = wx.TextCtrl(self.panelDatos, wx.ID_ANY, "", style=wx.TE_CENTRE)
        self.labelEfectividad = wx.StaticText(self.panelDatos, wx.ID_ANY, _("Efectividad (%):"))
        self.textEfectividad = wx.TextCtrl(self.panelDatos, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.labelVFinal = wx.StaticText(self.panelDatos, wx.ID_ANY, _("Volumen final (L):"))
        self.textVFinal = wx.TextCtrl(self.panelDatos, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.panelDerecha = wx.Panel(self.panelCentral, wx.ID_ANY)
        self.labelFormulas = wx.StaticText(self.panelDerecha, wx.ID_ANY, _("Formulas"))
        self.panelFormula = wx.Panel(self.panelDerecha, wx.ID_ANY)
        self.panelPPM = wx.Panel(self.panelFormula, wx.ID_ANY)
        self.textPPM = wx.TextCtrl(self.panelPPM, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.labelPPM = wx.StaticText(self.panelPPM, wx.ID_ANY, _("Partes por millon"))
        self.labelIgual = wx.StaticText(self.panelFormula, wx.ID_ANY, _("="))
        self.panelFormulaDerecha = wx.Panel(self.panelFormula, wx.ID_ANY)
        self.panelDividendo = wx.Panel(self.panelFormulaDerecha, wx.ID_ANY)
        self.panelFertilizante = wx.Panel(self.panelDividendo, wx.ID_ANY)
        self.textFertilizante = wx.TextCtrl(self.panelFertilizante, wx.ID_ANY, "", style=wx.TE_CENTRE)
        self.labelFertilizante = wx.StaticText(self.panelFertilizante, wx.ID_ANY, _("Fertilizante (gr)"))
        self.labelPor1 = wx.StaticText(self.panelDividendo, wx.ID_ANY, _("X"))
        self.panelIngredienteActivo = wx.Panel(self.panelDividendo, wx.ID_ANY)
        self.comboIngredienteActivo = wx.ComboBox(self.panelIngredienteActivo, wx.ID_ANY, choices=self.ingredientes, style=wx.CB_DROPDOWN)
        self.labelIngredienteActivo = wx.StaticText(self.panelIngredienteActivo, wx.ID_ANY, _("Ingrediente activo"))
        self.line = wx.StaticLine(self.panelFormulaDerecha, wx.ID_ANY)
        self.panelDivisor = wx.Panel(self.panelFormulaDerecha, wx.ID_ANY)
        self.panelAgua = wx.Panel(self.panelDivisor, wx.ID_ANY)
        self.textAgua = wx.TextCtrl(self.panelAgua, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.labelAgua = wx.StaticText(self.panelAgua, wx.ID_ANY, _("Agua (L)"))
        self.labelPor2 = wx.StaticText(self.panelDivisor, wx.ID_ANY, _("X"))
        self.panelConstante = wx.Panel(self.panelDivisor, wx.ID_ANY)
        self.textConstante = wx.TextCtrl(self.panelConstante, wx.ID_ANY, _("0.1"), style=wx.TE_CENTRE | wx.TE_READONLY)
        self.labelConstante = wx.StaticText(self.panelConstante, wx.ID_ANY, _("Constante"))
        self.static_line_1 = wx.StaticLine(self.panelDerecha, wx.ID_ANY)
        self.panelFormula1 = wx.Panel(self.panelDerecha, wx.ID_ANY)
        self.panelFertilizante1 = wx.Panel(self.panelFormula1, wx.ID_ANY)
        self.textFertilizante1 = wx.TextCtrl(self.panelFertilizante1, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.labelFertilizante1 = wx.StaticText(self.panelFertilizante1, wx.ID_ANY, _("Fertilizante (gr)"))
        self.labelIgual1 = wx.StaticText(self.panelFormula1, wx.ID_ANY, _("="))
        self.panelFormulaDerecha1 = wx.Panel(self.panelFormula1, wx.ID_ANY)
        self.panelDividendo1 = wx.Panel(self.panelFormulaDerecha1, wx.ID_ANY)
        self.panelPPM1 = wx.Panel(self.panelDividendo1, wx.ID_ANY)
        self.textPPM1 = wx.TextCtrl(self.panelPPM1, wx.ID_ANY, "", style=wx.TE_CENTRE)
        self.labelPPM1 = wx.StaticText(self.panelPPM1, wx.ID_ANY, _("Partes por millon"))
        self.labelPor11 = wx.StaticText(self.panelDividendo1, wx.ID_ANY, _("X"))
        self.panelAgua1 = wx.Panel(self.panelDividendo1, wx.ID_ANY)
        self.textAgua1 = wx.TextCtrl(self.panelAgua1, wx.ID_ANY, "", style=wx.TE_CENTRE | wx.TE_READONLY)
        self.labelAgua1 = wx.StaticText(self.panelAgua1, wx.ID_ANY, _("Agua (L)"))
        self.labelPor21 = wx.StaticText(self.panelDividendo1, wx.ID_ANY, _("X"))
        self.panelConstante1 = wx.Panel(self.panelDividendo1, wx.ID_ANY)
        self.textConstante1 = wx.TextCtrl(self.panelConstante1, wx.ID_ANY, _("0.1"), style=wx.TE_CENTRE | wx.TE_READONLY)
        self.labelConstante1 = wx.StaticText(self.panelConstante1, wx.ID_ANY, _("Constante"))
        self.line1 = wx.StaticLine(self.panelFormulaDerecha1, wx.ID_ANY)
        self.panelDivisor1 = wx.Panel(self.panelFormulaDerecha1, wx.ID_ANY)
        self.panelIngredienteActivo1 = wx.Panel(self.panelDivisor1, wx.ID_ANY)
        self.comboIngredienteActivo1 = wx.ComboBox(self.panelIngredienteActivo1, wx.ID_ANY, choices=self.ingredientes, style=wx.CB_DROPDOWN)
        self.labelIngredienteActivo1 = wx.StaticText(self.panelIngredienteActivo1, wx.ID_ANY, _("Ingrediente activo"))
        self.panelBotones = wx.Panel(self, wx.ID_ANY)
        self.buttonLimpiar = wx.Button(self.panelBotones, wx.ID_ANY, _("Limpiar"))
        self.buttonSalir = wx.Button(self.panelBotones, wx.ID_ANY, _("Salir"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.calcularDatos, self.textVSuministrado)
        self.Bind(wx.EVT_TEXT, self.calcularDatos, self.textVDrenado)
        self.Bind(wx.EVT_TEXT, self.calcularPPM, self.textFertilizante)
        self.Bind(wx.EVT_COMBOBOX, self.calcularPPM, self.comboIngredienteActivo)
        self.Bind(wx.EVT_TEXT, self.calcularFertilizante1, self.textPPM1)
        self.Bind(wx.EVT_COMBOBOX, self.calcularFertilizante1, self.comboIngredienteActivo1)
        self.Bind(wx.EVT_BUTTON, self.limpiar, self.buttonLimpiar)
        self.Bind(wx.EVT_BUTTON, self.salir, self.buttonSalir)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Ventana.__set_properties
        self.SetTitle(_("ventana"))
        self.SetSize((1024, 600))
        self.labelTitulo.SetFont(wx.Font(35, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
        self.labelDatos.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.labelFormulas.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.textPPM.SetToolTipString(_("Partes por millon"))
        self.labelPPM.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelPPM.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelIgual.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.textFertilizante.SetToolTipString(_("Fertilizante"))
        self.labelFertilizante.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelFertilizante.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelPor1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.comboIngredienteActivo.SetSelection(0)
        self.labelIngredienteActivo.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelIngredienteActivo.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.line.SetForegroundColour(wx.Colour(0, 0, 0))
        self.textAgua.SetToolTipString(_("Agua"))
        self.labelAgua.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelAgua.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelPor2.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.textConstante.SetToolTipString(_("Constante"))
        self.labelConstante.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelConstante.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelFertilizante1.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelFertilizante1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelIgual1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.labelPPM1.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelPPM1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelPor11.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelAgua1.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelAgua1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelPor21.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.labelConstante1.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelConstante1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.line1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.comboIngredienteActivo1.SetSelection(0)
        self.labelIngredienteActivo1.SetForegroundColour(wx.Colour(79, 79, 79))
        self.labelIngredienteActivo1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.panelCentral.SetMinSize((1000, 350))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Ventana.__do_layout
        mainBox = wx.BoxSizer(wx.VERTICAL)
        sizerBotones = wx.BoxSizer(wx.HORIZONTAL)
        sizerCentral = wx.FlexGridSizer(1, 2, 0, 20)
        sizerFormula = wx.BoxSizer(wx.VERTICAL)
        sizerFormulaInterno1 = wx.FlexGridSizer(1, 3, 5, 10)
        sizerFormulaDerecha1 = wx.BoxSizer(wx.VERTICAL)
        sizerDivisor1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerIngredienteActivo1 = wx.BoxSizer(wx.VERTICAL)
        sizerDividendo1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerConstante1 = wx.BoxSizer(wx.VERTICAL)
        sizerAgua1 = wx.BoxSizer(wx.VERTICAL)
        sizerPPM1 = wx.BoxSizer(wx.VERTICAL)
        sizerFertilizante1 = wx.BoxSizer(wx.VERTICAL)
        sizerFormulaInterno = wx.FlexGridSizer(1, 3, 5, 10)
        sizerFormulaDerecha = wx.BoxSizer(wx.VERTICAL)
        sizerDivisor = wx.BoxSizer(wx.HORIZONTAL)
        sizerConstante = wx.BoxSizer(wx.VERTICAL)
        sizerAgua = wx.BoxSizer(wx.VERTICAL)
        sizerDividendo = wx.BoxSizer(wx.HORIZONTAL)
        sizerIngredienteActivo = wx.BoxSizer(wx.VERTICAL)
        sizerFertilizante = wx.BoxSizer(wx.VERTICAL)
        sizerPPM = wx.BoxSizer(wx.VERTICAL)
        sizerDatos = wx.BoxSizer(wx.VERTICAL)
        gridFormula = wx.GridSizer(4, 2, 15, 17)
        mainBox.Add(self.labelTitulo, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        sizerDatos.Add(self.labelDatos, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)
        gridFormula.Add(self.labelVSuministrado, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        gridFormula.Add(self.textVSuministrado, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        gridFormula.Add(self.labelVDrenado, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        gridFormula.Add(self.textVDrenado, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        gridFormula.Add(self.labelEfectividad, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        gridFormula.Add(self.textEfectividad, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        gridFormula.Add(self.labelVFinal, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        gridFormula.Add(self.textVFinal, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.panelDatos.SetSizer(gridFormula)
        sizerDatos.Add(self.panelDatos, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.panelIzquierda.SetSizer(sizerDatos)
        sizerCentral.Add(self.panelIzquierda, 1, wx.ALL, 5)
        sizerFormula.Add(self.labelFormulas, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)
        sizerPPM.Add(self.textPPM, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizerPPM.Add(self.labelPPM, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelPPM.SetSizer(sizerPPM)
        sizerFormulaInterno.Add(self.panelPPM, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFormulaInterno.Add(self.labelIgual, 0, wx.ALIGN_CENTER, 0)
        sizerFertilizante.Add(self.textFertilizante, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizerFertilizante.Add(self.labelFertilizante, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelFertilizante.SetSizer(sizerFertilizante)
        sizerDividendo.Add(self.panelFertilizante, 0, 0, 0)
        sizerDividendo.Add(self.labelPor1, 0, wx.ALIGN_CENTER, 0)
        sizerIngredienteActivo.Add(self.comboIngredienteActivo, 0, 0, 0)
        sizerIngredienteActivo.Add(self.labelIngredienteActivo, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelIngredienteActivo.SetSizer(sizerIngredienteActivo)
        sizerDividendo.Add(self.panelIngredienteActivo, 0, 0, 0)
        self.panelDividendo.SetSizer(sizerDividendo)
        sizerFormulaDerecha.Add(self.panelDividendo, 1, 0, 0)
        sizerFormulaDerecha.Add(self.line, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        sizerAgua.Add(self.textAgua, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizerAgua.Add(self.labelAgua, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelAgua.SetSizer(sizerAgua)
        sizerDivisor.Add(self.panelAgua, 0, 0, 0)
        sizerDivisor.Add(self.labelPor2, 0, wx.ALIGN_CENTER, 0)
        sizerConstante.Add(self.textConstante, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizerConstante.Add(self.labelConstante, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelConstante.SetSizer(sizerConstante)
        sizerDivisor.Add(self.panelConstante, 0, 0, 0)
        self.panelDivisor.SetSizer(sizerDivisor)
        sizerFormulaDerecha.Add(self.panelDivisor, 1, 0, 0)
        self.panelFormulaDerecha.SetSizer(sizerFormulaDerecha)
        sizerFormulaInterno.Add(self.panelFormulaDerecha, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.panelFormula.SetSizer(sizerFormulaInterno)
        sizerFormula.Add(self.panelFormula, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizerFormula.Add(self.static_line_1, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 20)
        sizerFertilizante1.Add(self.textFertilizante1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizerFertilizante1.Add(self.labelFertilizante1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelFertilizante1.SetSizer(sizerFertilizante1)
        sizerFormulaInterno1.Add(self.panelFertilizante1, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFormulaInterno1.Add(self.labelIgual1, 0, wx.ALIGN_CENTER, 0)
        sizerPPM1.Add(self.textPPM1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizerPPM1.Add(self.labelPPM1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelPPM1.SetSizer(sizerPPM1)
        sizerDividendo1.Add(self.panelPPM1, 0, 0, 0)
        sizerDividendo1.Add(self.labelPor11, 0, wx.ALIGN_CENTER, 0)
        sizerAgua1.Add(self.textAgua1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizerAgua1.Add(self.labelAgua1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelAgua1.SetSizer(sizerAgua1)
        sizerDividendo1.Add(self.panelAgua1, 0, 0, 0)
        sizerDividendo1.Add(self.labelPor21, 0, wx.ALIGN_CENTER, 0)
        sizerConstante1.Add(self.textConstante1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizerConstante1.Add(self.labelConstante1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelConstante1.SetSizer(sizerConstante1)
        sizerDividendo1.Add(self.panelConstante1, 0, 0, 0)
        self.panelDividendo1.SetSizer(sizerDividendo1)
        sizerFormulaDerecha1.Add(self.panelDividendo1, 1, 0, 0)
        sizerFormulaDerecha1.Add(self.line1, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        sizerIngredienteActivo1.Add(self.comboIngredienteActivo1, 0, 0, 0)
        sizerIngredienteActivo1.Add(self.labelIngredienteActivo1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panelIngredienteActivo1.SetSizer(sizerIngredienteActivo1)
        sizerDivisor1.Add(self.panelIngredienteActivo1, 0, 0, 0)
        self.panelDivisor1.SetSizer(sizerDivisor1)
        sizerFormulaDerecha1.Add(self.panelDivisor1, 1, 0, 0)
        self.panelFormulaDerecha1.SetSizer(sizerFormulaDerecha1)
        sizerFormulaInterno1.Add(self.panelFormulaDerecha1, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.panelFormula1.SetSizer(sizerFormulaInterno1)
        sizerFormula.Add(self.panelFormula1, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.panelDerecha.SetSizer(sizerFormula)
        sizerCentral.Add(self.panelDerecha, 1, wx.ALL, 5)
        self.panelCentral.SetSizer(sizerCentral)
        mainBox.Add(self.panelCentral, 1, 0, 0)
        sizerBotones.Add(self.buttonLimpiar, 0, wx.ALIGN_CENTER, 0)
        sizerBotones.Add(self.buttonSalir, 0, wx.ALIGN_CENTER, 0)
        self.panelBotones.SetSizer(sizerBotones)
        mainBox.Add(self.panelBotones, 1, wx.ALIGN_CENTER, 0)
        self.SetSizer(mainBox)
        self.Layout()
        self.Centre()
        # end wxGlade

    def calcularPPM(self, event):  # wxGlade: Ventana.<event_handler>
        try:
            fertilizante = float(self.textFertilizante.Value)
            ingrediente = self.ingredientesValor[self.comboIngredienteActivo.CurrentSelection]
            agua = float(self.textAgua.Value)
            constante = float(self.textConstante.Value)

            ppm =  round((fertilizante * ingrediente) / (agua * constante), 2)
            self.textPPM.Value = str(ppm)
        except ValueError:
            self.textPPM.Value = ""

    def calcularFertilizante1(self, event):  # wxGlade: Ventana.<event_handler>
        try:
            ppm = float(self.textPPM1.Value)
            ingrediente = self.ingredientesValor[self.comboIngredienteActivo1.CurrentSelection]
            agua = float(self.textAgua1.Value)
            constante = float(self.textConstante1.Value)

            fertilizante =  round((ppm * agua * constante) / ingrediente, 2)
            self.textFertilizante1.Value = str(fertilizante)
        except ValueError:
            self.textFertilizante1.Value = ""

    def calcularDatos(self, event):  # wxGlade: Ventana.<event_handler>
        try:
            vsuministrado = float(self.textVSuministrado.Value)
            vdrenado = float(self.textVDrenado.Value)
            efectividad = round(vdrenado / vsuministrado, 4) * 100
            vfinal = vsuministrado
            if efectividad < 30:
                vfinal = vfinal + 100
            if efectividad > 50:
                vfinal = vfinal - 80
            # Mostrar resultados
            self.textEfectividad.Value = str(efectividad)
            self.textVFinal.Value = str(vfinal)
            self.textAgua.Value = str(vfinal)
            self.textAgua1.Value = str(vfinal)

            self.calcularPPM(event)
            self.calcularFertilizante1(event)

        except ValueError:
            self.limpiar_agua()

    def limpiar(self, event):  # wxGlade: Ventana.<event_handler>
        self.limpiar_agua()
        self.textVSuministrado.Value = ""
        self.textVDrenado.Value = ""
        self.textPPM.Value = ""
        self.textFertilizante.Value = ""
        self.textPPM1.Value = ""
        self.textFertilizante1.Value = ""

    def limpiar_agua(self):
        self.textEfectividad.Value = ""
        self.textVFinal.Value = ""
        self.textAgua.Value = ""
        self.textAgua1.Value = ""

    def salir(self, event):  # wxGlade: Ventana.<event_handler>
        wx.MessageBox("- Monica Barahona\n- Yurani Velasco", 'Creado por:', wx.OK | wx.ICON_INFORMATION)
        sys.exit(1)