import numpy as np
import math

global funclist

def linear(x, y):
    return np.array([x,y])

def reverse(y, x):
    return np.array([y,x])

def sinusoidal(x, y):
    return np.array([math.sin(x),math.sin(y)])
    
def cosine(x, y):
    return np.array([math.cos(x), math.cos(y)])

def spherical(x, y):
    sph = 1/(x*x + y*y)
    return np.array([x*sph, y*sph])
    
def swirl(x, y):
    rs = x*x+y*y 
    srs = math.sin(rs)
    crs = math.cos(rs)
    return np.array([x*srs-y*crs, x*crs+y*srs])
    
def horseshoe(x, y):
    hrs = 1/math.sqrt(x*x+y*y)
    return np.array([hrs*(x-y)*(x+y), 2*x*y])
    
def squpowsph(x, y):
    rs = x*x+y*y
    return np.array([x*x/rs, y*y/rs])
    
def squrootsph(x, y):
    rs = x*x+y*y 
    return np.array([math.sqrt(x)/rs,math.sqrt(y)/rs])
    
def squsph(x, y):
    r = math.sqrt(x*x+y*y)
    return np.array([math.sqrt(x)/r,math.sqrt(y)/r])

def hyperbolicsine(x, y):
    return np.array([math.asinh(x),math.asinh(y)])

def Var1(x, y):
    theta = np.arctan(x/y)
    r = math.sqrt(x*x+y*y)
    ven = math.pow(r, math.sin(theta))
    arr = [ven*math.cos(x), ven*math.sin(y)]
    return np.array(arr)

def Var2(x, y):
    theta = np.arctan(x/y)
    r = math.sqrt(x*x+y*y)
    ven = math.pow(r, math.cos(theta))
    arr = [ven*math.sin(x), ven*math.cos(y)]
    return np.array(arr)

def Var3(x, y):
    p1 = .2
    p2 = 4
    t1 = 1 + p1*x + p2*(x*x - y*y)
    t2 = p1*y + 2*p2*x*y
    ren = 1/(t1*t1+t2*t2)
    return np.array([ren*(x*t1+y*t2),ren*(y*t1-x*t2)])

def Var4(x, y):
    r1 = .4
    r2 = .4
    return np.array([(2*math.floor(x/r1)+1)*r1-x,(2*math.floor(y/r2)+1)*r2-y])

def Var5(x, y):
    r = math.sqrt(x*x+y*y)
    con = 2/(r+1)
    return np.array([con*x,con*y])

def Var6(x, y):
    theta = math.tan(x/y)
    r = math.sqrt(x*x+y*y)
    p0 = math.sin(theta+r)
    p1 = math.cos(theta-r)
    p0c = p0*p0*p0 
    p1c = p1*p1*p1 
    return np.array([r*(p0c+p1c),r*(p0c-p1c)])

#funclist = [linear, reverse, sinusoidal, spherical, swirl, horseshoe, squpowsph, squrootsph, squsph, hyperbolicsine]
funclist = [Var6, Var5]

def calc(var, input):
    function = funclist[var]
    x = input[0]
    y = input[1]
    output = function(x, y)
    return output
    
def getVarNum():
    return len(funclist)

    


