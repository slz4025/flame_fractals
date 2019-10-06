#have four initial points 
#take their average in the x and y dimension 
#add a random factor 
#import cv2
import numpy as np
import math
import random
import time

from Funcs import Func

global funcnums
global iterationsnum
global gamma
global size, n
global accumulator


def iterate():
    global accumulator
    Xlist = []
    Ylist = []
    collist = []
    
    P = choosePoint()#initial
    funcmaster = Func(funcnums)#generates funcnums lists 
    funcprob = funcmaster.problist
    #give prob to each func
    for counter in range(iterationsnum):
        #print(P)
        deter = random.random()
        ind = -1
        for i in range(funcnums):
            if deter < funcprob[i]:
                ind = i 
                break
        
        ind = int(random.random()*funcnums)
        Pu, use, C = funcmaster.run(ind, P)#update point to return np-style, can make color separate
        P = np.array([Pu[0],Pu[1],1])#next point
        (b, g, r) = C
        if counter >= 20:#plot point
            Xlist.append(use[0])
            Ylist.append(use[1])
            collist.append(C)
    #end
    
    #take mean, std deviation of X and Y
    meanX = np.mean(Xlist)
    stdX = np.std(Xlist)
    meanY = np.mean(Ylist)
    stdY = np.std(Ylist)
    
    maxX = meanX + 2.4*stdX#max(Xlist)
    minX = meanX - 2.4*stdX#min(Xlist)
    maxY = meanY + 1.5*stdY#max(Ylist)
    minY = meanY - 1.5*stdY#min(Ylist)
    
    scalex = (size-1)/(maxX-minX)
    scaley = (size-1)/(maxY-minY)
    
    #do afterwards
    for counter2 in range(iterationsnum-20):

        #location
        X = (Xlist[counter2]-minX)*scalex
        Y = (Ylist[counter2]-minY)*scaley
        if X >= size or X < 0 or Y >= size or Y < 0:
            continue
        (b,g,r) = collist[counter2]
        #color
        accumulator[X][Y][0] = (accumulator[X][Y][0] + b)/2.0
        accumulator[X][Y][1] = (accumulator[X][Y][1] + g)/2.0
        accumulator[X][Y][2] = (accumulator[X][Y][2] + r)/2.0
        accumulator[X][Y][3] += 1.0#alpha is the actual accumulator space
    accumulator = funcmaster.finalfunc(accumulator, size)#no change now
    
def choosePoint():
    x = (random.random()-.5)*2
    y = (random.random()-.5)*2
    return np.array([x,y,1])#2D vector

def createImage(image):
    v1 = 1/gamma
    processor = np.zeros((size,size,3))
    
    #fill processor for corrected
    for i in range(size):
        for j in range(size):
            P = accumulator[i][j]
            alpha = P[3]
            if alpha <= 1:#to avoid neg errors or large final alpha
                alpha_gammacorr = 1
                alpha_logcorr = 1
            else:
                alpha_gammacorr = math.pow(alpha, (v1))
                alpha_logcorr = math.log(alpha_gammacorr)/alpha_gammacorr
            
            #final alpha is between [0, 1] 
            #colors between [0, 1]
            red_corr = P[0]*alpha_logcorr 
            green_corr = P[1]*alpha_logcorr  
            blue_corr = P[2]*alpha_logcorr
            processor[i][j] = [red_corr,green_corr,blue_corr]
    #processor done
    
    #make brightest 1
    maxcol = np.max(processor)
    mulfac = 1.0/maxcol
    matfac = np.empty((size,size,3))
    matfac.fill(mulfac)
    processor = np.multiply(processor, matfac)
    
    
    #supersampling
    i = 0
    sqr = float(n*n)
    picsize = size/n
    while i < picsize:
        I = i*n
        j = 0
        while j < picsize:
            J = j*n
            
            k = 0
            sumr = 0.0
            sumg = 0.0
            sumb = 0.0
            
            while k < n:
                h = 0
                ind1 = I+k
                while h < n:
                    ind2 = J+h
                    sumr += processor[ind1][ind2][0]
                    sumg += processor[ind1][ind2][1]
                    sumb += processor[ind1][ind2][2]
                    h += 1
                k += 1
            image[i][j][0] = int(sumr/sqr*255)
            image[i][j][1] = int(sumg/sqr*255)
            image[i][j][2] = int(sumb/sqr*255)
            #print(image[x][y])
            j += 1
        i += 1
        
    image = image.astype(np.uint8)#normal image
    
    #POST-PROCESS
    #image = cv2.bitwise_not(image)
    
    return image
        
def initialize():
    global funcnums
    global iterationsnum
    global gamma
    global size, n
    global accumulator
    
    funcnums = 10
    iterationsnum = 10000
    gamma = 2.2 
    
    size = 300
    n = 10
    
    accumulator = np.zeros((size,size,4))#4 for colors
    
#one function, one variation
#one function, two variations
#two functions, one variation
def main():
    START = time.time()
    initialize()
    iterate()
    #accumulator should be full
    
    picsize = int(size/n)
    image = np.zeros((picsize,picsize,3))
    image2 = createImage(image)
    #cv2.imwrite("ss1.png", image2)
    print(time.time()-START)
    
    #cv2.imshow("Fractal Flame", image2)
    #k = cv2.waitKey()
    
if __name__ == "__main__":
    main()
