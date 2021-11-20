import random
from typing import List
from copy import deepcopy

import click
from tqdm import tqdm

from read_write import output_result, parse_input
from participant import Participant


@click.command()
@click.option("--input_path", help="Path to input file")
@click.option("--output_dir", default=None, help="Path to output dir file. Default will only print result in stdout")
def main(input_path, output_dir):
	participants_original: List[Participant] = parse_input(input_path)

	counter = 1
	while True:
		dones = []
		participants: List[Participant] = deepcopy(participants_original)
		random.shuffle(participants)
  
		while participants:
			current = participants.pop(0)

			if current.is_done:
				dones.append(current)
				continue

			if current.giver:
				participants.append(current)
				continue
				
			giver = current.assign_giver(participants)
			if giver is None:
				break

			if current.is_done:
				dones.append(current)
			else:
				participants.append(current)
   
		if participants == []:
			break
		
		counter += 1

	output_result(dones, output_dir)


if __name__ == "__main__":
	main()
