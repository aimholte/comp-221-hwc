# A.J. Imholte
# COMP 221
# HWC

import itertools
import string
import queue
from itertools import chain

# 1. Build the graph based off a text of words

def makeWordList(file):
    wordFile = open(file, 'r')
    solutionList = []
    for line in wordFile:
        word = line[:-1]
        solutionList.append(word)
    return solutionList

def makeGraph(file):
    graph = {}
    dict = {}
    textFile = open(file, 'r')
    for line in textFile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]  # Creates a "bucket" for every substring of the word where one letter is removed
            if bucket in dict:
                dict[bucket].append(word) # If this bucket is already in the dictionary, we simply append the word to its proper key
            else:
                dict[bucket] = [word] # Otherwise we add the new bucket and the word to the dictionary
    return dict

def findNeighbors(word, dictionary):
    ansList = []
    finalList = []
    c = []
    for i in range(len(word)):
        wordSplice = word[:i] + '_' + word[i+1:]
        ansList.append(dictionary.get(wordSplice))
    ansList = list(chain.from_iterable(ansList))
    solution = findDuplicates(ansList)
    del(solution[solution.index(word)])
    return solution

def makeNeighborQueue(neighbors):
    neighborQueue = queue.Queue()
    for neighbor in neighbors:
        neighborQueue.put(neighbor)
    return neighborQueue

def findDuplicates(list):
    solution = []
    for element in list:
        if element not in solution:
            solution.append(element)
    return solution







wordgraph = makeGraph('fourletterwords.txt')
# print(wordgraph)
#print(wordgraph)
# print(findNeighbors('BOAT', wordgraph))
#print(wordgraph)
wordList = makeWordList('fourletterwords.txt')
# print(wordList)
#print(wordgraph.get('_AHS'))


def makeABetterGraph(wordList, graph = wordgraph):
    theRealGraph = {}
    for word in wordList:
        neighbors = findNeighbors(word, graph)
        theRealGraph[word] = neighbors
    return theRealGraph

theBestGraphEver = makeABetterGraph(wordList)
# print(theBestGraphEver)

def findPath(startingWord, endingWord, graphDictionary = theBestGraphEver):
    stack = []
    visited = {}
    parentDict = {}
    parentDict[startingWord] = 'This is the start! Yay!'
    ansStack = []
    visited[startingWord] = False
    stack.append(startingWord)
    # for vertex in graphDictionary.keys():
    #     visited[vertex] = False
    #     stack.append(vertex)
    while len(stack) > 0:
        word = stack.pop()
        if(visited[word] == False):
            visited[word] = True
            for neighbor in graphDictionary.get(word):
                if neighbor not in visited:
                    stack.append(neighbor)
                    parentDict[neighbor] = word
                    visited[neighbor] = False
                if neighbor == endingWord:
                    current = endingWord
                    while current != None:
                        ansStack.append(current)
                        #print(ansStack)
                        current = parentDict[current]
                        if current == startingWord:
                            ansStack.append(startingWord)
                            #print(ansStack)
                            current = None
    ansStack.reverse()
    return ansStack

print(findPath("COAT", "SHIP"))

