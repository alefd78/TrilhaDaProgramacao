# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:53:40 2023

@author: Ale F. D.
"""


def sao_multiplicaveis(m1, m2):
    lmat1 = len(m1)
    cmat1 = len(m1[0])
    lmat2 = len(m2)
    cmat2 = len(m2[0])

    if (cmat1 == lmat2):
        return (True)
    else:
        return (False)