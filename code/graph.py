# Parker Michaelson
# A01248939
# parker.michaelson@gmail.com
# Assignment #3

# This file contains the TSPGraph class. TSPGraph is a class representing
# "static" information about the graph, information that does not change
# while a search is in progress. This includes a list of nodes and
# coordinates, an adjacency matrix for the nodes whose values are distances
# between adjacent nodes and a lookup table to correlate the number of a node
# in the source file with its internal representation. The class includes
# utility functions for constructing itself.



import math
import random
import re
from adjmatrix import AdjMatrix



class Graph:

    def __init__(self, graphfile="graph.txt"):
        self.nodelist = []
        self.namelookup = dict()
        self.idlookup = dict()
        self.adjmatrix = None
        self.load_graph(graphfile)
        self.print_stats()



    def load_graph(self, filename):
        with open(filename, 'r') as graphfile: 

            if graphfile == None:
                sys.exit("Graph File Non-Existent, ensure file exists.")

            nodecount = 0


            for line in graphfile:
                if line.strip()[0] == '#':
                    continue
                else:
                    matchobj = re.match(r"(?P<nodeone>\w+) (?P<nodetwo>\w+) (?P<adjval>\d+)", line)
                    if matchobj != None:
                        if matchobj.group('nodeone') not in self.idlookup:
                            self.namelookup[nodecount] = matchobj.group('nodeone')
                            self.idlookup[matchobj.group('nodeone')] = nodecount
                            self.nodelist.append([nodecount, matchobj.group('nodeone')])
                            nodecount += 1

                        if matchobj.group('nodetwo') not in self.idlookup:
                            self.namelookup[nodecount] = matchobj.group('nodetwo')
                            self.idlookup[matchobj.group('nodetwo')] = nodecount
                            self.nodelist.append([nodecount, matchobj.group('nodetwo')])
                            nodecount += 1


            self.adjmatrix = AdjMatrix(nodecount)

            graphfile.seek(0)
            for line in graphfile:
                if line.strip()[0] == '#':
                    continue
                else:
                    matchobj = re.match(r"(?P<nodeone>\w+) (?P<nodetwo>\w+) (?P<adjval>\d+)", line)
                    if matchobj != None:
                        self.adjmatrix.set_adjvalue(self.idlookup[matchobj.group('nodeone')], self.idlookup[matchobj.group('nodetwo')], float(matchobj.group('adjval')))



    def print_stats(self):
        print ""
        print self.nodelist
        print self.namelookup
        print self.idlookup
        self.adjmatrix.print_adjmatrix
        print ""
