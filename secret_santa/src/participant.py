from typing import List, Optional


class Participant:
	def __init__(self, name: str, group: Optional[str] = None, giver: Optional["Participant"] = None,
				 receiver: Optional["Participant"] = None) -> None:
		self.name: str = name
		self.group: Optional[str] = group
		self.giver: Optional[Participant] = giver
		self.receiver: Optional[Participant] = receiver
	
	@property
	def is_done(self) -> bool:
		return self.giver is not None and self.receiver is not None
	
	def assign_giver(self, participants: List["Participant"]) -> Optional["Participant"]:
		if self.giver:
			return None

		giver: Optional["Participant"] = self._get_first_possible_giver(participants)
		if giver is None:
			return None
		
		self.giver = giver
		giver.receiver = self
		return giver

	
	def _get_first_possible_giver(self, participants: List["Participant"]) -> Optional["Participant"]:

		for p in participants:
			if self.name == p.name:
				continue
			if self.group is not None and self.group == p.group:
				continue
			if p.receiver is not None:
				continue
			if (p.giver is not None and p.giver == self) or (self.receiver is not None and self.receiver == p):
				continue 
			return p
		return None
	
	def __str__(self):
		return f"name: {self.name}, group: {self.group}, receiver: {self.receiver.name}, giver: {self.giver.name}"
