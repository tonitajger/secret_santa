from datetime import datetime
from os import mkdir, path, umask
from typing import List, Optional

import graphviz

from participant import Participant


def parse_input(input_path: str) -> List[Participant]:

    with open(input_path, "r") as f:
        lines: List[str] = f.read().splitlines()

    participants: List[Participant] = []
    for l in lines:
        name: str
        group: Optional[str]
        try:
            name, group = l.split(",")
        except ValueError:
            name, group = l, None
        participants.append(Participant(name=name, group=group))
	
    return participants


def generate_output_dir() -> str:
    now: datetime = datetime.utcnow()
    now_str: str = now.strftime("%Y%m%dT%H%M%S")
    generated_dir: str = path.join("output", now_str)
    mkdir(generated_dir)
    return generated_dir


def output_result(participants: List[Participant], output_dir: str) -> None:

    str_list: map[str] = map(str, participants)
    result_str: str = "\n".join(str_list)

    sub_dir: str = path.join(output_dir, "result")
    mkdir(sub_dir)

    output_path: str = path.join(sub_dir, "result.txt")

    with open(output_path, "w") as f:
        f.write(result_str)
    

def output_files_to_send(participants: List[Participant], output_dir: str) -> None:
    sub_dir: str = path.join(output_dir, "files_to_send")
    mkdir(sub_dir)

    for p in participants:
        output_path: str = path.join(sub_dir, p.name + ".txt")

        with open(output_path, "w") as f:
            f.write(f"Hej {p.name}!\nDu ska köpa en present till {p.receiver.name} för max 200kr. Lycka till!\nMVH Tomten")


def visualize(participants: List[Participant], output_dir: str) -> None:
    subdir: str = path.join(output_dir, "visualization")
    mkdir(subdir)

    dot: graphviz.Digraph = graphviz.Digraph(comment="Secret Santa")
    for p in participants:
        dot.node(p.name, p.name)
    
    for p in participants:
        if p.giver:
            dot.edge(p.name, p.receiver.name)
    
    dot.render(path.join(subdir, "secret_santa_graph.gv"))

