#!/usr/bin/python3  	         	  

#                         ~  	         	  
#                        (o)<  DuckieCorp Software License  	         	  
#                   .____//  	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor  	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	         	  
#  	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR  	         	  
# customer of DuckieCorp, to deal in the Software without restriction,  	         	  
# including without limitation the rights to use, copy, modify, merge,  	         	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	         	  
# permit persons to whom the Software is furnished to do so, subject to the  	         	  
# following conditions:  	         	  
#  	         	  
# The above copyright notice and this permission notice shall be included in  	         	  
# all copies or substantial portions of the Software.  	         	  
#  	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	         	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	         	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  	         	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  	         	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  	         	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  	         	  
# IN THE SOFTWARE.  	         	  


# pip install --user requests beautifulsoup4  	         	  
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys
import time


def crawl(url, depth, maxDepth, visited):
    """  	         	  
    Given an absolute URL, print each hyperlink found within the document.  	         	  

    Your task is to make this into a recursive function that follows hyperlinks  	         	  
    until one of two base cases are reached:  	         	  

    0) No new, unvisited links are found  	         	  
    1) The maximum depth of recursion is reached  	         	  
    """
    tab = "\t"
    print(f"{tab * depth}{url}")

    try:
        response = requests.get(url)
    except Exception as e:
        # ... this block of code will be run in response
        print(f"Failed to get {url} because {e}")
        return

    visited.add(url)

    if depth >= maxDepth:
        return

    html = BeautifulSoup(response.text, 'html.parser')
    links = html.find_all('a')
    notVisited = set()
    for a in links:
        link = a.get('href')
        if link:
            # Create an absolute address from a (possibly) relative URL  	         	  
            absoluteURL = urljoin(url, link)

            # Only deal with resources accessible over HTTP or HTTPS
            if absoluteURL.startswith('http'):
                splitURL = absoluteURL.split("#", 1)
                if splitURL[0] in visited:
                    continue
                else:
                    crawl(splitURL[0], depth + 1, maxDepth, visited)
    return


# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool
if __name__ == "__main__":

    ## If no arguments are given...  	         	  
    if len(sys.argv) < 2:
        print("Please give an Absolute Url to start crawling and a depth to crawl if needed", file=sys.stderr)
        exit(0)
    else:
        url = sys.argv[1]

    parse = urlparse(url)
    if not "scheme" and "path" in parse:
        print("\t\tIf `url` is not absolute.")
        exit(0)

    maxDepth = 3

    if len(sys.argv) == 3:
        maxDepth = int(sys.argv[2])

    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")

    startTime = time.time()

    depth = 0
    visited = set()
    visited.add(url)
    try:
        crawl(url, depth, maxDepth, visited)
    except KeyboardInterrupt:
        print("KeyboardInterrupt exception is caught")

    endTime = time.time()
    print(f"Done in {endTime - startTime:.3f} seconds! Number of links visited is {len(visited)}", file=sys.stderr)
