import re
import os
from difflib import SequenceMatcher as SM
import itertools

def combine_lists(list1, list2):
    c = list(itertools.product(list1, list2))
    return c

def readfile(filename):
    data=[]
    with open(filename) as f:
        for line in f:
           line=line.strip("\n")
           data.append(line)
    return data

def anti_vowel(c):
    newstr = ""
    vowels = ('A', 'E', 'I', 'O', 'U')
    for x in c:
        if x not in vowels:
            newstr = newstr+x       
    return newstr


def create_dict(data,x=0, y=1):
    dataDict={}
    for item in data:
        vals=item.split("|")
        try:
            dataDict[vals[x]].add(vals[y])
        except:
            dataDict[vals[x]]=set([vals[y]])
    return dataDict


def best_match(list1, list2):
        cList=combine_lists(list1, list2)
        cScore=[]
        for item in cList:
            cScore.append(SM(None, item[0],item[1]).ratio())
        return cList[cScore.index(max(cScore))], max(cScore)