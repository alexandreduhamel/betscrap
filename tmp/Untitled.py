#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


def calc_odds_prob(odds):
    return 1/odds

def calc_return_rate(odds):
    return np.sum(calc_odds_prob(odds))

def calc_odds_norm(odds, rr):
    return odds / rr

def is_surebet(odds, rr):
    return rr < 1

def calc_return_gain_rate(rr):
    return 100 / rr

