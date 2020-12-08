# Campaign Monitor API

Project created on a Windows system using Python 3.8.6 and Flask as the web framework for the server side. It is consisted of a python, 
an html, a css and a javascript file that together make the project functional.

## Installing

* <ins>Clone or download repository: </ins>
		
	git clone https://github.com/AlexFlorides/Campaign-Monitor-API.git

requirements.txt file created automatically using command:
	
	pip3 freeze > requirements.txt

To install automatically all dependencies used in the project use the command:

	pip3 install -r requirements.txt

## Running Demo

To run the project simply open cmd terminal, change directory (using cd command) to directory of exracted files and type:
	python main.py

This starts the server that runs at "[localhost:5000/](localhost:5000/)" or "http://127.0.0.1:5000/"

After you open the website on the browser of you choice, you can see a simple page that shows a table of all active subscribers
in the list provided in the code, as well a form that the user can enter the Email Address and Full Name of a new subscriber to
add them in the list. The table is retrieving all data from the Campaign Monitor API website, therefore any change, either adding
or removing a subscriber, it will automatically update table.

### Note

For some undetermined reason when deleting a subscriber the table does not update automatically and a page refresh is required by the user!

## Adaptation

To adapt this project for your account, simply open main.py and template.js, locate listID and apiID and change them according to your values that you can found in your Campaign Monitor account.
