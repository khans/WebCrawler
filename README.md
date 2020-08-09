walrus.ai - "Woogle" Code Challenge
===================================

## **Stage 1**

**Please complete both of the components below.**

### Backend: Web Crawler

Write a crawler program that, when given a url and an integer limit, crawls the url, any links on the page, any links on those pages, and so on and so forth. For each crawled url, output the url and the page title. Your program should not crawl pages more than the limit.

### Frontend: Search UI

Build a simple UI with a form with two input boxes — one for the url and one for the limit. On form submission, the crawler should run and the application should display the list of crawled pages.

### Prerequisites:
Python 3
	https://www.python.org/downloads/
Flask - Web framework for Python 
	command: pip3 install Flask
Requests:
	command: pip3 install requests
Beautiful Soup:
    command: pip3 install beautifulsoup4
Editor:
	Sublime Text 

### Working:
1) In my directory "WebCrawlerFiles", I created a file "webcrawler.py" in which I wrote my Flask Application. This will serve as the Backend.
2) To run the flask application, on the mac terminal, navigate to the directory and run the command: 
	python3 webcrawler.py 
3) The application will run on port 5000. You can test the localhost on the browser (http://localhost:5000/) to see if it gives the message, "Welcome! Your site is up and running!"
4) We will need to run the html file "urlform.html". This html file contains the form which acts as the Frontend.
5) Run the html file and fill in the form with the url and an integer limit.
6) If everything goes smoothly, the url and subsquent other urls will be crawled. The crawled urls, along with their titles are collected in a datastructure of the form:
[[<url1>,<title1>],[<url2>,<title2>]...] 
7) The results of this datastructure will be displayed using the "results.html" file. This file resides in the "templates" folder.
8) If the entered url on the "urlform.html" is incorrect, broken, or to which a connection cannot be established an html message: "Your Input URL might be broken!" will be displayed on the screen". This html message is from the "errors.html" file in the templates folder as well.
9) By default, I'm testing on the url https://walrus.ai/
10) Please Note line Number  57 of webcrawler.py:    "res = requests.get(extract, timeout=3)", I set a timeout of 3 while making a connection with an extracted url. If I increase it or omit the timeout, the processing will take very long.
11) The results.html file is simply printing out the results in a tabulated format.

### Unit Testing
1) For unit testing the application and the method in "webcrawler.py", I created a test file, "test_webcrawler.py". It resides in the same directory as "webcrawler.py"
2) The unit tests are for testing the local host if it is up, to test if the status code is 200 if a connection is established.
3) If a rule does noty exist on the localhost it will give a status code of 401
4) There are exceptions being printed to the console for broken urls.
5) The corner cases for the method : webcrawler_method(<string>,<int>) are tested in the test_webcrawler_method_corner_cases() method of the test file.
6) To run the unit test cases, simply type: 
	"python3 -m unittest test_webcrawler.py"

Note: The Samples directory has screenshots of results for url https://walrus.ai/ and limit 23 and 4.


### Resources: 
I have listed resources that I used for this project:
##BeautifulSoup:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
##Flask:
https://www.tutorialspoint.com/flask/index.htm
https://flask.palletsprojects.com/en/1.1.x/testing/
##Naming convention:
https://www.python.org/dev/peps/pep-0008/
https://medium.com/@dasagrivamanu/python-naming-conventions-the-10-points-you-should-know-149a9aa9f8c7
##Stack Overflow:
https://stackoverflow.com/questions/57337321/flask-b-text-appears-before-request-data-results
https://stackoverflow.com/questions/44892061/flask-unittest-for-post-method
https://stackoverflow.com/questions/56716750/how-to-extract-absolute-url-of-href-with-relative-path