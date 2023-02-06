# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:05:59 2023

@author: Davi SD
"""

def maiusculas(frase):
    letras = " "
    fraseMinuscula = frase.lower()
    for l in range(len(frase)):
        if(fraseMinuscula[l] > frase[l]):
           letras = letras + frase[l]
           #print(frase[l], end = '')
    return(letras.strip())
