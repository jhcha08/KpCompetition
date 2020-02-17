
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
import os
from collections import OrderedDict


# In[1]:

## Np 평균

def Np_average(data): # data는 DF 형태
    Np_avr = [ ]
    
    for i in range(1, 367):
        for j in range(0, 24):
        
            # 0분부터 14분
            Np_data_00 = data[(data['min'] < 15) & (data['doy'] == i) & (data['hr'] == j)]['Np'].values
            avr_00 = np.nanmean(Np_data_00)
        
            # 15분부터 29분
            Np_data_15 = data[(data['min'] >= 15) & (data['min'] < 30) & (data['doy'] == i) 
                                & (data['hr'] == j)]['Np'].values
            avr_15 = np.nanmean(Np_data_15) 
            
            # 30분부터 44분
            Np_data_30 = data[(data['min'] >= 30) & (data['min'] < 45) & (data['doy'] == i) 
                                & (data['hr'] == j)]['Np'].values
            avr_30 = np.nanmean(Np_data_30)
        
            # 45분부터 59분
            Np_data_45 = data[(data['min'] >= 45) & (data['min'] <= 59) & (data['doy'] == i) 
                               & (data['hr'] == j)]['Np'].values
            avr_45 = np.nanmean(Np_data_45) 
        
            Np_avr.append(avr_00)
            Np_avr.append(avr_15)
            Np_avr.append(avr_30)
            Np_avr.append(avr_45)
    
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    
    Np_part = partition(Np_avr, int(len(Np_avr)/ 12)) 
    
    return Np_part


# In[2]:

## Tp 평균

def Tp_average(data): # data는 DF 형태
    Tp_avr = [ ]
   

    for i in range(1, 367):
        for j in range(0, 24):
        
            # 0분부터 14분
            Tp_data_00 = data[(data['min'] < 15) & (data['doy'] == i) & (data['hr'] == j)]['Tp'].values
            avr_00 = np.nanmean(Tp_data_00) 
        
            # 15분부터 29분
            Tp_data_15 = data[(data['min'] >= 15) & (data['min'] < 30) & (data['doy'] == i) 
                                & (data['hr'] == j)]['Tp'].values
            avr_15 = np.nanmean(Tp_data_15) 
        
            # 30분부터 44분
            Tp_data_30 = data[(data['min'] >= 30) & (data['min'] < 45) & (data['doy'] == i) 
                                & (data['hr'] == j)]['Tp'].values
            avr_30 = np.nanmean(Tp_data_30)
        
            # 45분부터 59분
            Tp_data_45 = data[(data['min'] >= 45) & (data['min'] <= 59) & (data['doy'] == i) 
                               & (data['hr'] == j)]['Tp'].values
            avr_45 = np.nanmean(Tp_data_45) 
        
            Tp_avr.append(avr_00)
            Tp_avr.append(avr_15)
            Tp_avr.append(avr_30)
            Tp_avr.append(avr_45)
    
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    
    Tp_part = partition(Tp_avr, int(len(Tp_avr)/ 12)) 
    
    return Tp_part


# In[3]:

## Vp 평균
def Vp_average(data): # data는 DF 형태
    Vp_avr = [ ]
    

    for i in range(1, 367):
        for j in range(0, 24):
        
            # 0분부터 14분
            Vp_data_00 = data[(data['min'] < 15) & (data['doy'] == i) & (data['hr'] == j)]['Vp'].values
            avr_00 = np.nanmean(Vp_data_00)
        
            # 15분부터 29분
            Vp_data_15 = data[(data['min'] >= 15) & (data['min'] < 30) & (data['doy'] == i) 
                                & (data['hr'] == j)]['Vp'].values
            avr_15 = np.nanmean(Vp_data_15)
        
            # 30분부터 44분
            Vp_data_30 = data[(data['min'] >= 30) & (data['min'] < 45) & (data['doy'] == i) 
                                & (data['hr'] == j)]['Vp'].values
            avr_30 = np.nanmean(Vp_data_30)
        
            # 45분부터 59분
            Vp_data_45 = data[(data['min'] >= 45) & (data['min'] <= 59) & (data['doy'] == i) 
                               & (data['hr'] == j)]['Vp'].values
            avr_45 = np.nanmean(Vp_data_45)
        
            Vp_avr.append(avr_00)
            Vp_avr.append(avr_15)
            Vp_avr.append(avr_30)
            Vp_avr.append(avr_45)
    
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    
    Vp_part = partition(Vp_avr, int(len(Vp_avr)/ 12)) 
    
    return Vp_part


# In[4]:

## B_gsm_x 평균

def B_gsm_x_average(data): # data는 DF 형태
    B_gsm_x_avr = [ ]
    

    for i in range(1, 367):
        for j in range(0, 24):
        
            # 0분부터 14분
            B_gsm_x_data_00 = data[(data['min'] < 15) & (data['doy'] == i) & (data['hr'] == j)]['Bgsm_x'].values
            avr_00 = np.nanmean(B_gsm_x_data_00)
        
            # 15분부터 29분
            B_gsm_x_data_15 = data[(data['min'] >= 15) & (data['min'] < 30) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_x'].values
            avr_15 = np.nanmean(B_gsm_x_data_15)
        
            # 30분부터 44분
            B_gsm_x_data_30 = data[(data['min'] >= 30) & (data['min'] < 45) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_x'].values
            avr_30 = np.nanmean(B_gsm_x_data_30)
        
            # 45분부터 59분
            B_gsm_x_data_45 = data[(data['min'] >= 45) & (data['min'] <= 59) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_x'].values
            avr_45 = np.nanmean(B_gsm_x_data_45) 
        
            B_gsm_x_avr.append(avr_00)
            B_gsm_x_avr.append(avr_15)
            B_gsm_x_avr.append(avr_30)
            B_gsm_x_avr.append(avr_45)
    
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    
    B_gsm_x_part = partition(B_gsm_x_avr, int(len(B_gsm_x_avr)/ 12)) 
    
    return B_gsm_x_part


# In[5]:

## B_gsm_y 평균

def B_gsm_y_average(data): # data는 DF 형태
    B_gsm_y_avr = [ ]
   

    for i in range(1, 367):
        for j in range(0, 24):
        
            # 0분부터 14분
            B_gsm_y_data_00 = data[(data['min'] < 15) & (data['doy'] == i) & (data['hr'] == j)]['Bgsm_y'].values
            avr_00 = np.nanmean(B_gsm_y_data_00) 
        
            # 15분부터 29분
            B_gsm_y_data_15 = data[(data['min'] >= 15) & (data['min'] < 30) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_y'].values
            avr_15 = np.nanmean(B_gsm_y_data_15)
        
            # 30분부터 44분
            B_gsm_y_data_30 = data[(data['min'] >= 30) & (data['min'] < 45) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_y'].values
            avr_30 = np.nanmean(B_gsm_y_data_30) 
        
            # 45분부터 59분
            B_gsm_y_data_45 = data[(data['min'] >= 45) & (data['min'] <= 59) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_y'].values
            avr_45 = np.nanmean(B_gsm_y_data_45) 
        
            B_gsm_y_avr.append(avr_00)
            B_gsm_y_avr.append(avr_15)
            B_gsm_y_avr.append(avr_30)
            B_gsm_y_avr.append(avr_45)
    
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    
    B_gsm_y_part = partition(B_gsm_y_avr, int(len(B_gsm_y_avr)/ 12)) 
    
    return B_gsm_y_part


# In[6]:

## B_gms_z 평균

def B_gsm_z_average(data): # data는 DF 형태
    B_gsm_z_avr = [ ]
    

    for i in range(1, 367):
        for j in range(0, 24):
        
            # 0분부터 14분
            B_gsm_z_data_00 = data[(data['min'] < 15) & (data['doy'] == i) & (data['hr'] == j)]['Bgsm_z'].values
            avr_00 = np.nanmean(B_gsm_z_data_00) / len(B_gsm_z_data_00)
        
            # 15분부터 29분
            B_gsm_z_data_15 = data[(data['min'] >= 15) & (data['min'] < 30) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_z'].values
            avr_15 = np.nanmean(B_gsm_z_data_15)
        
            # 30분부터 44분
            B_gsm_z_data_30 = data[(data['min'] >= 30) & (data['min'] < 45) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_z'].values
            avr_30 = np.nanmean(B_gsm_z_data_30)
        
            # 45분부터 59분
            B_gsm_z_data_45 = data[(data['min'] >= 45) & (data['min'] <= 59) & (data['doy'] == i) 
                                    & (data['hr'] == j)]['Bgsm_z'].values
            avr_45 = np.nanmean(B_gsm_z_data_45) 
        
            B_gsm_z_avr.append(avr_00)
            B_gsm_z_avr.append(avr_15)
            B_gsm_z_avr.append(avr_30)
            B_gsm_z_avr.append(avr_45)
    
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    
    B_gsm_z_part = partition(B_gsm_z_avr, int(len(B_gsm_z_avr)/ 12)) 
    
    return B_gsm_z_part


# In[7]:

## Bt 평균

def Bt_average(data): # data는 DF 형태
    Bt_avr = [ ]
   

    for i in range(1, 367):
        for j in range(0, 24):
        
            # 0분부터 14분
            Bt_data_00 = data[(data['min'] < 15) & (data['doy'] == i) & (data['hr'] == j)]['Bt'].values
            avr_00 = np.nanmean(Bt_data_00) / len(Bt_data_00)
        
            # 15분부터 29분
            Bt_data_15 = data[(data['min'] >= 15) & (data['min'] < 30) & (data['doy'] == i) 
                                & (data['hr'] == j)]['Bt'].values
            avr_15 = np.nanmean(Bt_data_15) 
        
            # 30분부터 44분
            Bt_data_30 = data[(data['min'] >= 30) & (data['min'] < 45) & (data['doy'] == i) 
                                & (data['hr'] == j)]['Bt'].values
            avr_30 = np.nanmean(Bt_data_30) 
        
            # 45분부터 59분
            Bt_data_45 = data[(data['min'] >= 45) & (data['min'] <= 59) & (data['doy'] == i) 
                               & (data['hr'] == j)]['Bt'].values
            avr_45 = np.nanmean(Bt_data_45) 
        
            Bt_avr.append(avr_00)
            Bt_avr.append(avr_15)
            Bt_avr.append(avr_30)
            Bt_avr.append(avr_45)
    
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    
    Bt_part = partition(Bt_avr, int(len(Bt_avr)/ 12)) 
    
    return Bt_part


# In[ ]:




# In[ ]:



