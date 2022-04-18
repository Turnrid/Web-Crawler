# CS 1440 Assignment 5 Hints

## Students' advice from last semester

*   I went through the starter code and completed the TODO statements one at a time.  Because this assignment was smaller, I jumped into coding with minimal planning. I should've spent more time thinking and planning.
    *   Plan ahead. This one assignment got lots easier once I paused to think it through.
    *   Follow the To-Dos and don't get too fancy.
    *   Understand what the starter code already does and what changes really need to be made to have it function correctly.
*   Play around with the demo code first to understand how it works and then it's easy to figure out.
    *   The REPL is your best friend. 
    *   Add comments as needed to clarify your code.

*   I wasted a lot of time testing my program on `https://unnovative.net`.  The right address is `http://unnovative.net`. I wasn't understanding the error I got when I tried to go to that site with `https://`.
    *   Read the Wikipedia article about URLs
    *   After I removed the fragment, it took me a while to figure out that I accidentally left the `#` in the link.
    *   I had to figure out how to use the object returned by `urlparse()`, and also realize that I needed to preserve the original URL string instead of adding all the parsed parts back together. (I'm not saying I couldn't have done something like that. I just realized it added unneeded complexity).
*   Make sure you understand recursion but don't overthink it.
    *   Don't stress too much about it. The word "recursion" seems scary, it really isn't too bad.  Review Erik's notes on recursion if you're stuck.
*   As soon as you get started on it, it'll kind of fall into place. Just be sure to understand the starter code and read through the assignment description to know exactly what you're meant to be doing.
*   Take it slow, test a lot and with different websites of different sizes.
    *   Plan to take some time with the testing server Erik gives you.  Visit it with your browser so you can see what it looks like to your program.


## Erik's Hints

*   Study the supplied demonstration programs to answer your questions about
    how to use the code libraries.
*   Get an early start on this program so you have enough time to ask questions
    before the final lecture.
*   Leave yourself plenty of time for testing.
*   Identify the base case(s) and handle these at the top of `crawl()`.
    *   *Do not* make a recursive call to `crawl()` when a base case is
        reached.
    *   Do make a recursive call to `crawl()` otherwise.
*   It is very possible for your program to get into an infinite recursive
    loop.  Watch your program carefully to guard against this!
*   Try [Exception Handling](https://wiki.python.org/moin/HandlingExceptions)
    when you run into errors.
*   You can test your program against `http://cs.usu.edu/`,
    `http://unnovative.net/level0.html`, or another website you control.  Some
    sites consider automated crawlers like this to be a nuisance, or worse.  Be
    respectful of others' bandwidth.
*   Python functions accept arguments via pass-by-reference.  When your
    `visited` set is modified within a function call, the caller will see that
    its contents have been updated.  This means that you don't need to return
    anything from `crawl()`.
*   If you encounter web pages which cause your crawler to hang, you can avoid
    them by hard-coding their URLs to the `visited` set before your program
    begins.
*   Don't expect that your program's output will exactly match my sample
    output.  What websites you are able to find will depend upon many factors
    outside of our control.  Our program is running loose on the internet,
    which means that it is crawling over a vast network that is constantly
    undergoing change, and which can present different pathways depending upon
    when and how you connect to it.
*   Don't be surprised if your program's output is different today than it was
    yesterday, even though you didn't change anything.
*   Most websites treat URLs with a trailing slash `/` the same as without (for
    example, `http://example.com` vs. `http://example.com/` are the same page).
    Other websites may serve different content from both addresses.  It's
    really not worth the hassle to try to figure this one out.  Google's own
    crawler regards slashed and un-slashed URLs as [different
    pages.](https://webmasters.googleblog.com/2010/04/to-slash-or-not-to-slash.html).
    If it's good enough for Google, it's good enough for your crawler.
*   You may find this [Crawler Test Site](https://crawler-test.com/) to be helpful.


## Using the Testing server

You will find a program called [testing_server.py](../demo/testing_server.py)
in the starter code repository.  This is a little HTTP server that can run on
your own computer.  It makes up new webpages as you browse and counts every
visited page, displaying a report when it shuts down.  Because infinite loops
can easily occur in recursive programs it shuts itself down after a few
seconds.

This program lets you work on the assignment when the internet is unavailable
as well as helps you troubleshoot tricky crawler problems.

Instructions are found in [Using the Testing server](../demo/Using_the_Testing_Server.md).
