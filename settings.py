class Settings():
	"""A class to store all the settings for Alien Invasion."""
	
	def __init__(self):
		"""Initialize the game's settings."""
		#Screen settings
		self.screen_width = 1300
		self.screen_height = 700
		self.bg_colour = (200, 255, 200)
		
		#Ship settings
		self.ship_speed_factor = 1.5
		
		#Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_colour = (60, 60, 60)
		self.bullets_allowed = 3
		
