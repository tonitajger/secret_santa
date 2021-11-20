from datetime import datetime
from os import path, mkdir
from typing import List, Optional

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


def output_result(participants: List[Participant], output_dir: str) -> None:

    str_list: map[str] = map(str, participants)
    result_str: str = "\n".join(str_list)

    if not path.exists(output_dir):
        mkdir(output_dir)

    now: datetime = datetime.utcnow()
    now_str: str = now.strftime("%Y%m%dT%H%M%S")
    generated_dir: str = path.join(output_dir, now_str)
    mkdir(generated_dir)
    output_path: str = path.join(generated_dir, "result.txt")

    with open(output_path, "w") as f:
        f.write(result_str)
    


def output_files_to_send(participants: List[Participant], output_dir: str) -> None:

    now: datetime = datetime.utcnow()
    now_str: str = now.strftime("%Y%m%dT%H%M%S")

    if output_dir is None:
        output_dir = "output/files_to_send/"

    if not path.exists(output_dir):
        mkdir(output_dir)

    generated_dir_path: str = path.join(output_dir, now_str)
    generated_dir = path.dirname(generated_dir_path)

    for p in participants:
        
        output_path: str = path.join(generated_dir, p.name + ".txt")

        with open(output_path, "w") as f:
            f.write(f"Hej {p.name}!\nDu ska köpa en present till {p.receiver.name} för max 200kr. Lycka till!\nMVH Tomten")


