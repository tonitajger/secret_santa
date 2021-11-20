from typing import Dict, List, Tuple


class Participant:

	def __init__(self, name_group: [str, Tuple]) -> None:
		self.giver = None
		self.receiver = None

		if isinstance(name_group, str):
			self.name, self.group = name_group.split(",")
		elif isinstance(name_group, tuple):
			self.name, self.group = name_group
		else:
			raise TypeError("Constructor expects a string")

	def reset(self):
		self._receiver = None
		self._giver = None
	
	def __str__(self) -> str:
		return f"{self.name}, {self.group}"
		