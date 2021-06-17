# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 10:51:44 2021

@author: Devineni
"""

import numpy as np
import statistics
from statistics import mean
import time
import datetime as dt
import matplotlib.pyplot as plt
import operator # for plotting

from openpyxl import load_workbook

# import mysql.connector
import os
import pymysql
from sqlalchemy import create_engine

from easygui import *
import sys

from sklearn.linear_model import LinearRegression

def prRed(skk): print("\033[31;1;m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[33;1;m {}\033[00m" .format(skk))

#%% 
import pandas as pd
i = 4
df = pd.read_excel("input_data.xlsx")
df.at[i,"bar(tau)e,2"] = ((df.at[i,"dotV1"]*df.at[i,"tau_e1"]/2) 
                          + (df.at[i,"dotV2"]*df.at[i,"tau_e2"]/2) 
                          + (df.at[i,"dotV3"]*df.at[i,"tau_e3"]/2))/df.at[i,"dot(V)s"]
df.at[i,"bar(tau)e,1"] = ((df.at[i,"dotV1"]*df.at[i,"tau_s1"]/2) 
                          + (df.at[i,"dotV2"]*df.at[i,"tau_s2"]/2) 
                          + (df.at[i,"dotV3"]*df.at[i,"tau_s3"]/2))/df.at[i,"dot(V)s"]

df.at[i, "[tau]2"] = df.at[i,"bar(tau)e,2"]/2
df.at[i, "V2"] = df.at[i,"bar(tau)e,2"]*df.at[i,"dot(V)s"] 



#%%
from sympy import *
tau_bar_e2, vdot_s, v23, tau_bar_3 = symbols(r'{\bar{\mathrm{\tau}}}_{e2} {\dot{\mathrm{V}}}_{s} V_23 {\left\langle\bar{\mathrm{\tau}}\right\rangle}_3') 
v1, v2, v3 = symbols('V_1 V_2 V_3')
vdot_1, vdot_2, vdot_3 = symbols(r'{\dot{\mathrm{V}}}_{1} {\dot{\mathrm{V}}}_{2} {\dot{\mathrm{V}}}_{3}')

vdot_23 = symbols(r'{\dot{\mathrm{V}}}_{23}')

alpha1, alpha2, alpha3, alpha = symbols(r'{\left\langle\bar{\mathrm{\alpha}}\right\rangle}_1 {\left\langle\bar{\mathrm{\alpha}}\right\rangle}_2 {\left\langle\bar{\mathrm{\alpha}}\right\rangle}_3 {\left\langle\bar{\mathrm{\alpha}}\right\rangle}')
eqn_v2 = ((vdot_s + v23/tau_bar_3)*(tau_bar_e2/3600))/(2 + tau_bar_e2/(tau_bar_3*3600))
dic = {vdot_s:df.at[i,"dot(V)s"], v23: 195.1, tau_bar_3: df.at[i,"air age"], tau_bar_e2: df.at[i,"bar(tau)e,2"]  }
eqn_v2.subs(dic)
#%% Equation 1
from sympy import *
t2,t3, s, q3, q23 = symbols('t2, t3, s, q3, q23') 
#v1, v2, v3 , alpha1, alpha2, alpha3, vdot, 


expr = log((1/(t2*s + 1)) / ((1+(q3/q23)*(1- 1/(t2*s + 1)*1/(t3*s + 1)))))
print("Expression : {} ".format(expr)) 
# Use sympy.Derivative() method 
expr_diff = Derivative(expr, s, s, s, s) 
  
print("Value of the derivative : {} ".format(expr_diff.doit())) 
expr_diff.doit().subs({t2:1, t3: 1, s:0, q3:1, q23:1})
expr_diff


#%%

# %%
v1, v2, v3 = symbols('V_1 V_2 V_3')
vdot_1, vdot_2, vdot_3 = symbols(r'{\dot{\mathrm{V}}}_{1} {\dot{\mathrm{V}}}_{2} {\dot{\mathrm{V}}}_{3}')

vdot_23 = symbols(r'{\dot{\mathrm{V}}}_{23}')

alpha1, alpha2, alpha3, alpha = symbols(r'{\left\langle\bar{\mathrm{\alpha}}\right\rangle}_1 {\left\langle\bar{\mathrm{\alpha}}\right\rangle}_2 {\left\langle\bar{\mathrm{\alpha}}\right\rangle}_3 {\left\langle\bar{\mathrm{\alpha}}\right\rangle}')

eqn = v1 + v2 + v3**2 + alpha + vdot_23 + vdot_1
eqn



#%%


#%%
prYellow("==============End of Execution================")
