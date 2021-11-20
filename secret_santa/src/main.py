import random
from typing import List
from copy import deepcopy

import click

from input_output import generate_output_dir, output_files_to_send, output_result, parse_input, visualize
from participant import Participant


@click.command()
@click.option("--input_path", help="Path to input file")
@click.option("--output_results", "-r", is_flag=True, help="Include flag to generate result file")
@click.option('--files_to_send', '-fs', is_flag=True, help="Include flag to generate all files to send to participants.")
@click.option('--export_graph', '-g', is_flag=True, help="Output a graph.")
@click.option('--anonymize', '-a', is_flag=True, help="Anonymize graph and result file. Note that files to send will not be anonymized")
def main(input_path, output_results, files_to_send, export_graph, anonymize):
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

	output_dir: str = generate_output_dir()

	if files_to_send:
		output_files_to_send(dones, output_dir)

	if anonymize:
		for i, p in enumerate(dones):
			p.name = str(i)

	if output_results:
		output_result(dones, output_dir)

	if export_graph:
		visualize(dones, output_dir)


if __name__ == "__main__":
	main()
