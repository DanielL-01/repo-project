class Mouth:
	def __init__(self, Humaninfo):
		self.human = Humaninfo

	def describe_about_sex(self):
		print(f"I am {self.human.sex}")