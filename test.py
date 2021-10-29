#son las 10
def MexHat(sigma, K):
    M =  numpy.zeros((K,K));
    for x in range(0,5):
        for y in range(0,K):
            M[x,y] = 1/(pi*sigma**2) * ( 1-1-2*(x**2+y**2)/sigma**2) * numpy.exp(- (x**2+y**2)/(2*sigma**2))

MexHat(sigma = 1, K = 5)

print(M)
