# -*- coding: utf-8 -*-
from copy import deepcopy


class Graph(object):
    
    
    def __init__(self, ):
        """
        Creates a new empty graph
        (a graph is a list of nodes that might have edges between them)
        """
        self.__nodes = []
    
    
    def add_isolated_node(self, content):
        """
        Creates a new node with the given content and adds it
        to the graph.
        :param content: the info to be stroed within the node
        """
        node = __Node(content)
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
        
        return set([x for prospect_node in self.__nodes if prospect_node.info == node_info])
    
    
    @property
    def nodes(self, ):
        return deepcopy(self.__nodes)
    
    
    def get_parents(self, node):
        return node.parents
    
    
    def get_neighbors(self, node):
        return node.neighbors
    

    class __Node:
        
        
        def __init__(self, info):
            """
            Creates a new isolated node with a white color.
            :param info: the value to be stored within  the node
            """
            self.info = info
            self.__origin_nodes = dict()
            self.__destiny_nodes = dict()
            self.color = 'white'
            self.cost = 0
        
        
        def add_neighbor(self, neighbor, edge_cost = 0, directed = False):
            """
            Adds a node as a neighbor by creating an edge between
            the self node and the neighbor node; an edge is a dictionary
            key of the form (neighbor, cost)
            :param neighbor: A node object to be added.
            :param edge_cost: The cost of the edge to be created.
            :param directed: If directed it'll create only an edge coming from
                the self node to the neighbor.
            """
            
            def __set_neighbor_relationship(starting_node, ending_node, cost):
                starting_node.__destiny_nodes[(ending_node.info, cost)] = ending_node
                ending_node.__origin_nodes[(starting_node, cost)] = starting_node
            
            
            __set_neighbor_relationship(self, neighbor, edge_cost)
            
            if not directed: __set_neighbor_relationship(neighbor, self, edge_cost)
        
        
        @property
        def neighbors(self, ):
            return deepcopy(self.__destiny_nodes.values())
        
        
        @property
        def parents(self, ):
            return deepcopy(self.__origin_nodes.values())
        
        
        def __del__(self, ):
            
            
            def __pop_nodes(nodes, side, info):
                
                for node in nodes:
                    edges = [x for x in node.__dict__[side].keys() if x[0] == info]
                    
                    for edge in edges:
                        node.__dict__[side].keys.pop(edge)
            
            
            origin_nodes = self.__origin_nodes.values()
            destiny_nodes = self.__destiny_nodes.values()
            far = '_Node__destiny_nodes'
            near = '_Node__origin_nodes'
            __pop_nodes(origin_nodes, far)
            __pop_nodes(destiny_nodes, near)
        
        
        def __eq__(self, other):
            """
            A node will be equals to another if their info have the same values,
            also if the edges that end in the self node are equal to the ones
            that end in the other node
            """
            
            def __get_all_edges(node):
                origins_set = set(node.__origin_nodes.keys())
                destinys_set = set(node.__destiny_nodes.keys())
                return deepcopy(origins_set.union(destinys_nodes))
            
            
            are_equals = self.info == other.info \
                    and __get_all_edges(self) == __get_all_edges(other)
            return are_equals