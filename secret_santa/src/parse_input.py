from typing import List

from participant import Participant


def parse_input(input_file: str) -> List[Participant]:

	with open(input_file, "r") as f:
		lines: List[str] = f.read().splitlines()
		
	participants: List[Participant] = [Participant(*l.split(",")) for l in lines]
	return participants
