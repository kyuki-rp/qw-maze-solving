#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

class QuantumWalk():

    def __init__(self, graph):
        self.graph = graph        
        self.edge_df = pd.DataFrame()

    def set_coin(self):
        walk = Walk(self.graph)
        walk.grover_walk()
        
    def get_flow(self, node):
        inflow = np.array([(inedge.initial_node.identifier, inedge.initial_node, node, self.graph.get_edge(inedge.initial_node.identifier, node.identifier).data['state']) for inedge in node.adjacent_inedges])
        outflow = np.array([(outedge.final_node.identifier, node, outedge.final_node, self.graph.get_edge(node.identifier, outedge.final_node.identifier).data['state']) for outedge in node.adjacent_outedges])
        if len(inflow) >= 2:
            inflow = inflow[np.argsort(inflow[:, 0])] # Sort by innode identifier
            outflow = outflow[np.argsort(outflow[:, 0])] # Sort by innode identifier
        return inflow, outflow

    def evolve(self):
        # Calculating next state
        new_states = []
        edge_se = pd.Series()
        self.sum_state = 0
        for node in self.graph.nodes:
            inflow, outflow = self.get_flow(node)

            if node.data['property']=='sink':
                new_state = [(innode.identifier, outnode.identifier, 0) for i, (_, innode, outnode, _) in enumerate(outflow)]
                new_states = new_states + new_state
            else:
                if len(inflow)!=0:
                    new_state = node.data['coin'].dot(inflow[:,3])
                    edge_se = edge_se.append(pd.Series(inflow[:,3], index=[f"{self.graph.get_node(i).data['fake_identifier']}->{node.data['fake_identifier']}" for i in inflow[:,0]]))

                    if np.isscalar(new_state):
                        new_state = np.array([new_state]) # To list
                    new_state = [(innode.identifier, outnode.identifier, new_state[i]) for i, (_, innode, outnode, _) in enumerate(outflow)]
                    new_states = new_states + new_state
                    self.sum_state += inflow[:,3].dot(inflow[:,3])
            
        self.edge_df = self.edge_df.append(edge_se, ignore_index=True)

        # Overwrite state
        for initial_node_identifier, final_node_identifier, state in new_states:
            self.graph.get_edge(initial_node_identifier, final_node_identifier).data_update(key='state',val=state)

    def to_edge_df(self, out_dir):
        self.edge_df.to_csv(f'{out_dir}/edge_df.csv', index=False)

class Walk():

    def __init__(self, graph):
        self.graph = graph
        
    def grover_walk(self):
        for node_identifier, degree in self.graph.get_degrees().items():
            if degree in [0, 1]:
                coin = np.identity(degree)
            elif degree==2:
                coin = np.array([[0,1],[1,0]])
            elif degree>=3:
                n=degree
                uni_array = np.zeros((degree,degree)) + 2/n
                coin = uni_array + np.eye(degree) * (-2/n + 2/n -1)
            node = self.graph.get_node(node_identifier)
            node.data_update(key='coin',val=coin)
  
            
        
