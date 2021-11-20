from typing import List, Tuple

from participant import Participant


def parse_input(input_file: str) -> List[Participant]:

    with open(input_file, "r") as f:
        lines: List[str] = f.read().splitlines()

    participants: List[Participant] = []
    for l in lines:
        name, group = l.split(",")
        participants.append(Participant(name=name, group=group))
	
    return participants
