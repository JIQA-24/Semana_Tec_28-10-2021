import numpy

"""
filtros.py
Aqui van los kernel con los que hacermos los filtros
"""

#chikri

def sobelh():

    k = numpy.array([[-1,-2,-1],[0,0,0],[1,2,1]])

    '''
    -1 -2 -1
    0 0 0 
    1 2 1
    '''
    return k


def sobelv():

    k = numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])

    '''
    -1 0 1
    -2 0 2
    -1 0 1
    '''
    return k

#Brunichan

def emboss():
    k = numpy.array([[-2,-1,0],[-1,1,1],[0,1,2]])

    '''
    -2 -1 0
    -1 1 1
     0 1 2
    '''
    return k

def sharpen():
    k = numpy.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

    '''
     0 -1  0
    -1  5 -1
     0 -1  0
    '''
    return k

def passf():
    k = numpy.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

    '''
     0 -1  0
    -1  4 -1
     0 -1  0
    '''
    return k
