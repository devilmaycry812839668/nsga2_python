#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from function.funUserDefine import *
from selection.selection import selection
from crossover.crossover import crossover
from mutation.mutation import mutation
from dominanceMain.dominanceMain import dominanceMain
from dominanceMain.estimate import estimate

#200个个体, 30个变量， 变量数值范围0到2**14
#交叉概率0.6， 编译概率0.1
xN=500
yN=30
alfa=0.8
belta=1.0/30

random.seed(0)
np.random.seed(0)

#测试population
population=np.random.rand(xN, yN)
functionObject=ZDT1(population)

for i in xrange(500):
    f_population=population.copy()
    selection(population, functionObject)
    crossover(population, alfa)
    mutation(population,  belta)
    c_population=population
    temp_population=np.vstack((f_population, c_population))
    population=dominanceMain(temp_population, functionObject)

estimate(population, functionObject)
 

