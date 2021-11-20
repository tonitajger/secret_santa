from typing import List, Optional


class Participant:
	def __init__(self, name: str, group: Optional[str] = None) -> None:
		self.name: str = name
		self.group: Optional[str] = group
		self.giver: Optional[Participant] = None
		self.receiver: Optional[Participant] = None
	
	def is_done(self) -> bool:
		return self.giver and self.receiver
	
	def assign_giver(self, participants: List["Participant"]) -> Optional["Participant"]:
		if self.giver:
			raise Exception(f"Error while trying to assign a giver to {self} which already has giver {self.giver}.")

		giver: Optional = self._get_first_possible_giver(participants)
		if giver is None:
			return
		
		self.giver = giver
		giver.receiver = self
		return giver

	
	def _get_first_possible_giver(self, participants: List["Participant"]) -> Optional["Participant"]:

		for p in participants:
			if self.group is not None and self.group == p.group:
				continue
			if self.giver is not None:
				continue
			if p.receiver is not None:
				continue
			if p.giver is not None and p.giver == self:
				continue 
			return p

	
	def __str__(self) -> str:
		return f"{self.name}, {self.group}"
	
	def __eq__(self, other: "Participant") -> bool:
		return self.name == other.name
