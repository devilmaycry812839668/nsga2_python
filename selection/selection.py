#!/usr/bin/env python
#encoding:UTF-8
import random
import numpy as np
"""
        二元锦标赛 方式选择
"""
def mycmp2(i, j, funScore):
    s1=0
    s2=0
    s=funScore.shape[1] 

    for k in xrange(s):
        if funScore[i][k]<funScore[j][k]:
            s1+=1
        elif funScore[i][k]>funScore[j][k]:
            s2+=1

    if s1==0 and s2!=0:
        return j
    elif s1!=0 and s2==0:
        return i
    else:
        temp=[i, j]
        random.shuffle(temp)
        return temp[0]
 

def selection(population, functionObject):
    ###为函数对象赋值新的种群个体
    functionObject.population=population

    #计算新种群目标函数数值，并建立矩阵 funScore
    funScore=np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
    funScore=np.transpose(funScore)
    
    N=population.shape[0]
    V=population.shape[1]

    indicate_0=range(N)
    indicate=[]

    for _ in xrange(N):
        a1, a2=random.sample(indicate_0, 2) 
        indicate.append( mycmp2(a1, a2, funScore) )
    
    population[:]=population[indicate]
    funScore[:]=funScore[indicate]


if __name__=="__main__":
    np.random.seed(0)
    random.seed(0)
    from function.funUserDefine import *
    population=np.random.rand(5, 2)
    functionObject=ZDT1(population)
    #print population
    #print functionObject
    selection(population, functionObject)
    #print population
    #print functionObject
 
