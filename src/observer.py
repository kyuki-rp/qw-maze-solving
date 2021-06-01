#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from graphviz import Digraph
import numpy as np


class Observer():

    def __init__(self, graph):
        self.graph = graph

    def gv_plot(self, file_path, node_sep=1):

        # Setting graph
        self.gv_graph = Digraph(format="eps")
        self.gv_graph.attr(splines ='true')

        # add nodes
        for node in self.graph.nodes:
            if len(node.adjacent_inedges)==0:
                pass
            elif node.data['property']=='sink':
                self.gv_graph.node(node.identifier, label=node.data['fake_identifier'], pos=f"{node.pos[0]*node_sep},{node.pos[1]*node_sep}!", color='blue', fillcolor='lightskyblue', style='filled', fontsize = '10', fontname='Times-Roman', shape='circle', width='0.25', fixedsize='true')
            elif node.data['property']=='source':
                self.gv_graph.node(node.identifier, label=node.data['fake_identifier'], pos=f"{node.pos[0]*node_sep},{node.pos[1]*node_sep}!", color='red', fillcolor='lightpink', style='filled', fontsize = '10', fontname='Times-Roman', shape='circle', width='0.25', fixedsize='true')
            else:
                self.gv_graph.node(node.identifier, label=node.data['fake_identifier'], pos=f"{node.pos[0]*node_sep},{node.pos[1]*node_sep}!", color='black', fontsize = '10', fontname='Times-Roman', shape='circle', width='0.25', fixedsize='true')

        # add edges
        for edge in self.graph.edges:
            if edge.data['property']=='in':
                self.gv_graph.edge(edge.initial_node.identifier, edge.final_node.identifier, label=f"{edge.data['state']:.2f}", color='red', fontcolor='red', fontname='Times-Roman')
            elif edge.data['property']=='out':
                self.gv_graph.edge(edge.initial_node.identifier, edge.final_node.identifier, label=f"{edge.data['state']:.2f}", color='blue', fontcolor='blue', fontname='Times-Roman')
            elif edge.data['property']=='self':
                self.gv_graph.edge(edge.initial_node.identifier, edge.final_node.identifier, label=f"{edge.data['state']:.2f}", color='black', fontcolor='black', fontname='Times-Roman', **edge.data['args'])

        # Output figure
        self.to_fig(file_path)

    def to_fig(self, file_path):
        # Output file: '_temp.dot'
        try:
            self.gv_graph.render('_temp.dot')
        except:
            pass
        
        # Making directory
        os.makedirs('/'.join(file_path.split('/')[:-1]), exist_ok=True)

        # Changing from '_temp.dot' to 'png' or 'eps'
        extension = file_path.split('.')[-1]
        if extension=='png':
            os.system(f'dot -Kfdp -n -Tpng _temp.dot -o {file_path}')
        elif extension=='eps':
            os.system(f'dot -Tps _temp.dot -o {file_path}')
        os.remove('_temp.dot')