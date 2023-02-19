import pandas as pd
import graphviz
import os

os.environ['PATH'] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

def graph_automata(self, states, alphabet, initial_state, accepting_states, trans_func):
    states = set(states)
    alphabet = set(alphabet)

    automata = graphviz.SimpleDFA(states, alphabet, initial_state, accepting_states, trans_func)

    graph = automata.trim().to_graphviz()

    graph.attr(rankdir='LR')

    graph.render('Nier', format='pdf', view=True)