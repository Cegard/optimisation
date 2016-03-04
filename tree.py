# -*- coding: utf-8 -*-
from graph import Graph
from helpers import list_add


class Tree(Graph):
    
    
    def __init__(self, root_info):
        Graph.__init__(self)
        self.add_node(root_info)
        self.__head = self.get_nodes(root_info)
    
    
    def add_child(self, node,  node_info):
        """
        Checks if there's a cycle in the tree, if there's not then
        creates a node and adds it to the tree, returns a boolean
        saying if the node was added or not
        """
    
    
    def __makes_a_cycle(self, starting_node, info, cost = 0):
        
        
        def __set_lists(iter_l):
            l1 = []
            l2 = [list_add(l1, x) for x in iter_l]
            return (l1, l2)
        
        
        parents = self.get_parents(starting_node)
        parent_infos, parent_nodes = __set_lists(parents)
        makes_a_cycle = node_info in parent_infos
        
        while (not makes_a_cycle and parent_nodes != []):
            parents = [x for x in self.get_parents(y) for y in parent_nodes]
            parent_infos, parent_nodes = __set_lists(parents)
            makes_a_cycle = node_info in parent_infos
        
        return makes_a_cycle
    
    
    makes_a_cycle = __makes_a_cycle(node, info)
    
    if not makes_a_cycle: self.add_node()