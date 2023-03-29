from eye import Eyes
from mouth import Mouth

class Head:
	def __init__(self, Humaninfo):
		self.human = Humaninfo
		self.eyes = Eyes()
		self.mouth = Mouth(self.human) 