from typing import List
import graphviz

from participant import Participant


def visualize(participants: List[Participant], output_path="output/visualization/results.gv") -> None:
    dot: graphviz.Digraph = graphviz.Digraph(comment="Secret Santa")
    for p in participants:
        dot.node(p.name, p.name)
    
    for p in participants:
        if p.giver:
            dot.edge(p.name, p.receiver.name)
    
    dot.render(output_path)
