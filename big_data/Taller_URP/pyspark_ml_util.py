###################################################################################
#   Organizacion     : XXXXXX
#   Programa         : pyspark_ml_util.py
#                      /ruta/xxxx.py
#   Creado por       : Nombre
#   Fecha Creacion   : 07/09/2018
#   Proposito        : xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#                      xxxxxxxxxxxxxxxxxxx
#   Fuentes de datos :
#   Destino          : /rutadestino
#                    : 
#   Modificaciones   :
#      Correlativo       :
#      Modificado por    :
#      Fecha Modificacion:
#      Descripcion       :
###################################################################################
from __future__ import division
import numpy as np
import pandas as pd
import scipy as sp
import imblearn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (precision_score, recall_score,f1_score,accuracy_score,confusion_matrix)

def density_chart(target,probabilidad_1):
    """es la funcion de densidad"""
    dftotal=pd.DataFrame({'target':target,'p1':probabilidad_1})
    sns.kdeplot(dftotal.loc[dftotal['target']==1,'p1'],shade=True,color='orangered',alpha=0.7,label='For class 1' )
    sns.kdeplot(dftotal.loc[dftotal['target']==0,'p1'],shade=True,color='royalblue',alpha=0.5,label='For class 0')
    plt.subplots_adjust(top=1.5,right=2.5)

    plt.legend(fontsize=15)
    plt.xlim(0,1)
    plt.title('Density Chart',size=20)
    plt.ylabel('Probability Density',size=15)
    plt.xlabel('Predicted Probability',size=15)

    median_1=round(dftotal.loc[dftotal['target']==1,'p1'].median(),2)
    median_0=round(dftotal.loc[dftotal['target']==0,'p1'].median(),2)

    plt.axvline(median_1,color='orangered',ls='dotted',alpha=1)
    plt.axvline(median_0,color='royalblue',ls='dotted',alpha=1)
    
    plt.text(median_0,-0.11,median_0,size=13,color='royalblue')
    plt.text(median_1,-0.11,median_1,size=13,color='orangered')
    
    x=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.99]
    plt.xticks(x,['0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','0.99'],fontsize=13)
    plt.grid()
    plt.show()

def acumulado(valor):
    total=0
    for i in valor:
        total=total+i
        yield total
        
def reporte_ganancia_lift(y_real,prob1,cuantiles):

    ##################################################  TABLA ############################################
    df=pd.DataFrame({'y_real':y_real,'prob1':prob1}).sort_values(by='prob1',ascending=False)
    df['contador']=np.arange(len(y_real))
    df['cuantiles']=pd.qcut(df['contador'],cuantiles,labels=False)
    
    tabla=pd.concat([pd.crosstab(df['cuantiles'],columns=df['y_real']),pd.crosstab(df['cuantiles'],columns='count')],axis=1)
    
    tabla['por_Q_Planta']=(tabla['count']/sum(tabla['count'])*100).round(0).astype(int)
    tabla['por_Q_Portados']=(tabla[1]/sum(tabla[1])*100).round(0).astype(int)
    tabla['Q_Planta_acum']=pd.DataFrame(list(acumulado(tabla['count'])))
    tabla['por_Q_Planta_acum']=(tabla['Q_Planta_acum']/sum(tabla['count'])*100).round(0).astype(int)
    tabla['churn_porta_acum']=list(acumulado(tabla[1]))
    tabla['Ganancia']=(tabla['churn_porta_acum']/sum(tabla[1])*100).round(0).astype(int)
    tabla['Efectividad']=(tabla['churn_porta_acum']/tabla['Q_Planta_acum']*100).round(0).astype(int)
    tabla['Lift']=(tabla['por_Q_Portados']/tabla['por_Q_Planta'])
  
  
    ################################################### CURVA GANANCIA###############################
   
    fig, ax = plt.subplots(1)
    
    index = np.arange(cuantiles)
    bar_width = 0.7

    rects1 = plt.bar(index, tabla['Ganancia'], bar_width, color='orangered',label='Gain', alpha= 0.8)
    rects2 = plt.plot(index,tabla['Efectividad'], color='royalblue',label='Efectividad', alpha= 2,linewidth=5.0)
    
    
    plt.xlabel('%Pobla',size=20)
    plt.ylabel('%churns contactados',size=20)
    plt.title('Ganancia por %Efectividad - %',size=25)
    plt.subplots_adjust(top=1.5, right=3)
    plt.legend(fontsize=15,loc=9)
   
    # Agregando los datos a los graficos
    for i,j in tabla['Efectividad'].items():
        ax.annotate(str(j)+'%', xy=(i, j),size=15)
    
    
    for i,j in tabla['Ganancia'].items():
        ax.annotate(str(j)+'%', xy=(i, j),size=15)
        
    
    # Formato de los ejes
    x=[]
    for i in range(1,cuantiles+1):
        x.append(str(int(100/cuantiles*i))+'%')
    plt.xticks(index, x,fontsize=13)
    
    y=[0,20,40,60,80,100]
    plt.yticks(y,['0%','20%','40%','60%','80%','90%','100%'],fontsize=13)
    plt.grid()
    
    ################################################### CURVA LIFT ###########################################
   
    fig1, ax1 = plt.subplots(1)
    
    index = np.arange(cuantiles)

    rect2 = plt.bar(index,tabla['Lift'],color='royalblue',label='Lift')
     
    plt.xlabel('Cuantiles',size=20)
    plt.title('Lift',size=25)
    plt.subplots_adjust(top=1.5, right=3)
    plt.legend(fontsize=15,loc=9)
   
    # Agregando los datos a los graficos
    for i,j in tabla['Lift'].items():
        ax1.annotate(str(j), xy=(i,j),size=15)
    
    plt.axhline(1,color='red',alpha= 2,linewidth=3,ls='dotted')
    plt.xticks(index,np.arange(1,cuantiles+1),fontsize=13)
    plt.grid()
    
def indicadores_modelos(y_real,prob1):
    dftotal=pd.DataFrame({'y_real':y_real,'p1':prob1})
    
    for i in range(0,len(dftotal)):
        if dftotal.loc[i,'p1']>=0.5:
            dftotal.loc[i,'pred']=1
        else:
            dftotal.loc[i,'pred']=0

        
    Precision=round(precision_score(dftotal['y_real'], dftotal['pred']),2)
    Recall=round(recall_score(dftotal['y_real'],dftotal['pred']),2)
    F1_Score=round(f1_score(dftotal['y_real'], dftotal['pred']),2)
    Accuracy=round(accuracy_score(dftotal['y_real'], dftotal['pred']),2)
    df=pd.DataFrame({'metricas_name':['Precision', 'Recall','F1_Score','Accuracy'],
                     'porcentaje':[Precision*100, Recall*100, F1_Score*100, Accuracy*100]
                    })  
    fig,ax= plt.subplots(1)
    plt.barh(df['metricas_name'],df['porcentaje'], align='center',color=['red','green','orange','royalblue'])


    for i in ax.patches:
        ax.text(i.get_width()+.3, i.get_y()+.38, str(i.get_width())+'%', fontsize=15,color='black')

    x=[0,50,100]
    plt.xticks(x,['0%','50%','100%'],fontsize=15)
    plt.grid()

    plt.yticks(fontsize=15)

    plt.xlim(0,100)
    plt.grid()
    plt.subplots_adjust(top=1, right=1.5)
    plt.title('Resultados',size=20)
    plt.show()

