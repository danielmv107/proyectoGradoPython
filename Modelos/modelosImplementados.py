# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:19:22 2021

@author: DANIEL MEJIA VELEZ
@Cod: 1663916
"""

#Tratamiento de los datos

import pandas as pd



#Preprocesamiento de los datos
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


from sklearn.svm import SVC
import sklearn.metrics as skM 

#Metricas del modelo
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score


#Graficos
import matplotlib.pyplot as plt 
 
import warnings
warnings.filterwarnings('once')


dataSet= pd.read_csv('dataSet.csv', delimiter=',' , engine='python', encoding = "ISO-8859-1")
df=pd.DataFrame(dataSet)
#print(df.info())
#Se crea un dataframe que contiene los datos de los estudiantes que calleron en bajo 
y = df['BajoRendimiento']


df=pd.get_dummies(data=df, drop_first=True)


#Se dropean los datos del archivo csv innecesarios
df= df.drop(['id'], axis='columns')
df= df.drop(['BajoRendimiento'], axis='columns')
df= df.drop(['totalBajosRendimientos'], axis='columns')
df= df.drop(['retiradoPorBajoRendimiento_SI'], axis='columns')





datasetFinal = pd.concat([df], axis='columns')





#print(datasetFinal.info())



#Split de los datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(datasetFinal, y,
                                                    test_size = 0.25,
                                                    random_state = 42,
                                                    stratify = y)


#Algoritmo de decision 
algoritmo = DecisionTreeClassifier(criterion='entropy', splitter="best", max_depth=12)

#Entrenamiento del modelo utilizado
algoritmo.fit(X_train, y_train)

#Algoritmo de predicción
y_pred = algoritmo.predict(X_test)



#*********************************************************
#Se pasan los datos al SVM
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
predic = svm.predict(X_test)

#X_test.to_csv(r'C:\Users\DANIEL\Desktop\TG1\actualizado\prediccion.csv',encoding='utf-8', header=True)

print("********Árbol de decisión***********")
matriz = confusion_matrix(y_test, y_pred)
print("Matriz de confusion")
print(matriz)
print()


#Relacion entre las predicciones correctas y el numero total de predicciones
#Con que frecuencia es correcto el clasificador
exactitud = accuracy_score(y_test, y_pred)
print("Exactitud del modelo") #vp+vn/vp+fp+fn+vn
print(exactitud)
print()

#Relacion entre las predicciones correctas y el numero total de predicciones
#correctas previstas, mide la precision del modelo a la hora de predecir casos positivos
precision = precision_score(y_test, y_pred)
print("Presicion del modelo")
print(precision)
print()

#Relacion entre las predicciones positivas correctas y el numero total de predicciones
#positivas o cuan sensible es el modelo para detectar instancias positivas.
sensibilidad = recall_score(y_test, y_pred) #vp/vp+fn
print("Sensibilidad del modelo") # vp/vp+fn
print(sensibilidad)
print()

#El puntaje F1 es la medida armonica de la memoria y la precision,
#con un puntuacion mas alta, mejor es el modelo.
puntaje = f1_score(y_test, y_pred)
print("medida armonica del modelo")
print(puntaje)
print()


print("Curva ROC")
fpr, tpr, _ = skM.roc_curve(y_test,  y_pred)
auc = skM.roc_auc_score(y_test, y_pred)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show() 

print("\n")
print("**************SVM******************")
matriz = confusion_matrix(y_test, predic)
print("Matriz de confusion")
print(matriz)
print()

#Relacion entre las predicciones correctas y el numero total de predicciones
#Con que frecuencia es correcto el clasificador
exactitud = accuracy_score(y_test, predic)
print("Exactitud del modelo") #vp+vn/vp+fp+fn+vn
print(exactitud)
print()

#Relacion entre las predicciones correctas y el numero total de predicciones
#correctas previstas, mide la precision del modelo a la hora de predecir casos positivos
precision = precision_score(y_test, predic)
print("Presicion del modelo")
print(precision)
print()

#Relacion entre las predicciones positivas correctas y el numero total de predicciones
#positivas o cuan sensible es el modelo para detectar instancias positivas.
sensibilidad = recall_score(y_test, predic) #vp/vp+fn
print("Sensibilidad del modelo") # vp/vp+fn
print(sensibilidad)
print()

#El puntaje F1 es la medida armonica de la memoria y la precision,
#con un puntuacion mas alta, mejor es el modelo.
puntaje = f1_score(y_test, predic)
print("medida armonica del modelo")
print(puntaje)
print()


print("Curvas ROC")
aucAr = skM.roc_auc_score(y_test, y_pred)
aucSVM = skM.roc_auc_score(y_test, predic)
print("Arboles "+str(aucAr))
print("SVM "+str(aucSVM))

a_fpr, a_tpr, _ = skM.roc_curve(y_test,  y_pred)
svm_fpr, svm_tpr, _ = skM.roc_curve(y_test, predic)

plt.plot(a_fpr,a_tpr,label='auc Árbol de decisión= %0.3f' % aucAr)
plt.plot(svm_fpr,a_tpr,label='auc SVM= %0.3f' % aucSVM)

plt.title('Curva ROC')
plt.legend(loc=4)
plt.xlabel('1-especificidad')
plt.ylabel('Sensibilidad')
plt.show()






