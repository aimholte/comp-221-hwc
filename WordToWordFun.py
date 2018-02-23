# A.J. Imholte
# COMP 221
# HWC

import itertools
import string
import queue
from itertools import chain


# Sequences found for 'BOAT' to 'SHIP':

# Depth first search sequence: 'BOAT', 'BOAS', 'BOYS', 'BOYO', 'BOZO', 'MOZO', 'MOZZ', 'MUZZ', 'TUZZ', 'TIZZ', 'JIZZ',
# 'JAZZ', 'JAZY', 'JAXY', 'WAXY', 'WAVY', 'WAVE', 'WAWE', 'WAWS', 'WAYS', 'WEYS', 'WETS', 'WETA', 'WENA', 'WENT', 'WEST',
#  'WOST', 'WORT', 'WORN', 'WOON', 'WOOS', 'WOPS', 'TOPS', 'TOPO', 'TORO', 'TORY', 'TOWY', 'TOWT', 'TOUT', 'TOUR', 'YOUR',
#  'YOUS', 'YOWS', 'YOWL', 'YAWL', 'YAWP', 'YAUP', 'YAUD', 'YARD', 'YARR', 'YAAR', 'YEAR', 'YEAS', 'YEPS', 'YUPS', 'YUKS',
#  'YUKY', 'PUKY', 'PUKU', 'PUPU', 'PUPA', 'PUNA', 'PUNT', 'PUTT', 'PUTZ', 'LUTZ', 'LUTE', 'LURE', 'LURS', 'LUVS', 'LAVS',
# 'LAVA', 'LANA', 'LANX', 'LYNX', 'LYNE', 'LYSE', 'LOSE', 'LOSS', 'LOTS', 'LOTO', 'LOGO', 'LOGY', 'POGY', 'POXY', 'PIXY',
#  'PITY', 'PITS', 'PISS', 'PISO', 'PESO', 'PEPO', 'REPO', 'REPP', 'REAP', 'REAN', 'REIN', 'REIS', 'REWS', 'TEWS', 'TENS',
# 'TENE', 'TETE', 'TETH', 'TECH', 'TICH', 'TICS', 'TILS', 'TILT', 'TIPT', 'TIPI', 'TITI', 'ZITI', 'ZITE', 'ZINE', 'ZINS',
#  'ZIPS', 'ZAPS', 'ZAGS', 'YAGS', 'YAGI', 'YOGI', 'YOGH', 'YODH', 'YODE', 'YORE', 'YORP', 'YOOP', 'YOOF', 'ROOF', 'ROOT',
# 'RONT', 'RONG', 'RUNG', 'RUNS', 'RUTS', 'RUTH', 'RUSH', 'RUST', 'RAST', 'RASP', 'RAMP', 'RAMS', 'RAHS', 'PAHS', 'PARS',
#  'PART', 'PACT', 'PACY', 'PALY', 'PALP', 'PULP', 'PULS', 'PUYS', 'PRYS', 'PROS', 'PROW', 'PLOW', 'PLOY', 'PLAY', 'PLAT',
# 'PYAT', 'PYAS', 'PYES', 'PEES', 'PEER', 'PUER', 'PURR', 'PURL', 'PIRL', 'PIRN', 'PION', 'PHON', 'PHOT', 'PHUT', 'SHUT',
#  'SHUN', 'SHIN', 'SHIP']


# Breadth first search sequence: ['BOAT', 'BHAT', 'SHAT', 'SHIT', 'SHIP']
# Further sequences for other words can be seen by running this Python file.
# Analysis and selection of best algorithm can be found in the report for this homework.


'''
A simple function used to make a list of words from all the words in a given text file.
'''
def makeWordList(file):
    wordFile = open(file, 'r')
    solutionList = []
    for line in wordFile:
        word = line[:-1]
        solutionList.append(word)
    return solutionList

wordList = makeWordList('fourletterwords.txt')


'''
A function that builds a graph based off what "bucket" each word fits into.
'''
def makeGraph(file):
    graph = {}
    dict = {}
    textFile = open(file, 'r')
    for line in textFile: # For each line in the file
        word = line[:-1]
        for i in range(len(word)): # Iterate over the length of the string
            bucket = word[:i] + '_' + word[i+1:]  # Creates a "bucket" for every substring of the word where one letter is removed
            if bucket in dict:
                dict[bucket].append(word) # If this bucket is already in the dictionary, we simply append the word to its proper key
            else:
                dict[bucket] = [word] # Otherwise we add the new bucket and the word to the dictionary
    return dict

wordgraph = makeGraph('fourletterwords.txt')

'''
A function to find if there are in duplicate elements in a list.
'''
def findDuplicates(list):
    solution = []
    for element in list:
        if element not in solution:
            solution.append(element)
    return solution

'''
Given a word and a dictionary found from the makeGraph function, returns all the neighbors of the given word.
'''
def findNeighbors(word, dictionary):
    ansList = []
    for i in range(len(word)):
        wordSplice = word[:i] + '_' + word[i+1:] # All the "buckets" the input word belongs to
        ansList.append(dictionary.get(wordSplice)) # Appends all the values from these "buckets" to the list
    ansList = list(chain.from_iterable(ansList))
    solution = findDuplicates(ansList) # Checks for and removes any duplicates if found
    del(solution[solution.index(word)]) # Makes sure that the original word is not in its list of neighbors
    return solution

'''
Creates a more readable and understandable graph based off the data that we have from the first makeGraph function. This
returns a graph where the keys are no longer buckets but words, and their respective values are lists of words that
differ by one letter.
'''
def makeABetterGraph(wordList, graph = wordgraph):
    theRealGraph = {}
    for word in wordList: # For each word in the list of words from the file
        neighbors = findNeighbors(word, graph) # Find all the neighbors of the word based off the graph made before
        theRealGraph[word] = neighbors # Add the word and its neighbors to the graph
    return theRealGraph

theBestGraphEver = makeABetterGraph(wordList) # The graph that we will actually use to do the search for paths to words

'''
Given the improved graph from the makeABetterGraph function, a starting word, and an ending word, this function finds
a path from the starting word to the ending word based off the depth first search algorithm.
'''
def findPath(startingWord, endingWord, graphDictionary = theBestGraphEver):
    stack = [] # A stack to hold the nodes that still need to be visited
    visited = {} # A dictionary that tells us if a node has been visited
    parentDict = {} # A dictionary that holds the child to parent relationships for words in the graph
    # parentDict[startingWord] = 'This is the start! Yay!'
    ansStack = []
    visited[startingWord] = False
    stack.append(startingWord) # Push the starting word to the stack
    # for vertex in graphDictionary.keys():
    #     visited[vertex] = False
    #     stack.append(vertex)
    while len(stack) > 0: # While there are elements in the stack
        word = stack.pop() # Pop the first element from the stack
        if(visited[word] == False): # If this element has not been visited
            visited[word] = True # Set its visited value to True
            for neighbor in graphDictionary.get(word): # For each one of this words' neighbors
                if neighbor not in visited:
                    stack.append(neighbor) # Push the neighbor to the stack
                    parentDict[neighbor] = word # Add the child-parent pair to the parent dictionary
                    visited[neighbor] = False
                if neighbor == endingWord: # If we find the ending word
                    current = endingWord # Set the current word to the ending word to start
                    while current != None:
                        ansStack.append(current) # Append the current word to our answer
                        #print(ansStack)
                        current = parentDict[current] # Assign current to the current word's parent
                        if current == startingWord:
                            ansStack.append(startingWord)
                            #print(ansStack)
                            current = None # Set current to none once the starting word is found
                            ansStack.reverse() # Reverse the order of the stack to find the actual path the algorithm takes
                            return ansStack

# Testing print statments to make sure the program is working

# print(wordgraph)
# print(wordgraph)
# print(findNeighbors('BOAT', wordgraph))
# print(wordgraph)
# print(wordList)
# print(wordgraph.get('_AHS'))
# print(theBestGraphEver)

# Depth First Search:
print('Finding the path using the depth first search algorithm...')

print('Start: COAT, End: SHIP' + '\n Path: ' + str(findPath("BOAT", "SHIP")) + '\n')
print('Start: COAT, End: SLOW' + '\n Path: ' + str(findPath("COAT", "SLOW")) + '\n')
print('Start: SAIL, End: BALL' + '\n Path: ' + str(findPath('SAIL', 'BALL')) + '\n')
print('Start: AFAR, End: MALL' + '\n Path: ' + str(findPath('AFAR', 'MALL')) + '\n')
print('Start: ALAS, End: POST' + '\n Path: ' + str(findPath('ALAS', 'POST')) + '\n')
print('Start: RAFT, End: PYRO' + '\n Path: ' + str(findPath('RAFT', 'PYRO')) + '\n')
print('Start: ZOOM, End: TILT' + '\n Path: ' + str(findPath('ZOOM', 'TILT')) + '\n')
print('Start: FARM, End: YOLK' + '\n Path: ' + str(findPath('FARM', 'YOLK')) + '\n')
print('Start: YETI, End: SNOW' + '\n Path: ' + str(findPath('YETI', 'SNOW')) + '\n')

print('\n')

'''
Finds the path from the starting word to the ending word based off the graph yielded from the makeABetterGraph function.
This function uses breadth first search to find the path.
'''
def wordToWordbfs(start, end, graphToUse = theBestGraphEver):
        Q = queue.Queue() # A queue to hold the nodes that we still have to visit
        visited = [] # A list to hold the nodes that we have visited
        ans = []
        parentDict = {} # A dictionary holding the child-parent relationship for any given node
        Q.put(start) # Enqueue the starting wording
        visited.append(start) # Mark it as visited
        while(Q.empty() == False): # While the queue is not empty
            vertex = Q.get() # Dequeue from the queue
            for child in graphToUse.get(vertex): # For each child from the vertex
                if child not in visited: # If the child has not been visited
                    Q.put(child) # Enqueue the child
                    visited.append(child) # Mark the child as visited
                    parentDict[child] = vertex # Add the child parent relationship to the dictionary
                if child == end: # If we find the ending word
                    current = end # Set the current word to the ending word
                    while current != None:
                        ans.append(current) # Append the current word to the answer path
                        current = parentDict[current] # Set current to the current word's parent
                        if current == start: # If we find the starting word
                            ans.append(start) # Add it to the answer
                            current = None # Stop our search
                            ans.reverse() # Reverse the list to show the path
                            return ans


# Breadth First Search:
print('Finding the path using the breadth first search algorithm...')

print('Start: COAT, End: SHIP' + '\n Path: ' + str(wordToWordbfs("BOAT", "SHIP")) + '\n')
print('Start: COAT, End: SLOW' + '\n Path: ' + str(wordToWordbfs("COAT", "SLOW")) + '\n')
print('Start: SAIL, End: BALL' + '\n Path: ' + str(wordToWordbfs('SAIL', 'BALL')) + '\n')
print('Start: AFAR, End: MALL' + '\n Path: ' + str(wordToWordbfs('AFAR', 'MALL')) + '\n')
print('Start: ALAS, End: POST' + '\n Path: ' + str(wordToWordbfs('ALAS', 'POST')) + '\n')
print('Start: RAFT, End: PYRO' + '\n Path: ' + str(wordToWordbfs('RAFT', 'PYRO')) + '\n')
print('Start: ZOOM, End: TILT' + '\n Path: ' + str(wordToWordbfs('ZOOM', 'TILT')) + '\n')
print('Start: FARM, End: YOLK' + '\n Path: ' + str(wordToWordbfs('FARM', 'YOLK')) + '\n')
print('Start: YETI, End: SNOW' + '\n Path: ' + str(wordToWordbfs('YETI', 'SNOW')) + '\n')