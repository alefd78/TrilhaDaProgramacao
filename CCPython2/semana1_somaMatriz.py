# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 21:14:52 2023

@author: Alessandro F. D.
"""


def soma_matrizes(mat1, mat2):
    lmat1 = len(mat1)
    cmat1 = len(mat1[0])
    lmat2 = len(mat2)
    cmat2 = len(mat2[0])
    matResultado = mat1[:]

    if (lmat1 != lmat2 or cmat1 != cmat2):
        return (False)

    for l in range(lmat1):
        for c in range(cmat1):
            # print(mat1[l][c], end = '\t')
            matResultado[l][c] = mat1[l][c] + mat2[l][c]

    return (matResultado)