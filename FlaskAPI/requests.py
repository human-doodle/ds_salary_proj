# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:59:33 2020

@author: Shivani
"""

import requests
from data_input import data_in

URL='http://127.0.0.1:5000/predict'
headers={"Content-Type": "application/json"}
data={"input":data_in}

r=requests.get(URL,headers=headers, json=data)

