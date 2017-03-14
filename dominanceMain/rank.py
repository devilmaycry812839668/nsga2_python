#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
import copy
"""
    输入：支配关系字典 r_dict
    {个体号码：[支配其的个数， 被其支配的个体列表]}

    输出:分层字典 layerDict
    {1:[3,1,4], 2:[2,0]}
"""
def rank(r_dict):
    #拷贝 支配关系字典
    r_dict=copy.deepcopy(r_dict)

    #支配集分层, 层号初始化
    i=1

    #分层字典 layerDict
    layerDict={}

    while r_dict!={}:
        #取出当前种群非支配个体，放入第i层
        layerDict[i]=[]

        #找出当前非支配个体
        for k, v in r_dict.items():
            if v[0]==0:
                layerDict[i].append(k)

        ###将被 第i层支配的个体 支配数减1
        for k in layerDict[i]:
            #val[0] 支配 k 的个体数 
            #val[1] 个体 k 支配的个体列表
            val=r_dict.pop(k)
            for v in val[1]:
                r_dict[v][0]-=1

        i=i+1

    return layerDict


if __name__=="__main__":
    r_dict={0: [7, []], 1: [3, [0, 2, 5]], 2: [6, [0, 5]], 3: [3, [0, 2, 5, 6]], 4: [0, [0, 1, 2, 3, 5, 6, 7, 8]], 5: [8, []], 6: [5, [5]], 7: [3, [0, 2, 5, 6]], 8: [2, [0, 1, 2, 3, 5, 6, 7]], 9: [0, [0, 1, 2, 3, 5, 6, 7, 8]]}
    print rank(r_dict)


