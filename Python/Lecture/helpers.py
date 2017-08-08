'''
this module contains only a few simple functions in order to demonstrate how self-defined functions can be imported
'''
import math

def cumsum(numList):
        ''' Function calculates the sum over all elements in numList'''
        sum=0
        for i in numList:
                sum+=i
        return sum #return euclidean distance

def eukliddist2(pointA=[0,0,0],pointB=[0,0,0]):
        ''' 
        Function calculates the euclidean distance between a pair of points
        If only for one point coordinates are assigned at function-call, 
        then the function returns the magnitude of this point.
        '''
        mindim=min(len(pointA),len(pointB)) #determine minimum dimension of points
        sum=0
        for i in range(mindim):
                sum+=math.pow(pointA[i]-pointB[i],2)
        return math.sqrt(sum) #return euclidean distance