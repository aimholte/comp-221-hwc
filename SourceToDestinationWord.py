# A.J. Imholte
# Algorithm Design and Analysis
# HWC

from adjGraph import Graph
import itertools

# Build the graph

def makeGraph(file):
    dict = {}
    graph = {}
    textFile = open(file, 'r')
    for line in textFile: # iterates over every word in the file
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]  # Creates a "bucket" for every substring of the word where one letter is removed
            if bucket in dict:
                dict[bucket].append(word) # If this bucket is already in the dictionary, we simply append the word to its proper key
            else:
                dict[bucket] = [word] # Otherwise we add the new bucket and the word to the dictionary

    # for bucket in dict.keys():
    #     for firstWord in dict[bucket]:
    #         for secondWord in dict[bucket]:
    #             if firstWord != secondWord:
    #                 # if both words aren't in the graph
    #                     #  Add both words to the graph as keys
    #                     #  Add both wrods to each others' list of values
    #                 # if both words are in the graph
    #                     # Add boths w=to each others' list of values
    #                 # If the first word is in the graph but the second word is not
    #                     # Add the second word to graph as a key
    #                     # Add the first word as a value to the second words' list of values
    #             pass
    #         pass
    #     pass
    # pass

                    # Creates edges of the graph

    return graph

wordgraph = makeGraph('fourletterwords.txt')


# Now we have a way to build the graph given the text file...let's see if we can make an algorithm that can solve this problem!

# First attempting with the traveling salesman framework...

def sourceToDestination(graph ,sourceWord, destinationWord):
    startingIndex = graph.getVertex(sourceWord)
    endingIndex = graph.getVertex(destinationWord)
    for i in itertools.permutations(startingIndex, endingIndex):
        print(i)

print(sourceToDestination(wordgraph, 'COAT', 'SHIP'))