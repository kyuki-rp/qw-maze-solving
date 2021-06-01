#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src import QuantumWalk
from src import Network
from src import Observer

    
def experiment1(out_dir):
    
    # Setting graph
    graph = Network()
    graph.create_lattice_graph(5,6)
    properties = {'4,4':'sink'}
    graph.set_properties(properties)
    graph.add_selfloop_edge('0,0', data={'state':1})
    graph.add_selfloop_edge('5,4', data={'state':0})
    graph.add_bidirectional_edge('0,0', '1,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,1', '1,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,3', '1,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,4', '1,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,1', '2,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,3', '2,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,2', '3,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,2', '4,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,2', '4,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,3', '5,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,3', '5,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,1', '5,0', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,1', '5,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,4', '5,4', data=({'state':0},{'state':0}))
    graph.get_edge('0,0', '0,0').data_update(key='args', val={'tailport':'w', 'headport':'w'})
    graph.get_edge('5,4', '5,4').data_update(key='args', val={'tailport':'e', 'headport':'e'})
    graph.set_fake_node()

    # Setting quantum walk on network
    qw = QuantumWalk(graph)
    qw.set_coin()

    # Time evolution
    observer = Observer(graph)
    for i in range(10):
        observer.gv_plot(f'{out_dir}/gv_{i}.png', node_sep=0.8)
        observer.gv_plot(f'{out_dir}/gv_{i}.eps', node_sep=0.8)
        print(f'gv_{i}')
        qw.evolve()

    # Output log
    qw.to_edge_df(out_dir)

def experiment2(out_dir):
    
    # Setting graph
    graph = Network()
    graph.create_lattice_graph(5,4)
    properties = {'0,3':'sink'}
    graph.set_properties(properties)
    graph.add_selfloop_edge('0,0', data={'state':1})
    graph.add_selfloop_edge('0,2', data={'state':0})
    graph.add_bidirectional_edge('0,2', '0,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,0', '1,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,1', '1,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,0', '2,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,1', '2,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,0', '3,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,1', '3,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,0', '1,0', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,0', '2,0', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,2', '1,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,2', '2,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,0', '3,0', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,2', '3,2', data=({'state':0},{'state':0}))
    graph.get_edge('0,0', '0,0').data_update(key='args', val={'tailport':'w', 'headport':'w'})
    graph.get_edge('0,2', '0,2').data_update(key='args', val={'tailport':'w', 'headport':'w'})
    graph.set_fake_node()

    # Setting quantum walk on network
    qw = QuantumWalk(graph)
    qw.set_coin()

    # Time evolution
    observer = Observer(graph)
    for i in range(10):
        observer.gv_plot(f'{out_dir}/gv_{i}.png', node_sep=1)
        observer.gv_plot(f'{out_dir}/gv_{i}.eps', node_sep=1)
        print(f'gv_{i}')
        qw.evolve()

    # Output log
    qw.to_edge_df(out_dir)

def experiment3(out_dir):
    
    # Setting graph
    graph = Network()
    graph.create_lattice_graph(5,3)
    properties = {'0,4':'sink'}
    graph.set_properties(properties)
    graph.add_selfloop_edge('0,3', data={'state':0})
    graph.add_selfloop_edge('0,1', data={'state':1})
    graph.add_bidirectional_edge('0,4', '0,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,2', '0,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,1', '0,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,1', '1,0', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,1', '1,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,3', '1,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,3', '1,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,1', '1,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,2', '1,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,0', '2,0', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,4', '2,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,0', '2,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,1', '2,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,2', '2,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,3', '2,4', data=({'state':0},{'state':0}))
    graph.get_edge('0,3', '0,3').data_update(key='args', val={'tailport':'w', 'headport':'w'})
    graph.get_edge('0,1', '0,1').data_update(key='args', val={'tailport':'w', 'headport':'w'})
    graph.set_fake_node()

    # Setting quantum walk on network
    qw = QuantumWalk(graph)
    qw.set_coin()

    # Time evolution
    observer = Observer(graph)
    for i in range(10):
        observer.gv_plot(f'{out_dir}/gv_{i}.png', node_sep=1)
        observer.gv_plot(f'{out_dir}/gv_{i}.eps', node_sep=1)
        print(f'gv_{i}')
        qw.evolve()

    # Output log
    qw.to_edge_df(out_dir)

def experiment4(out_dir):
    
    # Setting graph
    graph = Network()
    graph.create_lattice_graph(5,5)
    properties = {'3,0':'sink'}
    graph.set_properties(properties)
    graph.add_selfloop_edge('0,0', data={'state':1})
    graph.add_selfloop_edge('2,0', data={'state':0})
    graph.add_bidirectional_edge('0,0', '0,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,1', '0,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,2', '0,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,3', '0,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,1', '3,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,2', '3,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,3', '3,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,0', '4,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,1', '4,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,2', '4,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('4,3', '4,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,0', '2,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,1', '1,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,1', '1,0', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,0', '3,0', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,1', '3,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,1', '4,1', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,2', '2,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,2', '3,2', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,3', '2,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,3', '3,3', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('0,4', '1,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('1,4', '2,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('2,4', '3,4', data=({'state':0},{'state':0}))
    graph.add_bidirectional_edge('3,4', '4,4', data=({'state':0},{'state':0}))
    graph.get_edge('0,0', '0,0').data_update(key='args', val={'tailport':'s', 'headport':'s'})
    graph.get_edge('2,0', '2,0').data_update(key='args', val={'tailport':'s', 'headport':'s'})
    graph.set_fake_node()

    # Setting quantum walk on network
    qw = QuantumWalk(graph)
    qw.set_coin()

    # Time evolution
    observer = Observer(graph)
    for i in range(10):
        observer.gv_plot(f'{out_dir}/gv_{i}.png', node_sep=1)
        observer.gv_plot(f'{out_dir}/gv_{i}.eps', node_sep=1)
        print(f'gv_{i}')
        qw.evolve()

    # Output log
    qw.to_edge_df(out_dir)

# Call functions
experiment1(out_dir='out/ex1')
experiment2(out_dir='out/ex2')
experiment3(out_dir='out/ex3')
experiment4(out_dir='out/ex4')