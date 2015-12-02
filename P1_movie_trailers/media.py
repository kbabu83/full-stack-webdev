class Movie(object):
	"""
	Bean holding some information about a movie 
	"""

	def __init__(self, title, poster_loc, trailer):
		self.title = title
		self.poster_image_url = poster_loc
		self.trailer_youtube_url = trailer

