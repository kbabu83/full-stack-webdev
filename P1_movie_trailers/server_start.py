#!/usr/bin/env python
import webserver

def main():
	# Start a server instance on the default port (8888)
	server = webserver.WebServer()
	server.start_server()	


if __name__ == '__main__':
	main()
