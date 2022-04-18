#!/bin/env python3  	         	  

from urllib.parse import urlparse  	         	  
import sys  	         	  


# This demo program illustrates the `urlparse()` function  	         	  
#  	         	  
# The `urlparse()` function easily evaluates whether a URL is absolute and  	         	  
# suitable for use with the Requests library.  	         	  

def anatomyOfAUrl(url):  	         	  
    parsed = urlparse(url)  	         	  
    print(f"'{url}' breaks down like this:")  	         	  

    if parsed.scheme:  	         	  
        print(f"\tScheme        = '{parsed.scheme}'")  	         	  
    else:  	         	  
        print("\tNO scheme")  	         	  

    if parsed.netloc:  	         	  
        print(f"\tLocation      = '{parsed.netloc}'")  	         	  
    else:  	         	  
        print("\tNO location")  	         	  

    if parsed.path:  	         	  
        print(f"\tPath          = '{parsed.path}'")  	         	  
    else:  	         	  
        print("\tNO path")  	         	  

    if parsed.params:  	         	  
        print(f"\tParameters    = '{parsed.params}'")  	         	  
    else:  	         	  
        print("\tNO parameters")  	         	  

    if parsed.query:  	         	  
        print(f"\tQuery         = '{parsed.query}'")  	         	  
    else:  	         	  
        print("\tNO query")  	         	  

    if parsed.fragment:  	         	  
        print(f"\tFragment      = '{parsed.fragment}'")  	         	  
    else:  	         	  
        print("\tNO fragment")  	         	  


if len(sys.argv) < 2:  	         	  
    for url in [ 'http://unnovative.net/levels/level1.html',  	         	  
            'unnovative.net/levels/level1.html',  	         	  
            '//unnovative.net/?key=value',  	         	  
            'unnovative.net',  	         	  
            'http://localhost:8000',  	         	  
            'http://localhost/',  	         	  
            'http://localhost:8000/level0.html',  	         	  
            'https://usu.instructure.com/courses/518265/pages/5-readings-and-resources?module_item_id=3263688#approach', ]:  	         	  
        anatomyOfAUrl(url)  	         	  
        print()  	         	  
else:  	         	  
    for url in sys.argv[1:]:  	         	  
        anatomyOfAUrl(url)  	         	  
        print()  	         	  
