
class Settings:
	def __init__(self):
		self.activation = False

		self.user_source = "data/user.json"
		self.anime_source = "data/anime.json"
		self.users = None
		self.animes = None
		self.menu = """
ANIME LIST APP
-------------------------------
1. VIEW ALL LISTED ANIMES
2. SEARCH ANIME BY TITLE
3. SEARCH ANIME BY GENRE
4. ADD A NEW ANIME TO THE LIST
5. REMOVE ANIME FROM YOUR LIST
6. UPDATE ANIME DETAILS
Q. QUIT APP
-------------------------------
		"""