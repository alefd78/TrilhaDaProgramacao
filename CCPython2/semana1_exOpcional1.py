# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:54:15 2023

@author: Davi SD
"""


def imprime_matriz(mat):
    linha = len(mat)
    coluna = len(mat[0])
    for l in range(linha):

        for c in range(coluna):
            x = str(mat[l][c])

            if (c == coluna):
                print(x)
            else:
                print(x, end=' ')

        print("")