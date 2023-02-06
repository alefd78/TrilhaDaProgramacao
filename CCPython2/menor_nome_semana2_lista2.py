# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:16:13 2023

@author: Davi SD
"""


def menor_nome(nomes):
    for l in range(len(nomes)):
        nomes[l] = nomes[l].strip().lower().capitalize()

    menorNome = nomes[0]

    for l in range(len(nomes)):

        if (len(menorNome) > len(nomes[l])):
            menorNome = nomes[l]

    return (menorNome)
    # return(menorNome.strip().lower().capitalize())