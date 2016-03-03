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
        """
        Deletes a node from the graph and all edges where it appears
        :param node: The node to remove 
        """
        self.__nodes.remove(node)
        del(node)    
    
    
    def get_nodes(self, node_info):
        """
        Finds all the nodes with the given info in the graph.
        :param node_info: The info of the node..
        :returns: A list containing all the nodes with the given info 
        """
        
        return [x for prospect_node in self.__nodes if prospect_node.info == node_info]
    
    
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
            self.__in_edges = set()
            self.__out_edges = set()
            self.parent = None
            self.color = 'white'
            self.cost = 0
        
        
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
                starting_node.__out_edges.add(ending_node, cost)
                ending_node.__in_edges.add(starting_node, cost)
            
            
            __set_neighbor_relationship(self, neighbor, edge_cost)
            
            if not directed: __set_neighbor_relationship(neighbor, self, edge_cost)
        
        
        @property
        def neighbors(self, ):
            return deepcopy(self.__out_edges)
        
        
        def __del__(self, ):
            
            
            def __remove_edge(edges, edge):
                edges -= edge
            
            
            for edge in self.__in_edges.union(self.__out_edges):
                secondary_node = in_edge[0]
                cost = edge[1]
                edge_to_remove = {(self, cost)}
                __remove_edge(secondary_node.__out_edges, edge_to_remove)
                __remove_edge(secondary_node.__in_edges, edge_to_remove)
        
        
        def __eq__(self, other):
            """
            A node will be equals to another if their info have the same values,
            also if the edges that end in the self node are equal to the ones
            that end in the other node
            """
            
            def __get_all_edges(node):
                return node.__in_edges.union(node.__out_edges)
            
            
            return self.info == other.info \
                    and __get_all_edges(self) == __get_all_edges(other)