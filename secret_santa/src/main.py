import random
from typing import List
from copy import deepcopy

import click

from read_write import output_files_to_send, output_result, parse_input
from participant import Participant
from visualize import visualize


@click.command()
@click.option("--input_path", help="Path to input file")
@click.option("--output_dir", default=None, help="Path to output dir file. Default will only print result in stdout")
@click.option('--files_to_send', '-fs', is_flag=True, help="Include flag to generate all files to send to participants.")
@click.option('--export_graph', '-g', is_flag=True, help="Output a graph.")
def main(input_path, output_dir, files_to_send, export_graph):
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

			random.shuffle(participants) # Not necessary but adds a bit of randomness to the solution

		if participants == []:
			break
		
		counter += 1

	if output_dir:
		output_result(dones, output_dir)

	if files_to_send:
		output_files_to_send(dones, output_dir)

	if export_graph:
		visualize(dones)


if __name__ == "__main__":
	main()
