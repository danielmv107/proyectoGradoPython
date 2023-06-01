# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:19:22 2021

@author: DANIEL MEJIA VELEZ
@Cod: 1663916
"""

#Tratamiento de los datos
import numpy as np
import pandas as pd

#Preprocesamiento de los datos
#from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#from sklearn import tree



#Graficos
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

#import matplotlib.pyplot as plt 
 
import warnings
warnings.filterwarnings('once')





def botonAcc():
    
    dataSet= pd.read_csv('dataSet.csv', delimiter=',' , engine='python', encoding = "ISO-8859-1")
    df=pd.DataFrame(dataSet)
    #print(df.info())
    #Se crea un dataframe que contiene los datos de los estudiantes que calleron en bajo 
     
    #Se pasan los datos categoricos a one-hot-encoder
    df=pd.get_dummies(data=df, drop_first=True)
    
    #Se dropean los datos del archivo csv innecesarios
    df= df.drop(['id'], axis='columns')
    df= df.drop(['totalBajosRendimientos'], axis='columns')
    df= df.drop(['retiradoPorBajoRendimiento_SI'], axis='columns')
    
    explicativas = df.drop(columns='BajoRendimiento')
    
    #Se crea un dataframe que contiene los datos de los estudiantes que desertaron
    objetivo = df.BajoRendimiento
    
    
    
    #Variables predicción
    if comboTipoProg.get() == "1 (Pregrado)":
        carrera = 1
    else:
        carrera = 0
    
    if comboJornada.get() == "0 (Diurno)":
        jornada = 0
    else:
        jornada =1
        
    if comboSexo.get() == "1 (Masculino)":
        sexo = 1
    else:
        sexo = 0
    
    edadIngPred = float(edad.get())
    
    
    
    if comboCity.get() == "0 (Tuluá)":
        tulua = 0
        
    else:
        tulua = 1

    if comboExcep.get() == "0 (NO)":
        excep = 0
        
    else:
        excep = 1

    cantSemestre = float(semestres.get()) 

    promedio = float(promGen.get())
    ing = float(promIng.get())
    ciencias = float(promCien.get())
    otrasMate = float(promOtra.get())
    aprobados = float(credAproba.get())
    reprobados = float(credReproba.get())
    mateCance = float(canceladas.get())
    mateHabi = float(habilitadas.get())



    
    #Algoritmo de decision max_depth=10
    algoritmo = DecisionTreeClassifier(criterion="entropy", splitter="best", max_depth=10)
    
    #Entrenamiento del modelo utilizado
    algoritmo.fit(X=explicativas,y=objetivo)
    
    
    estudiante = np.array([carrera, edadIngPred, 0, tulua, excep, cantSemestre, promedio, ing, ciencias, otrasMate,
                           aprobados, reprobados, mateCance, mateHabi, sexo, jornada])
    
    matrEst = np.array([estudiante,estudiante])
    
    #Algoritmo de predicción
    prediccion = algoritmo.predict(matrEst)
    
    if(prediccion[1] == 1):
        des = "El estudiante tiende a incurrir en un bajo rendimiento académico "
    else:
        des = "El estudiante no tiende a incurrir en un bajo rendimiento académico"

    
    tk.messagebox.showinfo("Resultado",des,)


#funcion del boton CARGAR DATOS
def cargar():
        
    datos = np.loadtxt('dato.txt',delimiter=',')
    
    if datos[0] == 1:
        comboTipoProg.current(0)
    else:
        comboTipoProg.current(1)
        
    
    if datos[15] == 1:
        comboJornada.current(1)
    else:
        comboJornada.current(0)

    if datos[14] == 1:
        comboSexo.current(0)
    else:
        comboSexo.current(1)
    
    
    edad.delete(0,"end")   
    edad.insert(0,str(datos[1]))
    
    if datos[3] == 1:
        comboCity.current(1)
    else:
        comboCity.current(0)
        
    if datos[4] == 1:
        comboExcep.current(1)
    else:
        comboExcep.current(0)
    
    semestres.delete(0,"end")
    semestres.insert(0,str(datos[5]))
    
    promGen.delete(0,"end")
    promGen.insert(0,str(datos[6]))
    
    promIng.delete(0,"end")
    promIng.insert(0,str(datos[7]))
    
    promCien.delete(0,"end")
    promCien.insert(0,str(datos[8]))
    
    promOtra.delete(0,"end")
    promOtra.insert(0,str(datos[9]))
    
    credAproba.delete(0,"end")
    credAproba.insert(0,str(datos[10]))
    
    credReproba.delete(0,"end")
    credReproba.insert(0,str(datos[11]))
    
    canceladas.delete(0,"end")
    canceladas.insert(0,str(datos[12]))
    
    habilitadas.delete(0,"end")
    habilitadas.insert(0,str(datos[13]))


#diseño de la aplicaión 
#Interfaz
tkVent = tk.Tk()
tkVent.geometry("1000x647")
tkVent.resizable(0,0)
tkVent.iconbitmap('img/logoU.ico')
tkVent.config(bg="white")
tkVent.title("Sistema de alerta temprana")

#Creación de la imagen                
fondo = tk.PhotoImage(file="img/fondo.png")
labelFondo = tk.Label(tkVent,image=fondo).place(x=0, y=0)



fontStyle = tkFont.Font(family="times new roman", size=20)
labelTittle = tk.Label(tkVent, text="Sistema de alerta temprana de BRA", bg="#FFFFFF", font= fontStyle).place(x=300, y=80)


tk.Label(tkVent, text="Tipo de programa:", bg="#FFFFFF",font=("Verdana",14)).place(x=50,y=145)
comboTipoProg = ttk.Combobox(tkVent, state="readonly",font=("Verdana",12),width=13)
comboTipoProg["values"]=["1 (Pregrado)","0 (Tecnológico)"]
comboTipoProg.place(x=300,y =150)

tk.Label(tkVent, text="Jornada:", bg="#FFFFFF",font=("Verdana",14)).place(x=50,y=175)
comboJornada = ttk.Combobox(tkVent, state="readonly",font=("Verdana",12),width=13)
comboJornada["values"]=["0 (Diurno)","1 (Nocturno)"]
comboJornada.place(x=300,y =180)


tk.Label(tkVent, text="Sexo:", bg="#FFFFFF",font=("Verdana",14)).place(x=50,y=205)
comboSexo = ttk.Combobox(tkVent, state="readonly",font=("Verdana",12),width=13) 
comboSexo["values"]=["1 (Masculino)","0 (Femenino)"]
comboSexo.place(x=300,y =210)

tk.Label(tkVent, text="Edad de ingreso:", bg="#FFFFFF",font=("Verdana",14)).place(x=50,y=235)
edad = tk.Entry(tkVent,  width=6,font=("Verdana",12))
edad.place(x=300,y =240)



tk.Label(tkVent, text="Ciudad residencia:", bg="#FFFFFF",font=("Verdana",14)).place(x=50,y=265)
comboCity = ttk.Combobox(tkVent, state="readonly",font=("Verdana",12),width=13)
comboCity["values"]=["0 (Tuluá)","1 (Otro)"]
comboCity.place(x=300,y =270)


tk.Label(tkVent, text="Condicion de excepción:", bg="#FFFFFF",font=("Verdana",14)).place(x=50,y=295)
comboExcep = ttk.Combobox(tkVent, state="readonly",font=("Verdana",12),width=13)
comboExcep["values"]=["0 (NO)","1 (SI)"]
comboExcep.place(x=300,y =300)

tk.Label(tkVent, text="Semestres matriculados:", bg="#FFFFFF",font=("Verdana",14)).place(x=50,y=325)
semestres = tk.Entry(tkVent,  width=6,font=("Verdana",12))
semestres.place(x=300,y =330)


tk.Label(tkVent, text="Promedio general del estudiante:", bg="#FFFFFF",font=("Verdana",14)).place(x=500,y=145)
promGen = tk.Entry(tkVent,  width=6,font=("Verdana",12))
promGen.place(x = 880,y =145)

tk.Label(tkVent, text="Promedio de materias de Ingeniería:", bg="#FFFFFF",font=("Verdana",14)).place(x=500,y=175)
promIng = tk.Entry(tkVent,  width=6,font=("Verdana",12))
promIng.place(x = 880,y =175)

tk.Label(tkVent, text="Promedio de materias de Ciencias:", bg="#FFFFFF",font=("Verdana",14)).place(x=500,y=205)
promCien = tk.Entry(tkVent,  width=6,font=("Verdana",12))
promCien.place(x = 880,y =205)

tk.Label(tkVent, text="Promedio de otras materias:", bg="#FFFFFF",font=("Verdana",14)).place(x=500,y=235)
promOtra = tk.Entry(tkVent,  width=6,font=("Verdana",12))
promOtra.place(x = 880,y =235)

tk.Label(tkVent, text="Proporción creditos  aprobados:", bg="#FFFFFF",font=("Verdana",14)).place(x=500,y=265)
credAproba = tk.Entry(tkVent,  width=6,font=("Verdana",12))
credAproba.place(x = 880,y =265)


tk.Label(tkVent, text="Proporción creditos  reprobados:", bg="#FFFFFF",font=("Verdana",14)).place(x=500,y=295)
credReproba = tk.Entry(tkVent,  width=6,font=("Verdana",12))
credReproba.place(x = 880,y =295)


tk.Label(tkVent, text="Proporción materias canceladas:", bg="#FFFFFF",font=("Verdana",14)).place(x=500,y=325)
canceladas = tk.Entry(tkVent,  width=6,font=("Verdana",12))
canceladas.place(x = 880,y =325)

tk.Label(tkVent, text="Proporción materias habilitadas:", bg="#FFFFFF",font=("Verdana",14)).place(x=500,y=355)
habilitadas = tk.Entry(tkVent,  width=6,font=("Verdana",12))
habilitadas.place(x = 880,y =355)



tk.Label(tkVent, text="Daniel Mejia V.", bg="#FFFFFF").place(x=5,y=520)

boton = tk.Button(tkVent,text="Predicción", command=botonAcc, height=2, width=15,font=("Verdana",12))
boton.place(x=500,y=400)

Bcargar = tk.Button(tkVent,text="Cargar Datos", command=cargar, height=2, width=15,font=("Verdana",12))
Bcargar.place(x=300,y=400)

tk.Button(tkVent)

tkVent.mainloop()




