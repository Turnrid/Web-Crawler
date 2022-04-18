#!/bin/env python3  	         	  

# if this doesn't work because of a missing package, `pip3 install --user requests`  	         	  
import requests  	         	  


# This demo program illustrates the requests library  	         	  
#  	         	  
# Requests is a simple interface to making HTTP requests from a Python program.  	         	  

def demo(url):  	         	  
    try:  	         	  
        # if an error happens anywhere in this `try` block...  	         	  
        response = requests.get(url)  	         	  
        print(f"[{response.status_code} '{response.reason}'] {response.url}")  	         	  
        i = 5  	         	  
        for line in response.text.split('\n'):  	         	  
            if i == 0:  	         	  
                print('\t...')  	         	  
                break  	         	  
            print(f"\t{line}")  	         	  
            i -= 1  	         	  

    except Exception as e:  	         	  
        # ... this block of code will be run in response  	         	  
        print(f"Failed to get {url} because {e}")  	         	  

    finally:  	         	  
        # The final print() will *always* happen, exception or no  	         	  
        print()  	         	  


demo('http://example.com')  	         	  
demo('https://cs.usu.edu/about/contact')  	         	  
demo('http://unnovative.net/does-not-exist.html')  	         	  
demo('ftp://unnovative.net/does-not-exist.html')  	         	  
