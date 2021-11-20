from typing import Optional


class Participant:
	def __init__(self, name: str, group: Optional[str] = None) -> None:
		self.name: str = name
		self.group: Optional[str] = group
		self.giver: Optional[Participant] = None
		self.receiver: Optional[Participant] = None
	
	def __str__(self) -> str:
		return f"{self.name}, {self.group}"
