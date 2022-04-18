# CS 1440 Assignment 5: Recursive Web Crawler

* [Instructions](./instructions/README.md)
* [Rubric](./instructions/Rubric.md)
* [Hints](./instructions/Hints.md)
* [Sample output](./instructions/Output.md)


## Background story

This time he wants to create a visualization of the World Wide Web (WWW) that captures the breadth and depth of its interconnections (something to do with Russians and fake news, sounds like a scam if you ask me!)  He is convinced that it looks like some kind of recursive tree-thing.  But he has no idea of how many branches there will be, nor how far it is from root to tip.  More data is needed.  One way to generate this data is to grab a notebook and fire up your favorite web browser.  Go to a web page (just about any page will do) and start clicking links.  Each time you click a link, check your notebook to see if you've been there before.  If you haven't, write it down in the notebook and click away.  If you have already been there, go to the next link.

If you ever get to a dead-end where there are no links to click, or if all of the links have already been visited, go back to an earlier page with unvisited links and continue from there.  Now that I think about it, you will want to keep track of which pages lead to which links so you'll know how far back into the notebook you should backtrack when you hit a dead-end...  Now that I write this down, it strikes me as being very tedious and repetitive (and error-prone!).  It's obvious that this job should be done by a program.  Google, Bing and Yahoo! have programs called "web crawlers" that do this.  It's time to write your own!  Given the time constraints we must work under, it seems prudent to leverage existing solutions instead of re-inventing the wheel.

Your task is to use software libraries to write a recursive web crawler which, given a starting URL, will visit all web pages reachable from that page, then visit all pages reachable from those pages, etc., up to a specified maximum depth.  Once a URL has been visited it must *NOT* be re-visited.  Due to the World Wide Web's structure as an undirected graph of hyperlinks, a recursive algorithm is the natural choice to traverse it.


## Running the starter code

In addition to the crawler that you will complete, 4 code demos and a test server are provided.

0.  `src/crawler.py` - The starter code that you will complete
1.  `demo/demo_beautifulsoup.py` - Example of how to use the BeautifulSoup library
2.  `demo/demo_requests.py` - Example of how to use the Requests library
3.  `demo/demo_urljoin.py` - Example of how to use the URL Join library
4.  `demo/demo_urlparse.py` - Example of how to use the URL Parse library
5.  `demo/testing_server.py` - A controlled environment in which to test your crawler

Read and run all of the demo programs to learn how to use the required libraries.
