# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:12:09 2018
@author: Pramukh swami
"""

import requests

key = str(input("Enter your API Key: "))
headers = {"content-type":"application/json", "x-api-key":key}

def recent_films():
    url = "http://www.api.shortfundly.com/film/recent_films"
    r = requests.get(url, headers=headers).json()
    print(r)
    
def recent_telugu():
    url = "http://www.api.shortfundly.com/film/recent_telugu"
    r = requests.get(url, headers=headers).json()
    print(r)

def recent_malayalam():
    url = "http://www.api.shortfundly.com/film/recent_malayalam"
    r = requests.get(url, headers=headers).json()
    print(r)

def recent_kannada():
    url = "http://www.api.shortfundly.com/film/recent_kannada"
    r = requests.get(url, headers=headers).json()
    print(r)

def toprated():
    url = "http://www.api.shortfundly.com/film/toprated"
    r = requests.get(url, headers=headers).json()
    print(r)
    
i=0
while(i!=5):
    i = int(input("***CHOICES***\n1.For Recent Films\n2.For Telugu Films\n3. For Malyalam Films\n4. For Kanada Films\n5. For Toprated Films\n"))
    if(i==1):
        recent_films()
        break
    if(i==2):
        recent_telugu()
        break
    if(i==3):
        recent_malayalam()
        break
    if(i==4):
        recent_kannada()
        break
    if(i==5):
        recent_kannada()
        break