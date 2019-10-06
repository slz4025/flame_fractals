import random 
import math
import numpy as np

import Variations
global varinum, varinumm1
varinum = Variations.getVarNum()

class Func:
    #self.funcnum
    #self.funclist
    #self.colorlist
    #self.weightlist
    #self.problisttemp
    #self.problist
    def __init__(self, num):
        self.funcnum = num
        self.funclist = []
        self.colorlist = []
        self.weightlist = []
        self.problisttemp = []
        self.problist = []
        
        sumprob = 1.0
        for i in range(self.funcnum):
            curr = np.zeros((2,3))#2x3
            
            #may have to put a factor to prevent it from going out of [0,1]
            for j in range(2):
                for k in range(3):
                    curr[j][k] = (random.random()-.5)*2
            self.funclist.append(curr)
            
            color = np.zeros((3))#dim 3
            #change col basis from r,g,b to m,y,c or another lin ind system?
            #col = random.random    random
            #col = math.sqrt(random.random())    lean towards col channel
            #col = mean + 2*(random.random() - 0.5)*std    linear around middle
            
            for j in range(3):
                color[2] = math.sqrt(random.random())#max(0.0,min(1.0,random.gauss(.9, .05)))
                color[1] = math.sqrt(random.random())#math.sqrt(random.random())#max(0.0,min(1.0,random.gauss(.1, .1)))
                color[0] = math.sqrt(math.sqrt(random.random()))#1-math.sqrt(random.random())#max(0.0,min(1.0,random.gauss(0, .05)))
                #color[j] = random.random()
                    
            self.colorlist.append(color)
            
            weights = np.zeros((varinum))
            sumwe = 0.0#add up to one
            for j in range(varinum):
                w = random.random()
                sumwe += w
                weights[j] = w#easier later on
            for j in range(len(weights)):#add to zero
                weights[j] /= sumwe
            self.weightlist.append(weights)
            
            self.problisttemp.append(random.random())#random acceptance
            sumprob += self.problisttemp[i]
        for j in range(len(self.problisttemp)):
            self.problisttemp[j] /= sumprob 
        self.problist = []
        cumsum = 0.0
        for j in range(len(self.problisttemp)):
            cumsum += self.problisttemp[j]
            self.problist.append(cumsum)
        self.problist[-1] = 1.0#last element is one
        '''
        self.funclist[0] = np.zeros((2,3))
        self.funclist[1] = np.zeros((2,3))
        self.funclist[2] = np.zeros((2,3))
        self.funclist[3] = np.zeros((2,3))
        self.funclist[4] = np.zeros((2,3))
        self.funclist[5] = np.zeros((2,3))
        self.funclist[6] = np.zeros((2,3))
        self.funclist[7] = np.zeros((2,3))
        self.funclist[8] = np.zeros((2,3))
        self.funclist[9] = np.zeros((2,3))
        
        self.funclist[0][0][0] = -0.21599043
        self.funclist[0][0][1] = 0.39128832
        self.funclist[0][0][2] = 0.15390361
        self.funclist[0][1][0] = 0.53475811
        self.funclist[0][1][1] = 0.58686431
        self.funclist[0][1][2] = 0.47294074
        
        self.funclist[1][0][0] = 0.06504161
        self.funclist[1][0][1] = -0.05843842
        self.funclist[1][0][2] = -0.65391299
        self.funclist[1][1][0] = -0.73463109
        self.funclist[1][1][1] = -0.29495498
        self.funclist[1][1][2] = 0.53579856
        
        self.funclist[2][0][0] = 0.96398367
        self.funclist[2][0][1] = -0.21342449
        self.funclist[2][0][2] = 0.70316816
        self.funclist[2][1][0] = 0.16965996
        self.funclist[2][1][1] = -0.12645412
        self.funclist[2][1][2] = 0.2544815
        
        self.funclist[3][0][0] = -0.9419148
        self.funclist[3][0][1] = 0.33843361
        self.funclist[3][0][2] = 0.83168387
        self.funclist[3][1][0] = 0.50614666
        self.funclist[3][1][1] = 0.76196972
        self.funclist[3][1][2] = -0.91179269
        
        self.funclist[4][0][0] = -0.72600885
        self.funclist[4][0][1] = -0.30375827
        self.funclist[4][0][2] = 0.52840951
        self.funclist[4][1][0] = -0.36284105
        self.funclist[4][1][1] = 0.38865996
        self.funclist[4][1][2] = 0.94006902
        
        self.funclist[5][0][0] = -0.85643863
        self.funclist[5][0][1] = -0.85091814
        self.funclist[5][0][2] = -0.36932279
        self.funclist[5][1][0] = 0.73985352
        self.funclist[5][1][1] = -0.63626955
        self.funclist[5][1][2] = 0.25577402
        
        self.funclist[6][0][0] = -0.79986361
        self.funclist[6][0][1] = -0.45951446
        self.funclist[6][0][2] = 0.14988355
        self.funclist[6][1][0] = -0.52347797
        self.funclist[6][1][1] = -0.5566034
        self.funclist[6][1][2] = -0.1677346
        
        self.funclist[7][0][0] = 0.89417398
        self.funclist[7][0][1] = 0.93458184
        self.funclist[7][0][2] = 0.83966558
        self.funclist[7][1][0] = 0.169425
        self.funclist[7][1][1] = -0.76984709
        self.funclist[7][1][2] = -0.4929337
        
        self.funclist[8][0][0] = -0.66507092
        self.funclist[8][0][1] = 0.13150623
        self.funclist[8][0][2] = 0.12234821
        self.funclist[8][1][0] = -0.17868964
        self.funclist[8][1][1] = -0.99302379
        self.funclist[8][1][2] = 0.65299789
        
        self.funclist[9][0][0] = -0.00872277
        self.funclist[9][0][1] = 0.87967566
        self.funclist[9][0][2] = 0.0338448
        self.funclist[9][1][0] = 0.55334228
        self.funclist[9][1][1] = -0.71427207
        self.funclist[9][1][2] = 0.94529984
        
        self.colorlist[0] = np.zeros((3))
        self.colorlist[1] = np.zeros((3))
        self.colorlist[2] = np.zeros((3))
        self.colorlist[3] = np.zeros((3))
        self.colorlist[4] = np.zeros((3))
        self.colorlist[5] = np.zeros((3))
        self.colorlist[6] = np.zeros((3))
        self.colorlist[7] = np.zeros((3))
        self.colorlist[8] = np.zeros((3))
        self.colorlist[9] = np.zeros((3))
        
        self.colorlist[0][0] = 0.84707973  
        self.colorlist[0][1] = 0.96799506
        self.colorlist[0][2] = 0.062509
        
        self.colorlist[1][0] = 0.85652912
        self.colorlist[1][1] = 0.72733685
        self.colorlist[1][2] = 0.26960046
        
        self.colorlist[2][0] = 0.86772373
        self.colorlist[2][1] = 0.44776122
        self.colorlist[2][2] = 0.53691371
        
        self.colorlist[3][0] = 0.98652682
        self.colorlist[3][1] = 0.9046901
        self.colorlist[3][2] = 0.57733169
        
        self.colorlist[4][0] = 0.94697595
        self.colorlist[4][1] = 0.19770789
        self.colorlist[4][2] = 0.40405386
        
        self.colorlist[5][0] = 0.64275752
        self.colorlist[5][1] = 0.78837744
        self.colorlist[5][2] = 0.46017482
        
        self.colorlist[6][0] = 0.92035173
        self.colorlist[6][1] = 0.78724494
        self.colorlist[6][2] = 0.33762098
        
        self.colorlist[7][0] = 0.99776946
        self.colorlist[7][1] = 0.69813974
        self.colorlist[7][2] = 0.01745016
        
        self.colorlist[8][0] = 0.84710795
        self.colorlist[8][1] = 0.06794986
        self.colorlist[8][2] = 0.07769114
        
        self.colorlist[9][0] = 0.70873408
        self.colorlist[9][1] = 0.0792479
        self.colorlist[9][2] = 0.27506696
        '''
        print(self.funclist)
        print(self.colorlist)
        
        #done
    def run(self, ind, P):
        curr = self.funclist[ind]
        product = np.dot(curr, P)#like matrix multiplication
        weights = self.weightlist[ind]
        Melange = np.zeros((2))
        
        for v in range(varinum):
            V = Variations.calc(v, product)#v is index
            w = weights[v]
            N = np.array([V[0]*w, V[1]*w])
            Melange = np.add(Melange, N)
        
        color = self.colorlist[ind]
        return product, Melange, color
    
    def probability(self, ind):
        return self.problist[ind]
    
    def finalfunc(self, matrix, size):
        return matrix
    
    