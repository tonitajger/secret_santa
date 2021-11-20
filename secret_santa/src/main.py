import os
import random
from typing import Dict, List, Tuple
from copy import deepcopy

from tqdm import tqdm

from participant import Participant


def parse_input(input_file: str) -> Dict[str, str]:

	with open(input_file, "r") as f:
		lines: List[str] = f.read().splitlines()

	participants: List[Participant] = [Participant(l) for l in lines]
	return participants



def is_done(participant: Participant):
	return participant.giver and participant.receiver


def get_possibles(current: Participant, participant_lst: List[Participant], participant_type: str) -> List[Participant]:
	possible_lst: List[Participant] = []
	types: List = ["giver", "receiver"]

	for p in participant_lst:
		if current.group is not None and current.group == p.group:
			continue
		if getattr(current, participant_type) is not None:
			continue
		
		other_participant_type: str = [t for t in types if t != participant_type][0]
		if getattr(p, other_participant_type) is not None:
			continue
		
		
		if getattr(p, participant_type) is not None and getattr(p, participant_type).name == current.name:
			continue 
		
		possible_lst.append(p)
	
	return possible_lst



def main():
	participant_lst_original: List[Participant] = parse_input("./input/participants.txt")

	counter = 1
	while True:
		# print(f"try no {counter}")
		done_participants = []
		participant_lst: List[Participant] = deepcopy(participant_lst_original)
		random.shuffle(participant_lst)
		while participant_lst:
			p1 = participant_lst.pop()
			done_participants.append(p1)
			# print(p1)

			if p1.receiver is None:
				possible_receiver_lst = get_possibles(p1, participant_lst, "receiver")

				if not possible_receiver_lst:
					participant_lst.append(p1)
					break

				receiver = possible_receiver_lst.pop()
				while p1.receiver is None:
					if receiver.giver is None:
						# print(f"setting receiver {receiver} to giver {p1}")
						receiver.giver = p1
						p1.receiver = receiver
					else:
						receiver_new = possible_lst.pop()
						possible_receiver_lst.append(receiver)
						receiver = receiver_new
						random.shuffle(possible_lst)

			if p1.giver is None:
				possible_giver_lst = get_possibles(p1, participant_lst, "giver")

				if not possible_giver_lst: 
					participant_lst.append(p1)
					break
				giver = possible_giver_lst.pop()
				while p1.giver is None:
					if giver.receiver is None:
						# print(f"setting receiver {p1} to giver {giver}")
						giver.receiver = p1
						p1.giver = giver
					else:
						giver_new = possible_lst.pop()
						possible_giver_lst.append(giver)
						giver = giver_new
						random.shuffle(possible_lst)

			# print([f"{p}, giver: {p.giver}, receiver: {p.receiver}" for p in participant_lst])
			# print([f"{p}, giver: {p.giver}, receiver: {p.receiver}" for p in done_participants])
			# print(len(done_participants))
			random.shuffle(participant_lst)
		
		
		if participant_lst == []:
			# print("final result:")
			# print([f"{p.name}, giver: {p.giver.name}, receiver: {p.receiver.name}" for p in done_participants])
			break
		
		# print([f"{p}, giver: {p.giver}, receiver: {p.receiver}" for p in done_participants])
		counter += 1
		# print("invalid shuffle retrying... \n")


if __name__ == "__main__":
	for i in tqdm(range(int(1e4))):
		main()