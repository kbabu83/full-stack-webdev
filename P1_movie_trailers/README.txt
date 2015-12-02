This project runs a simple webserver instance that returns a HTML response with a list of movies with posters and trailer link upon connect.

To run the project,
a. copy the content to a local folder
b. run the command
	...> python server_start.py   
	(on Windows) 
	(or)
	$ .\server_start.py   
	(on *nix systems)

c. Open the link http://localhost:8888 in a browser tab to view the response.

Note: The method - open_movies_page() - in the given module "fresh_tomatoes" has been modified to return the HTML page as a string instead of opening the browser directly.
