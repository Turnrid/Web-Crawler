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


print("\tTODO: delete each TODO message as you fulfill it", file=sys.stderr)  	         	  

print("\tTODO: You will need to change crawl's signature to fulfill this assignment.", file=sys.stderr)  	         	  
def crawl(url):  	         	  
    """  	         	  
    Given an absolute URL, print each hyperlink found within the document.  	         	  

    Your task is to make this into a recursive function that follows hyperlinks  	         	  
    until one of two base cases are reached:  	         	  

    0) No new, unvisited links are found  	         	  
    1) The maximum depth of recursion is reached  	         	  
    """  	         	  

    print("\tTODO: Check the current depth of recursion; return now if you have gone too deep", file=sys.stderr)  	         	  
    print("\tTODO: Print this URL with indentation indicating the current depth of recursion", file=sys.stderr)  	         	  
    print("\tTODO: Handle exceptions (including KeyboardInterrupt) gracefully and prevent this program from crashing", file=sys.stderr)  	         	  
    response = requests.get(url)  	         	  
    if not response.ok:  	         	  
        print(f"crawl({url}): {response.status_code} {response.reason}")  	         	  
        return  	         	  

    html = BeautifulSoup(response.text, 'html.parser')  	         	  
    links = html.find_all('a')  	         	  
    for a in links:  	         	  
        link = a.get('href')  	         	  
        if link:  	         	  
            # Create an absolute address from a (possibly) relative URL  	         	  
            absoluteURL = urljoin(url, link)  	         	  

            # Only deal with resources accessible over HTTP or HTTPS  	         	  
            if absoluteURL.startswith('http'):  	         	  
                print(absoluteURL)  	         	  

    print("\n\tTODO: Don't just print URLs found in this document, visit them!", file=sys.stderr)  	         	  
    print("\tTODO: Trim fragments ('#' to the end) from URLs", file=sys.stderr)  	         	  
    print("\tTODO: Use a `set` data structure to keep track of URLs you've already visited", file=sys.stderr)  	         	  
    print("\tTODO: Call crawl() on unvisited URLs", file=sys.stderr)  	         	  

    return  	         	  


# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool
if __name__ == "__main__":

    ## If no arguments are given...  	         	  
    if len(sys.argv) < 2:  	         	  
        print("TODO: Put a helpful usage message here.", file=sys.stderr)
        exit(0)  	         	  
    else:  	         	  
        url = sys.argv[1]  	         	  

    print("\tTODO: determine whether variable `url` is an absolute URL", file=sys.stderr)  	         	  
    print("\t\tIf `url` is not absolute, notify user and call exit")

    print("\tTODO: allow the user to optionally override the default recursion depth of 3", file=sys.stderr)  	         	  
    maxDepth = 3  	         	  

    plural = 's' if maxDepth != 1 else ''  	         	  
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")  	         	  

    print("\tTODO: note what time the program began", file=sys.stderr)  	         	  

    print("\tTODO: crawl() keeps track of its max depth with a parameter, not a global!", file=sys.stderr)  	         	  
    print("\tTODO: wrap this call to crawl() in a try/except block to catch KeyboardInterrupt", file=sys.stderr)  	         	  
    crawl(url)  	         	  

    print("\tTODO: after the program finishes for any reason, report how long it ran and the number of unique URLs visited", file=sys.stderr)  	         	  
    print("\tTODO: are all of the TODOs deleted?", file=sys.stderr)  	         	  
