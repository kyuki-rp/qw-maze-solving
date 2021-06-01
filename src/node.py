#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np


class Node():
    
    def __init__(self, identifier, pos):
        self.identifier = identifier
        self.adjacent_inedges = []
        self.adjacent_outedges = []
        self.data = {}
        self.pos = pos

    def add_adjacent_inedges(self, edge):
        self.adjacent_inedges.append(edge)

    def remove_adjacent_inedges(self, search_initial_node, search_final_node):
        edge_index = [f'{edge.initial_node.identifier}->{edge.final_node.identifier}' for edge in self.adjacent_inedges].index(f'{search_initial_node}->{search_final_node}')
        _ = self.adjacent_inedges.pop(edge_index)

    def add_adjacent_outedges(self, edge):
        self.adjacent_outedges.append(edge)

    def remove_adjacent_outedges(self, search_initial_node, search_final_node):
        edge_index = [f'{edge.initial_node.identifier}->{edge.final_node.identifier}' for edge in self.adjacent_outedges].index(f'{search_initial_node}->{search_final_node}')
        _ = self.adjacent_outedges.pop(edge_index)

    def data_update(self, key, val):
        self.data[key] = val

    def dump_info(self):
        print(f"{self.identifier}:{self.data}")
        print(f"  + inedges:{','.join([f'{edge.initial_node.identifier}->{edge.final_node.identifier}' for edge in self.adjacent_inedges])}")
        print(f"  + outedges:{','.join([f'{edge.initial_node.identifier}->{edge.final_node.identifier}' for edge in self.adjacent_outedges])}")

