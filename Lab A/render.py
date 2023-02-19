from graphviz import Digraph

def visualize_nfa(nfa):
    """Visualizes an NFA using graphviz."""
    dot = Digraph()
    for i in range(nfa.num_states):
        dot.node(str(i), shape='circle', style='bold' if i in nfa.accept_states else '')
    dot.node('start', shape='point')
    dot.edge('start', str(nfa.start_state))
    for src_state, transitions in nfa.transitions.items():
        for symbol, dest_states in transitions.items():
            for dest_state in dest_states:
                dot.edge(str(src_state), str(dest_state), label=symbol)
    return dot