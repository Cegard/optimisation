# -*- coding: utf-8 -*-
from copy import deepcopy


class Graph(object):
    
    
    def __init__(self, ):
        """
        Creates a new empty graph
        (a graph is a list of nodes that might have edges between them)
        """
        self.__nodes = []
    
    
    def add_node(self, content):
        """
        Creates a new node with the given content and adds it
        to the graph.
        :param content: the info to be stroed within the node
        """
        self.__nodes.append(self.__Node(content))
    
    
    def remove_node(self, node):
        
        
        def __remove(node, edges):
            for edge in edges:
                ending = edge[0]
                cost = edge[1]
                ending.in_edges -= set((node, cost))
                ending.neighbors -= set((node, cost))

        
        __remove(node, node.in_edges)
        __remove(node, node.neighbors)
    
    
    def get_nodes(self, node_info):
        """
        Finds all the nodes with the given info in the graph.
        :param node_info: The info of the node..
        :returns: A list containing all the nodes with the given info 
        """
        
        return [x for node in self.__nodes if node.info == node_info]
    
    
    @property
    def nodes(self, ):
        return deepcopy(self.__nodes)
    

    class __Node:
        
        
        def __init__(self, info):
            """
            Creates a new isolated node with a white color.
            :param info: the value to be stored within  the node
            """
            self.info = info
            self.neighbors = set()
            self.parent = None
            self.color = 'white'
            self.cost = 0
            self.in_edges = set()
        
        
        def add_neighbor(self, neighbor, edge_cost = 0, directed = False):
            """
            Adds a node as a neighbor by creating an edge between
            the self node and the neighbor node; an edge is a
            tuple of the form (neighbor, cost)
            :param neighbor: A node object to be added.
            :param edge_cost: The cost of the edge to be created.
            :param directed: If directed it'll create only an edge coming from
                the self node to the neighbor.
            """
            
            def __set_neighbor_relationship(starting_node, ending_node, cost):
                ending_node.in_edges.add((starting_node, cost))
                starting_node.neighbors.add(ending_node, cost)
            
            
            __set_neighbor_relationship(self, neighbor, edge_cost)
            
            if not directed: __set_neighbor_relationship(neighbor, self, edge_cost)
        
        
        def __eq__(self, other):
            """
            A node will be equals to another if their info have the same values,
            also if the edges that end in the self node are equal to the ones
            that end in the other node
            """
            return self.info == other.info \
                    and set(self.in_edges) == set(other.in_edges)