# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:08:05 2021

@author: Raghavakrishna
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:26:23 2021

@author: Raghavakrishna
"""

import pandas as pd
import numpy as np
import statistics
from statistics import mean
import time
import datetime as dt
import matplotlib.pyplot as plt
import operator # for plotting
from uncertainties import ufloat

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
df = pd.read_excel("input_data.xlsx")

msg ="Please select an experiment"
title = "Experiment selection"
choices = df["name"].to_list()
choice = choicebox(msg, title, choices)


#%%
# write all the variables that are inputs

integer = df[df["name"]==choice].index[0]
location = df.at[integer, "location"]

dotV1, dotV2, dotV3, dotV4 = df.loc[integer, "dotV1"], df.loc[integer, "dotV2"],df.loc[integer, "dotV3"], df.loc[integer, "dotV4"]



#%%

class RandS:
    





#%%













