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
		return self.giver and self.receiver
	
	def assign_giver(self, participants: List["Participant"]) -> Optional["Participant"]:
		if self.giver:
			return

		giver: Optional["Participant"] = self._get_first_possible_giver(participants)
		if giver is None:
			return
		
		self.giver = giver
		giver.receiver = self
		return giver

	
	def _get_first_possible_giver(self, participants: List["Participant"]) -> Optional["Participant"]:

		for p in participants:
			if self == p:
				continue
			if self.group is not None and self.group == p.group:
				continue
			if self.giver is not None:
				continue
			if p.receiver is not None:
				continue
			if (p.giver is not None and p.giver == self) or (self.receiver is not None and self.receiver == p):
				continue 
			return p

	
	def __str__(self) -> str:
		return f"{self.name}, {self.group}"
	
	def __eq__(self, other: "Participant") -> bool:
		return self.name == other.name
