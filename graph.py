#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Graph(object):
    
    
    def __init__(self, ):
        """
        Creates a new empty graph
        """
        self.nodes = []
        self.edges = []
    
    
    def add_node(self, content):
        """
        Creates a new node with the given content and adds it
        to the graph.
        :param content: the info to be stroed within the node
        """
        self.nodes.append(self.__Node(content))
    
    
    def add_edge(self, node1, node2, cost = 0, directed = False):
        """
        Creates an edge between two nodes (not necesarilly different)
        :param node1: the node object contenting
        :param node2: the node object to be added
        :param cost: integer, the cost of the edge, 0 by default
        :param directed: boolean saying if the edge has a direction
        """
        self.edges.append[self.__Edge(node1, node2, cost, directed)]
    

    class __Node:
        
        
        def __init__(self, info):
            """
            Creates a new isolated node with a white color.
            :param info: the value to be stored within  the node
            """
            self.info = info
            self.neighbors = []
            self.parent = None
            self.color = 'white'
            self.cost = 0
        
        
        def add_neighbor(self, neighbor):
            """
            adds a child to the node
            :param neighbor: a Node object to be added
            """
            if neighbor not in self.neighbors: self.neighbors.append(neighbor)
        
        
        def set_parent(self, parent):
            """
            sets the parent of the self node
            :param parent: the parent node object
            """
            
            self.parent = parent
    
    
    class __Edge(object):
        
        
        def __init__(self, node1, node2, cost = 0, directed = False):
            """
            Creates an edge between two nodes (not necesarilly different)
            :param node1: the node object contenting
            :param node2: the node object to be added
            :param cost: integer, the cost of the edge, 0 by default
            :param directed: boolean saying if the edge has a direction
            """
            self.node1 = node1
            self.node2 = node2
            self.cost = cost
            self.node1.add_neighbor(node2)
            
            if not directed:
                self.node2.add_neighbor(node1)