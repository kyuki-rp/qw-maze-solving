#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from .edge import Edge
from .node import Node


class Network():

    def __init__(self):
        self.edges = []
        self.nodes = []

    def get_adjacency_matrix(self):
        labels = [node.identifier for  node in self.nodes]
        adj_matrix = pd.DataFrame(index=labels,columns=labels)
        for (innode, outnode) in [(node.identifier, outedge.final_node.identifier) for node in self.nodes for outedge in node.adjacent_outedges]:
            adj_matrix.loc[innode, outnode] = 1
        adj_matrix = adj_matrix.replace(np.nan, 0)
        return adj_matrix
        
    def get_degrees(self):
        return self.get_adjacency_matrix().sum().to_dict()
    
    def add_node(self, identifier, pos=None):
        new_node = Node(identifier, pos)
        self.nodes.append(new_node)

    def create_lattice_graph(self, n_i, n_j):
        for i in range(n_i):
            for j in range(n_j):
                self.add_node(f'{j},{i}', pos=(j,i))

    def add_edge(self, initial_node_identifier, final_node_identifier, data=None):
        initial_node = self.get_node(initial_node_identifier)
        final_node = self.get_node(final_node_identifier)
        new_edge = Edge(initial_node, final_node, data)
        self.edges.append(new_edge)

        # Add adjacent edges and nodes information for nodes.
        initial_node.add_adjacent_outedges(new_edge)
        final_node.add_adjacent_inedges(new_edge)

    def add_selfloop_edge(self, node_identifier, data={}):
        data_ = data
        data_['property'] = 'self'
        self.add_edge(node_identifier, node_identifier, data)

    def add_bidirectional_edge(self, initial_node_identifier, final_node_identifier, data={}):
        data_ = data[0]
        data_['property'] = 'in'
        self.add_edge(initial_node_identifier, final_node_identifier, data_)

        data_ = data[1]
        data_['property'] = 'out'
        self.add_edge(final_node_identifier, initial_node_identifier, data_)
            
    def create_lattice_graph(self, n_i, n_j):
        for i in range(n_i):
            for j in range(n_j):
                self.add_node(f'{j},{i}', pos=(j,i))
                
    def get_node(self, search_identifier):
        node_index = [node.identifier for node in self.nodes].index(search_identifier)
        return self.nodes[node_index]

    def get_edge(self, search_initial_node, search_final_node):
        edge_index = [f'{edge.initial_node.identifier}->{edge.final_node.identifier}' for edge in self.edges].index(f'{search_initial_node}->{search_final_node}')
        return self.edges[edge_index]
        
    def dump_info(self):
        print('--- Nodes info ---')
        for node in self.nodes:
            node.dump_info()

        print('--- Edges info ---')
        for edge in self.edges:
            edge.dump_info()
            
    def remove_node(self, search_identifier):
        node_index = [node.identifier for node in self.nodes].index(search_identifier)
        
        # Remove adjacent_inedges
        for edge in self.nodes[node_index].adjacent_inedges[::-1]:
            self.remove_edge(edge.initial_node.identifier, edge.final_node.identifier)

        # Remove adjacent_outedges
        for edge in self.nodes[node_index].adjacent_outedges[::-1]:
            self.remove_edge(edge.initial_node.identifier, edge.final_node.identifier)

         # Remove node
        _ =  self.nodes.pop(node_index)

    def set_fake_node(self):
        fake_identifier = 0
        for node in self.nodes:
            if len(node.adjacent_inedges)!=0:
                node.data_update(key='fake_identifier', val=str(fake_identifier))
                fake_identifier += 1

    def set_properties(self, properties):
        for node in self.nodes:
            if node.identifier in properties.keys():
                node.data_update(key='property', val=properties[node.identifier])
            else:
                node.data_update(key='property', val='nomal')

    def remove_edge(self, search_initial_node, search_final_node):
        edge_index = [f'{edge.initial_node.identifier}->{edge.final_node.identifier}' for edge in self.edges].index(f'{search_initial_node}->{search_final_node}')

        # Remove adjacent_edges from node
        self.edges[edge_index].initial_node.remove_adjacent_outedges(search_initial_node, search_final_node)
        self.edges[edge_index].final_node.remove_adjacent_inedges(search_initial_node, search_final_node)

        # Remove edge
        _ = self.edges.pop(edge_index)





