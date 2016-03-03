# -*- coding: utf-8 -*-
from graph import Graph

class Tree(Graph):
    
    
    def __init__(self, root_info):
        Graph.__init__(self)
        self.add_node(root_info)
        self.__head = self.get_nodes(root_info)
    
    
    def add_child(self,  node_info):
        """
        Checks if there's a cycle in the tree, if there's not then
        creates a node and adds it to the tree, returns a boolean
        saying if it added the node or not
        """
        pass
    
    
    def __makes_a_cycle(self, starting_node, node_info):
        
        
        def __add(lst, item):
            lst.append(item)
            return item
        
        
        def __set_lists(iter_l):
            l1 = []
            l2 = [__add(l1, x) for x in iter_l]
            return (l1, l2)
        
        
        makes_a_cycle = False
        parents = self.get_parents(starting_node)
        parent_infos, parent_nodes = __set_lists(parents)
        
        while (not makes_a_cycle and parents_odes != []):
            makes_a_cycle = node_info in parent_infos
            parents = [x for x in self.get_parents(y) for y in parent_nodes]
            parent_infos, parent_nodes = __set_lists(parents)