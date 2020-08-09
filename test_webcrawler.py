try:
    import unittest,requests
    from webcrawler import app, webcrawler_method
except Exception as e:
	print("Could not import the modules: {} ".format(e))


app.testing = True



class TestWebcrawler(unittest.TestCase):
    # Checking the localhost
    def test_index(self):
    	client = app.test_client()
    	response = client.get('/')
    	self.assertEqual(response.status_code,200)
    
    # On local host if we try to run a non existing rule: 
    def test_nonexisting_rule(self):
    	client = app.test_client()
    	response = client.get('/random')
    	self.assertEqual(response.status_code,404)
	
	# Check the connection with a url and a limit if its response is 200
    def test_input_connection_url(self):
    	client = app.test_client()
    	response = client.post('/input', data=dict(inputurl='https://walrus.ai/',limit=1), follow_redirects=True)
    	self.assertEqual(response.status_code,200)
    
    # If the input url is corrupt, requests will try to connect until timeout. If no connection is made I display another template for broken url
    def test_input_connection_corrupt_url(self):
    	client = app.test_client()
    	# Excpetion print statement will be shown for a url to which connection cannot be established.
    	response = client.post('/input', data=dict(inputurl='https:/jdfnbjk',limit=1), follow_redirects=True)

    	self.assertEqual(response.status_code,200)
    	expected_response = b'<!DOCTYPE html>\n<html>\n\t<body>\n\t\t<title>Broken Input URL</title>\n\t\t\t<h2>Your Input URL might be broken!</h2>\n\t</body>\n</html>'
    	self.assertEqual(response.data,expected_response)   	
    
    # Test the content type of the response
    def test_input_content(self):
    	client = app.test_client()
    	# Excpetion print statement will be shown for a url to which connection cannot be established.
    	response = client.post('/input', data=dict(inputurl='https://walrus.ai/',limit=2), follow_redirects=True)
    	
    	self.assertEqual(response.content_type,'text/html; charset=utf-8')    	
    
    # Test the webcrawler_method, if empty list [] is returned for: an empty url, corrupt url, limit out of range
    def test_webcrawler_method_corner_cases(self):
    	self.assertEqual(webcrawler_method('',0),[])
    	self.assertEqual(webcrawler_method('https:/jdfnbjk',1),[])
    	self.assertEqual(webcrawler_method('https://walrus.ai/',0),[])
    	self.assertEqual(webcrawler_method('https://walrus.ai/',-5),[])
    
    # Test the webcrawler_method for a good input, its result and the length of the result array
    def test_webcrawler_method_correct(self):
    	self.assertEqual(webcrawler_method('https://walrus.ai/',1),[['https://walrus.ai/', 'Add automated end-to-end tests in minutes | walrus.ai']])
    	self.assertEqual(len(webcrawler_method('https://walrus.ai/',10)),10)


if __name__ == '__main__':
	unittest.main()



