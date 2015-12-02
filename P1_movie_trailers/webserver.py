import socket

import media
import fresh_tomatoes

class WebServer(object):

	def __init__(self, port=8888):
		"""
		Constructs a new WebServer object.
		:param port: Port number which the server binds to (default: 8888)
		:return: nothing
		"""
		self.host = ''	#default to localhost
		self.port = port

	def get_movie_list(self, filename):
		"""
		Creates a list of movies from a given file. The file must hold the details
		in the format,
		##<Movie Name>##<Box image path>##<Trailer URL>##
		One line holds info about one movie

		:param filename: Input filename with movie data in the mentioned format
		:return: returns a list of 'movie.Movie' objects
		"""

	 	f = open(filename, 'rU')
		movies = []
		for line in f:
			data = line.split('##')
			title = data[1]
			poster = data[2]
			trailer = data[3]

			movie = media.Movie(title, poster, trailer)
			movies.append(movie)
	 	
	 	return movies

	def start_server(self):
		"""
		Starts a webserver on the set port number. Sends a HTTP response with 
		HTML data of the list of movies and related data
		Waits infinitely for HTTP requests. 

		:param: no params
		:return: nothing 
		"""
		listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listen_socket.bind((self.host, self.port))
		listen_socket.listen(1)
		print 'Serving HTTP on port %s ...' % self.port
		while True:
			client_connection, client_address = listen_socket.accept()
			request = client_connection.recv(1024)
			print request

			http_response = """\
			HTTP/1.1 200 OK

			{html_content}
			"""
			movies = self.get_movie_list('movie_list')
			view_content = fresh_tomatoes.open_movies_page(movies)

			http_response = http_response.format(html_content=view_content)

			client_connection.sendall(http_response)
			client_connection.close()


