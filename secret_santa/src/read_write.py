from datetime import datetime
from os import path, mkdir
from typing import List, Optional

from participant import Participant


def parse_input(input_path: str) -> List[Participant]:

    with open(input_path, "r") as f:
        lines: List[str] = f.read().splitlines()

    participants: List[Participant] = []
    for l in lines:
        name, group = l.split(",")
        participants.append(Participant(name=name, group=group))
	
    return participants


def output_result(participants: List[Participant], output_dir: Optional[str]) -> None:

    str_list: List[str] = map(str, participants)
    result_str: str = "\n".join(str_list)
    
    if output_dir:
        now: datetime = datetime.utcnow()
        now_str: str = now.strftime("%Y%m%dT%H%M%S")
        generated_dir: str = path.join(output_dir, now_str)
        mkdir(generated_dir)
        output_path: str = path.join(generated_dir, "result.txt")

        with open(output_path, "w") as f:
            f.write(result_str)
    
    else: print(result_str)
