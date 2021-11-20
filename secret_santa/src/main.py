import random
from typing import List
from copy import deepcopy

from tqdm import tqdm

from parse_input import parse_input
from participant import Participant


def main():
	participants_original: List[Participant] = parse_input("./input/participants.txt")

	counter = 1
	while True:
		dones = []
		participants: List[Participant] = deepcopy(participants_original)
  
		while participants:
			current = participants.pop(0)

			if current.giver: 
				continue
				
			giver = current.assign_giver(participants)
			if giver is None:
				break

			if current.is_done:
				dones.append(current)
			else:
				participants.append(current)

			random.shuffle(participants)
   
		if participants == []:
			break
		
		counter += 1


if __name__ == "__main__":
	for i in tqdm(range(int(1e3))):
		main()
