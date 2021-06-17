# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:59:57 2021

@author: Devineni
"""


import pandas as pd
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
# write all the variables that are inputs

location = "Herdern"

###############################################################################
# Variables

from sympy import *

v1, v2, v3 = symbols('V_1 V_2 V_3')
vdot_1, vdot_2, vdot_3, vdot_4 = symbols(r'{\dot{\mathrm{V}}}_{1} {\dot{\mathrm{V}}}_{2} {\dot{\mathrm{V}}}_{3} {\dot{\mathrm{V}}}_{4}')
taue1, taue2, taue3, taue4, taus1, taus2, taus3, taus4 = symbols(r"{\mathrm{\tau}}_{e_1} {\mathrm{\tau}}_{e_2} {\mathrm{\tau}}_{e_3} {\mathrm{\tau}}_{e_4} {\mathrm{\tau}}_{s_1} {\mathrm{\tau}}_{s_2} {\mathrm{\tau}}_{s_3} {\mathrm{\tau}}_{s_4}")
v23, tau_bar_3  = symbols(r"V_{23} {\left\langle\bar{\mathrm{\tau}}\right\rangle}_3")
tau_bar_e2, vdot_s = symbols(r"{\bar{\mathrm{\tau}}}_{e2} {\dot{\mathrm{V}}}_{s}")
tau2 = symbols(r"{\left\langle\bar{\mathrm{\tau}}\right\rangle}_2")
s = symbols(r"S")
tau_n1, tau_n2, tau_n3, tau_n23  = symbols(r"{\mathrm{\tau}}_{n_1} {\mathrm{\tau}}_{n_2} {\mathrm{\tau}}_{n_3} {\mathrm{\tau}}_{n_{23}}")
tau_bar_e1, tau_bar_e2, tau_bar_e23  = symbols(r"{\bar{\mathrm{\tau}}}_{e_1} {\bar{\mathrm{\tau}}}_{e_2} {\bar{\mathrm{\tau}}}_{e_{23}}")
sigma_squared = symbols(r"\mathrm{\sigma}^{2}")

###############################################################################
# Equations

if location == "Herdern":
    v23_val = 195.1 #m3

    eqn_vdot_s = (vdot_1 + vdot_2 + vdot_3)/2
    eqn_tau_bar_e2 = (((vdot_1 * taue1)/2) + ((vdot_2 * taue2)/2) + ((vdot_3 * taue3)/2) )/vdot_s
    eqn_tau_bar_e1 = (((vdot_1 * taus1)/2) + ((vdot_2 * taus2)/2) + ((vdot_3 * taus3)/2) )/vdot_s
else:
    v23_val = 145 #m3
    
    eqn_vdot_s = (vdot_1 + vdot_2 + vdot_3 + vdot_4)/2
    eqn_tau_bar_e2 = (((vdot_1 * taue1)/2) + ((vdot_2 * taue2)/2) + ((vdot_3 * taue3)/2) + ((vdot_4 * taue4)/2))/vdot_s
    eqn_tau_bar_e1 = (((vdot_1 * taus1)/2) + ((vdot_2 * taus2)/2) + ((vdot_3 * taus3)/2) + ((vdot_4 * taus4)/2))/vdot_s


eqn_tau2 = tau_bar_e2/2
eqn_v2 = ((vdot_s + v23/tau_bar_3)*(tau_bar_e2/3600))/(2 + tau_bar_e2/(tau_bar_3*3600))
eqn_vdot_3 = (v23 - v2)/tau_bar_3
eqn_vdot_2 = vdot_3 + vdot_s
eqn_s = 1-(vdot_s/vdot_2)
eqn_tau_n2 = v2 /vdot_2
eqn_v3 = v23 - v2
eqn_tau_n3 = v3 / vdot_3
e_rel_val = 0.5 # relativer Luftaustauschwirkungsgrad

eqn_f_of_s = log((1/(tau_n2*s + 1)) / ((1+(vdot_3/vdot_s)*(1- 1/(tau_n2*s + 1)*1/(tau_n3*s + 1)))))





###############################################################################
# Solutions


#%%

integer = 4
df = pd.read_excel("input_data.xlsx")
# input values
vdot_1_val, vdot_2_val, vdot_3_val, vdot_4_val = df.at[integer, 'dotV1'], df.at[integer, 'dotV2'], df.at[integer, 'dotV3'], df.at[integer, 'dotV4']
taue1_val, taue2_val, taue3_val, taue4_val = df.at[integer, 'tau_e1'], df.at[integer, 'tau_e2'], df.at[integer, 'tau_e3'], df.at[integer, 'tau_e4']
taus1_val, taus2_val, taus3_val, taus4_val = df.at[integer, 'tau_s1'], df.at[integer, 'tau_s2'], df.at[integer, 'tau_s3'], df.at[integer, 'tau_s4']

#evaluation
vdot_s_val = eqn_vdot_s.subs({vdot_1: vdot_1_val, vdot_2: vdot_2_val, 
                              vdot_3: vdot_3_val, vdot_4: vdot_4_val })

tau_bar_e2_val = eqn_tau_bar_e2.subs({vdot_1:vdot_1_val, taue1:taue1_val, vdot_2:vdot_2_val, 
                     taue2:taue2_val, vdot_3:vdot_3_val,taue3:taue3_val, 
                     vdot_4:vdot_4_val, taue4:taue4_val, vdot_s:vdot_s_val})

tau_bar_e1_val = eqn_tau_bar_e1.subs({vdot_1:vdot_1_val, taus1:taus1_val, vdot_2:vdot_2_val, 
                     taus2:taus2_val, vdot_3:vdot_3_val,taus3:taus3_val, 
                     vdot_4:vdot_4_val, taus4:taus4_val, vdot_s:vdot_s_val})

tau2_val = eqn_tau2.subs({tau_bar_e2:tau_bar_e2_val})

v2_val = eqn_v2.subs({vdot_s:vdot_s_val,v23: v23_val,tau_bar_e2:tau_bar_e2_val, tau_bar_3:df.at[integer, 'air age']})

vdot_3_val = eqn_vdot_3.subs({v23:v23_val,v2: v2_val,tau_bar_3:df.at[integer, 'air age'] })

vdot_2_val = eqn_vdot_2.subs({vdot_3: vdot_3_val,vdot_s: vdot_s_val })

s_val = eqn_s.subs({vdot_s:vdot_s_val, vdot_2:vdot_2_val})

tau_n2_val = eqn_tau_n2.subs({v2: v2_val, vdot_2:vdot_2_val  })

v3_val = eqn_v3.subs({v23:v23_val, v2: v2_val})

tau_n3_val = eqn_tau_n3.subs({v3:v3_val, vdot_3: vdot_3_val })

tau_n23_val = abs(Derivative(eqn_f_of_s, s).doit().subs({tau_n2:tau_n2_val, tau_n3: tau_n3_val, s:0, vdot_3:vdot_3_val, vdot_s:vdot_s_val}))

sigma_squared_val = Derivative(eqn_f_of_s, s, s).doit().subs({tau_n2:tau_n2_val, tau_n3: tau_n3_val, s:0, vdot_3:vdot_3_val, vdot_s:vdot_s_val})

mu3_val = Derivative(eqn_f_of_s, s, s, s).doit().subs({tau_n2:tau_n2_val, tau_n3: tau_n3_val, s:0, vdot_3:vdot_3_val, vdot_s:vdot_s_val})

mu4_val = Derivative(eqn_f_of_s, s, s, s, s).doit().subs({tau_n2:tau_n2_val, tau_n3: tau_n3_val, s:0, vdot_3:vdot_3_val, vdot_s:vdot_s_val})

sigma_squared_star_val = sigma_squared_val/pow(tau_n23_val,2)

tau_bar_e23_val = abs((sigma_squared_star_val + 1) * tau_n23_val)

alpha_23_val = tau_bar_e23_val/2

epsilon_a_23 = tau_n23_val/tau_bar_e23_val

tau_n1_val = tau_bar_e1_val/(2*3600)

#%%

prYellow("==============End of Execution================")
