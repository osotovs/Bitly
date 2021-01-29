# Bitly url shorterer

This utility allows you to shorten links through the bitly service, as well as track the number of clicks on them.
    
## How to install

Register at [bitly](https://app.bitly.com/) to receive an access token. in the script folder create the '.env' file. 
Write in it " BITLY_TOKEN = 'Bearer [access token]' ".
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

	pip install -r requirements.txt
	
It is recommended to put dependencies in a virtual environment.
To run the script, enter in the command line:

	python main.py [link for shortening]
	
It should turn out the following:

	(env) D:\self_soft\python\devman\API\bitly>python main.py https://dvmn.org/modules
	сокращенная ссылка:  bit.ly/2NLKTwO
	количество кликов:  2
	
## Project goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).