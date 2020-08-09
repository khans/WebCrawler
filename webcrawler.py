'''
    Flask Application for Python. This module webcrawler.py will contain the major algorithm for web crawling
    I will be using BFS to collect links on the first page, then subsequently keep extracting the links within that page in a FIFO  
'''

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

from collections import deque
import requests
import bs4 
import urllib.parse

#Localhost
@app.route('/')
def index():
	return "<h1>Welcome! Your site is up and running!</h1>"

# Accepting the input from the html file "urlform.html"
@app.route('/input',methods = ['POST', 'GET'])
def input():
    if request.method == 'POST':
        given_url = request.form['inputurl']
        limit = int(request.form['limit'])
        result = webcrawler_method(given_url,limit)
        if len(result) == 0:
        	return render_template('errors.html')
        return render_template('results.html',result = result)
    else:
        given_url= request.args.get('inputurl')
        limit = int(request.args.get('limit'))
        if len(result) == 0:
        	return render_template('errors.html')
        result = webcrawler_method(given_url,limit)
        return render_template('results.html',result = result)

# The webcrawler method which will take a url and an integer limit as input and use a BFS to crawl the links on that url

def webcrawler_method(given_url,limit):
    result = []			#Result is an array which in a smooth run should be of type[[url1,title1],[url2,title2]...]
    if given_url is None or given_url == '':
    	return result
    
    # create a queue using deque()
    queue = deque();
    queue.append(given_url); visited = set(); # visited is the set that will keep a check on duplicates. 
    #Initialize counter cnt to 0 and check it against the limit
    cnt = 0
    
    # Loop to pop exhaust the queue until the limit has reached
    while (queue and cnt<limit):
        extract = queue.popleft()
        if extract not in visited:
           
            try:
                res = requests.get(extract, timeout=3)
            except:
                print("An exception occurred, I can't connect with %s" %extract)
                continue
            cnt += 1
            soup = bs4.BeautifulSoup(res.text,'lxml')
            title_array = soup.select('title')
            title = ''
            if title_array:
                title = title_array[0].getText()

            result.append([extract,title])
            visited.add(extract)
            
            # Loop through the links and collect valid urls and populate the queue
            for link in soup.find_all('a',href = True):

                if len(link['href']) == 0:       
                	continue;
                if link['href'][:2] == '//':     # form the correct url if there are double slashes
                    correct_url = 'https:'
                    correct_url += link['href']
                    queue.append(correct_url)
                elif link['href'][0] == '/':	# form the correct url if theres a /
                	correct_url = urllib.parse.urljoin(extract, link['href'])
                	queue.append(correct_url)
                
                elif link['href'][0] =='#' or link['href'][0] =='.':			#Skip what begins with a # or a .
                    continue
                else:
                	if link['href'] not in visited:
                		queue.append(link['href'])
                	else:
                		continue
                	

    return result



if __name__ == '__main__':
	#app.debug = True;
	app.run()
	#app.run(debug = True)