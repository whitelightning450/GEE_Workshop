#!/usr/bin/env python
# coding: utf-8

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error 
import hydroeval as he
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Model_Evaluation_Plots(DF, predictions):

# Subplots.
    fig, ax = plt.subplots(1,1, figsize=(8, 7))
    fig.patch.set_facecolor('white')

    #set min/max for y-axis of the predictions/observations
    ymin = min(DF['flow_cfs'])*1.1
    ymax = max(DF['flow_cfs'])*1.1
    
    #add color options
    colors = ['blue', 'orange', 'red','green']


    # Add predictions to plot
    for pred in np.arange(0, len(predictions),1):
        ax.scatter(DF['flow_cfs'], DF[predictions[pred]],
                   c=colors[pred], alpha=0.35, label=predictions[pred])

     # Add some parameters.
    ax.set_title('Streamflow Predictions', fontsize=16)
    ax.set_xlabel('Observations (cfs)', fontsize=14)
    ax.set_ylabel('Predictions (cfs)', fontsize=14,)
    ax.set_ylim(ymin, ymax)
    ax.set_xlim(ymin, ymax)
    ax.legend(fontsize=14, loc='upper right')
    
    #Add a 1:1 prediction:observation plot
    ax.plot((0,ymax),(0,ymax), linestyle = '--', color  = 'red')

    plt.show()
    
    
def Hydrograph_Evaluation_Plots(DF, predictions):

# Subplots.
    fig, ax = plt.subplots(1,1, figsize=(8, 7))
    fig.patch.set_facecolor('white')

    #set min/max for y-axis of the predictions/observations
    ymin = min(DF['flow_cfs'])*1.1
    ymax = max(DF['flow_cfs'])*1.1
    
    #add color options
    colors = ['blue', 'red','green']
    
    ax.plot(DF['DOY'], DF['flow_cfs'],
                   c='orange', alpha=0.35, label= 'Observed')

    # Add predictions to plot
    for pred in np.arange(0, len(predictions),1):
        ax.plot(DF['DOY'], DF[predictions[pred]],
                   c=colors[pred], alpha=0.35, label=predictions[pred])

     # Add some parameters.
    ax.set_title('Streamflow Predictions', fontsize=16)
    ax.set_xlabel('Time (DOY)', fontsize=14)
    ax.set_ylabel('Streamflow (cfs)', fontsize=14,)
    ax.set_ylim(0, ymax)
    ax.legend(fontsize=14, loc='upper right')

    plt.show()
    

#Define some key model performance metics: RMSE, PBias, MAE, MAPE
def RMSE(DF, predictions):
    for pred in np.arange(0, len(predictions),1):
        rmse = mean_squared_error(DF['flow_cfs'], DF[predictions[pred]], squared=False)
        print('RMSE for ', predictions[pred], ' is ', rmse, ' cfs')

def MAPE(DF, predictions):
    for pred in np.arange(0, len(predictions),1):
        mape = round(mean_absolute_percentage_error(DF['flow_cfs'], DF[predictions[pred]])*100, 2)
        print('Mean Absolute Percentage Error for ', predictions[pred], ' is ', mape, '%')
        
def PBias(DF, predictions):
    for pred in np.arange(0, len(predictions),1):
        pbias = he.evaluator(he.pbias,  DF[predictions[pred]], DF['flow_cfs'])
        pbias = round(pbias[0],2)
        print('Percentage Bias for ', predictions[pred], ' is ', pbias, '%')
        
def KGE(DF, predictions):
    for pred in np.arange(0, len(predictions),1):
        kge, r, alpha, beta = he.evaluator(he.kge,  DF[predictions[pred]], DF['flow_cfs'])
        kge = round(kge[0],2)
        print('Kling-Glutz Efficiency for ', predictions[pred], ' is ', kge)
        

