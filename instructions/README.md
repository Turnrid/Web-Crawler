# CS 1440 Assignment 5 Instructions

## Description

Rely on 3rd-party libraries to quickly produce a functioning web crawler.  Use
Exception Handling to deliver a safe and robust solution to our client.
Deliver a well-tested and documented programming product by the end of this
sprint.


## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 5.0
Average Score % (Grade)          | 83.7% (B+)
% students thought this was Easy | 56.8%
... Medium                       | 29.5%
... Hard                         | 1.1%
... Too Hard/Did not complete    | 11.6%


## Objectives

*   Use recursion to solve a real-world problem
    *   Identify base cases
    *   Avoid infinite recursion
*   Leverage software libraries instead of re-inventing wheels
    -   urllib
    -   Requests
    -   BeautifulSoup
*   Understand how URLs are constructed and used
*   Create robust software by handling exceptions instead of crashing


## Preparation

0.  Clone the starter code repository.
1.  Carefully read these instructions and other documentation provided.
2.  Install the required libraries (installation instructions are given below).  
    *   Ensure that all required libraries are correctly installed by running
        each of the programs found under the `demo/` directory
    *   The `crawl.py` starter program  will successfully run when all required
        libraries are installed.  It won't do anything useful, but it won't
        crash.
3.  Study the `crawl.py` starter program.
    *   Identify the base case(s) of this problem's recursion.
    *   Draft your Software Development Plan *before* you begin writing any
        code.  For this assignment it is especially important for you to really
        understand where you are going before you start writing code.


## Submission Instructions

*   **IMPORTANT NOTE: This assignment is *not* eligible for the grading gift.  This due date cannot be moved.**
*   Tag commits at the end of select phases of the SDP:
    
    0.  Tag `analyzed` on the commit at the end of **Phase 1: System Analysis**
        *   Submission should include:
            *   Work finished on Software Development Plan phases 0 and 1, including relevant updates to `Plan.md`
            *   `Signature.md` updated
    1.  Tag `designed` on the commit at the end of **Phase 2: Design**
        *   Submission should include:
            *   Work finished on Software Development Plan through phase 2, including pseudocode and relevant updates to `Plan.md`
            *   `Signature.md` updated
            *   First draft of `Manual.md` describes the expected final product
    2.  Tag `implemented` on the commit at the end of **Phase 3: Implementation**
        *   Submission should include:
            *   Work finished on Software Development Plan through phase 3, including relevant updates to `Plan.md`
                *   We do *not* require Phase 3 to be filled out in `Plan.md`, but you may want to document notable events that happen during implementation (such as removing an unnecessary function/class)
                    *   **DO NOT COPY SOURCE CODE INTO PHASE 3 OF THE PLAN FILE *unless* it is directly relevant to a notable event you document**
            *   Majority of source code is implemented inside of `src/`
            *   `Signature.md` updated
            *   Updated draft of `Manual.md` describes the current product in detail
    3.  Tag `tested` on the commit at the end of **Phase 4: Testing & Debugging**
        *   Submission should include:
            *   Work finished on Software Development Plan through phase 4, including relevant updates to `Plan.md`
            *   Necessary updates and fixes to source code are applied
            *   `Signature.md` updated
    4.  Tag the final commit of this sprint `deployed`.
        *   Submission should include:
            *   Updated `README.md` with notes for your grader, if necessary
            *   Finalized `Signature.md` and `Plan.md` files
            *   Updated `Manual.md` file to match the final product
    5. **A special note**: the tags `implemented`, `tested`, and `deployed` may be on the same commit, but the rest must remain independent of each other and they must go in the order listed above.
        *   **IMPORTANT:** Having many different commits and having your tags on different commits will make it easier for your grader to know if work was properly done at the expected times
        * Noting anything in commit messages such as "This is actually the designed phase" (etc.) will not count, it is *based only on the tags themselves only*.
        * Any tags that are missing will be graded as if that tag and it's submission parts were not submitted, and therefore will not be graded, but rather recieve a 0 (on those tags).
*   Push tags **and** `master` branch to GitLab before the due date
    *   Mind the capitalization and spelling of your tags!
    *   `$ git push origin master`
    *   `$ git push origin analyzed designed implemented tested deployed`
        *   `$ git push origin --tags` is a shorthand way to push *all* tags 


## Testing your Crawler

You need to turn this program loose on the internet to find out if it works.  To keep this program really simple, it does not honor the [Robots Exclusion Standard](https://www.robotstxt.org/).  `robots.txt` is a file found on servers which contains rules that an automated web crawler is supposed to follow.  Because your crawler doesn't look out for these files, this means that a visit by your crawler could be regarded as malicious.

So far, no DuckieCorp interns have gotten into trouble while working on this project.  To keep it that way, try to restrict your testing activities to 

*   https://cs.usu.edu
*   http://unnovative.net/level0.html
*   The supplied [Testing Server](../demo/Using_the_Testing_Server.md)
*   Websites that you personally operate
*   Websites for which you have explicit permission to crawl

Of course, as your crawler visits these sites it will inevitably follow links to other sites outside of this set.  This is okay, and you won't get into trouble as long as your crawler's activities don't become noticeable to the site admin.

**TL;DR:** Don't hammer an unsuspecting site with an unreasonable amount of automated traffic.


## Requirements

### User Interface
*   Command line arguments
    *   If given **zero** command line arguments:
        *   Produce a simple usage message detailing the arguments that can be given to the program
            *   This usage message does not need to be complicated or long
        *   Immediately exit the program without `crawl`ing
    *   If given **one or two** command line arguments:
        1.  The first argument is the `StartingURL`; the URL your `crawl` function will start crawling from
            *   `StartingURL` is an http(s) *absolute* URL (see below for an explanation of what an absolute URL is)
            *   Print an error message and quit when the user-specified URL is not *absolute* or http(s)
                *   This must be your own error message; it is wrong if the **requests** library raises an exception here
                *   It is **not** recommended to use `try/except` blocks to accomplish this
                    *   Instead check certain attributes of the `ParseResult` object after using `urllib` to `parse` a given `StartingURL`
        2.  The second argument is the `MaximumDepth`; maximum distance in number of links from the starting website to navigate.
            *   When this parameter is not supplied or is not a positive integer your program will default to `3` links
*   Once command line arguments are processed
    *   Allow `crawl` to crawl and print all links encountered from `StartingURL` to `MaximumDepth`
*   As crawl is running
    *   Allow the user to exit the program by pressing `Ctrl-C`
        *   Accomplished by catching a `KeyboardInterrupt` exception and performing logic there
            *   If your program occasionally requires hitting `Ctrl-C` a couple times before the exception is actually seen by your code, *this is okay and expected*
            *   There is no way to control for when exactly this exception is thrown during the execution of `crawl` and external libraries used may interfere with this `KeyboardInterrupt` exception that you have no control over
        *   Politely tell the user goodbye and report your early exit to the user
        *   Report the "runtime statistics" of your program after reporting the program's early termination
            *   These runtime statistics may be *slightly* inaccurate if `Ctrl-C` is invoked due as the exception may be raised at any moment during `crawl`'s performance
    *   Time the program
*   Print out the "Runtime Statistics" of your program when crawl completes
    *   Print out these statistics to `sys.stderr`
        *   `print(..., file=sys.stderr)` will allow you to print to `stderr`
    *   Print out the time it took your program to run and the number of links visited in your runtime statistics
        *   Usage of the Python Standard Library `time` module will allow you to perform program timing
        *   Consider the correlation between the number of links visited (by our definition) and the size of a datastructure our `crawl` function is passed (detailed later)
            *   Returning an integer `count` value from crawl is **not** the recommended way to solve this
            *   Recall that any *mutable* data structure in Python behaves *like* it's "pass by reference" when given as a parameter
                *   This means that changes to the data structure happening *inside* crawl are reflected in the data structure *outside* of crawl without having to explicitly return said datastructure
                *   [More information on how Python passes arguments by "assignment"](https://realpython.com/python-pass-by-reference/#passing-arguments-in-python)
    *   These runtime statistics should be printed even when the user exits the program with a `KeyboardInterrupt`


### Functionality Of Crawler
*   Your `crawl` function **must** be recursive
*   Modify the function `crawl()` to take the following parameters:
    *   `url`: an absolute URL
    *   `depth`: the current depth of recursion
    *   `maxdepth`: the maximum depth of recursion
    *   `visited`: a `set` of URLs which have already been visited
*   The return value of `crawl()` does not matter and may be ignored
*   Supply a starting distance of `0` the first time `crawl()` is called in your program.  In other words, the initial URL supplied from the command line is depth **0**.
*   You may supply an empty `set()` for the initial value of `visited`, or you can define some URLs that your crawler should never visit.  One reason you might do this would be if you encounter URLs that make your program behave badly. By adding these to `visited` you can avoid them entirely.
*   Each time `crawl()` is called:
    *   Consider if the current call to crawl is work we know how to do:
        *   If the current value of `depth` exceeds `maxdepth`
            *   Immediately return from `crawl()`
        *   If the given url has been `visited`
            *   Immediately return from `crawl()`
        *   If the given url is not valid
            *   Check whether the URL in the `href` has a non-HTTP(S) scheme to see if a URL is valid
                *   The **requests** library only works with HTTP and HTTPS schemes, and we can't `crawl` on a URL that won't work.
            *   Immediately return from `crawl()`
    *   Otherwise:
        *   Print out the URL passed in through the `url` parameter
            *   Refer to the `depth` parameter to see the current depth of recursion
            *   Use indentation to indicate the current depth of recursion.  Print four spaces for each level of recursion (see the [sample output](Output.md))
        *   Mark the url that is about to be visited as `visited`
            *   An attempt to visit a url counts as a visited url for our purposes; no need to try failed urls again later
        *   Use the **requests** library to fetch the webpage by `url`
        *   Print any exceptions that are raised and return from this invocation of `crawl()`.  
            *   Your program *must not crash* when an unavailable resource is encountered.
        *   Scan the resulting HTML for anchor tags `<a>`.
        *   `for` each anchor tag:
            *   Check for an `href` attribute; if this anchor tag doesn't have one, `continue` to the next iteration of the loop.
            *   Discard the *fragment* portion of the URL, if present.
                *   One of the libraries utilized might have something to help with this...
            *   Determine whether the `href` attribute refers to an absolute URL.  If not, make it into an absolute URL by using the `urljoin()` function and the current value of `url`
                *   One of the libraries utilized might have something to help with this...
            *   Call `crawl()` again recursively with appropriate parameters 
                *   Don't forget to +1 your depth!
    *   The exact nature of how you make crawl perform these operations is up to you! However, it *must be recursive.*
*   Handle exceptions encountered during `crawl` by printing a human-friendly message and continuing running
    *   The exception to this requirement is that this program makes a clean exit when the user presses `Ctrl-C`
        *   Do not let the program display a stack-trace in this case
    *   Do not *swallow* exceptions and have their information lost to the depth of Python. Report some information about them!


### Required Users' Manual
In addition to the required developer documentation (`Plan.md` and `Signature.md`), your web crawler must have a simple users manual. A **first draft** of this users manual is required in the commit tagged `designed` that details your *expectation* of how the program will work, from the users perspective. A **final draft** of this users manual must detail how your implementation *actually* works. It must be provided and updated in the final `deployed` commit. If the first draft of the manual is not provided, you may achieve *at most* half points possible for the manual.

A good and helpful users manual does not need to be long, but does meet the criteria listed below.

*   A quality Users' Manual explains **how to use** the program
    *   Explain the difference between *absolute* and *relative* URLs
    *   You may assume the user has a basic proficiency of the command line and knows about *their* Python installation and it's `pip` package manager
*   A quality Users' Manual details any **additional dependencies and installation steps** your program must have
    *   Your user *must* be made aware of any additional installation steps beyond installing your source code and Python
    *   Noting the required libraries to be installed *is a must* for your Users' Manual
        *   You may just tell them to `pip install` a list of packages
    *   See section below [Utilizing Software Libraries](#utilizing-software-libraries) for more information on software libraries used by the program
        *   Only *3rd Party Libraries* need to be listed as an additional dependency. Libraries in the standard library (like `sys` or `math`) do not need to be noted, as they don't need to be installed
    *   **OPTIONAL NOTE FOR ADVANCED USERS AND THE CURIOUS SOFTWARE ENGINEER**
        *   You *may* create and provide a `requirements.txt` file and reference this in the users manual
        *   You must instruct the user to run the `pip install -r requirements.txt` command
        *   A `requirements.txt` file is *not* required for this project, but is a great way to communicate required packages for a product
        *   The provided `requirements.txt` file should only list packages *pertaining to this project*
            *   Running `pip freeze` may show additional packages installed on your system and these extra packages should *not* be listed in this projects `requirements.txt`
            *   EX: This project has nothing to do with `numpy`, and `numpy` should not be listed as one of the dependencies in a provided `requirements.txt`
        *   [Official `pip` documentation on pip requirements files](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
*   A quality Users' Manual details **common errors** of the program and incorrect usages
    *   Note and compare valid and invalid inputs


### Important requirements that many students overlook

*   **IMPORTANT** The starting URL given by the command line counts as **level 0**
    *   The links contained on this page are at **level 1**, and are displayed with **4 spaces of indentation**
    *   This means that when the program crawls to a distance of 3 links, it will go to **level 3**, and display links with `4 * 3 = 12` **12 spaces of indentation**
    *   All of the links at that last level are actually visited and printed themselves, but **none** of their child links get printed!
*   **IMPORTANT** The URL must be visited **only once**
*   **IMPORTANT** The URL must be printed **only once**, right before it is fetched with the requests library
*   **IMPORTANT** Any URL you attempt to fetch is considered to be visited, regardless of the response succeeding or failing
*   **IMPORTANT** Your program **must not** print a URL that does not get fetched
*   **IMPORTANT** Your program **must not** print a URL multiple times
    * *Exceptions* are for addresses like `https://usu.edu` vs `http://usu.edu` where these two starting `http(s)` addresses can be considered different links
        * See section [What URL's Are The "Same"?](#what-urls-are-the-same) for more information on what URLs we consider to be the "same link"
*   **IMPORTANT** Use indentation to indicate the current depth of recursion.
    *   Print **four spaces** for each level of recursion (see the [sample output](Output.md))
    *   **Do not** print tabs `\t`; just print **four spaces** 


## Utilizing software libraries

As Fred Brooks Jr. explains in his essay *No Silver Bullet*, one of the biggest
advancements of modern software engineering is the availability of libraries of
pre-written code.  Reusing well-crafted code enables us to create bigger, more
reliable and more featureful systems faster and more cheaply than writing every
line of code from scratch.  Software engineers spend a considerable portion of
their time learning how to incorporate new libraries into their projects.  Part
of the lesson of this assignment is to install and use code libraries written
by others to free you to pursue your immediate goal.

But this is only a small part of this assignment; you get to start from a
functional and nearly complete program.  Your goal is to add the element of
recursion; you do not need to use features of the libraries beyond what is
shown in the starter code to do this.  My advice is to stick to the starter
code and keep things simple.

Nevertheless, it is helpful to understand what the 3rd party code is doing in
your program.  I have included demo programs under the `demo/` directory for
this purpose.  I don't anticipate that you will need to spend much effort
studying these.


### Python Standard Library

#### [urllib.parse](https://docs.python.org/3.9/library/urllib.parse.html)  URL Parsing Library

The `urlparse()` function easily evaluates whether a URL is absolute and
suitable for use with the Requests library.

```
>>> from urllib.parse import urlparse
>>> parsed = urlparse('https://cs.stanford.edu/~knuth/news.html?query=The Art of Computer Programming#this-is-a-fragment')
>>> print(parsed)
ParseResult(scheme='https', netloc='cs.stanford.edu', path='/~knuth/news.html', params='', query='query=The Art of Computer Programming', fragment='this-is-a-fragment')
```

See the [urlparse.py demo program](../demo/demo_urlparse.py) for a more complete demonstration.


The `urljoin()` function combines an absolute URL with a relative URL,
resulting in a new absolute URL.  When two absolute URLs are joined, the paths
are matched as far as they are the same.

```
>>> from urllib.parse import urljoin
>>> absPlusRel = urljoin('https://cs.stanford.edu/', '~knuth/musings.html')
>>> print(absPlusRel)
https://cs.stanford.edu/~knuth/musings.html

>>> absPlusAbs = urljoin('https://cs.stanford.edu/~knuth/vita.html', 'https://cs.stanford.edu/~knuth/graphics.html')
>>> print(absPlusAbs)
https://cs.stanford.edu/~knuth/graphics.html
```

See the [urljoin.py demo program](../demo/demo_urljoin.py) for a more complete demonstration.


*This library is part of the Python standard distribution and does not need to
be installed manually.*



### 3rd Party Libraries

You need only use the libraries described below to complete this assignment.
In fact, your program should **not** use any other 3rd-party libraries because
of the extra work it creates for the graders.

The official documentation is linked for each library; at this point in the
semester I expect you to be capable of doing your own research.

Be sure to note that your program requires an installation of the following
software libraries in your Users Manual. We use `pip` to manage these software
library installations in Python as detailed below.


#### [Requests](http://docs.python-requests.org/en/master/) HTTP Library

A simple interface to making HTTP requests from a Python program.

```
>>> import requests
>>> r = requests.get('http://checkip.dyndns.com')
>>> print(r.text)
<html><head><title>Current IP Check</title></head><body>Current IP Address: 13.103.37.144</body></html>
```


See the [requests.py demo program](../demo/demo_requests.py) for a more complete demonstration.

Install this library by running

```
pip3 install --user requests
```


#### [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) HTML Parsing Library

BeautifulSoup uses a pluggable HTML parser to parse a (possibly invalid)
document into a tree representation.  BeautifulSoup provides methods and
Pythonic idioms that make it easy to navigate, search, and modify the parse
tree.

```
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<html><head><title>Current IP Check</title></head><body>Current IP Address: 13.103.37.144</body></html>")
>>> text = soup.find('body').text
>>> print(text)
Current IP Address: 13.103.37.144
```

See the [beautifulsoup.py demo program](../demo/demo_beautifulsoup.py) for a more complete demonstration.

Install this library by running

```
pip3 install --user beautifulsoup4
```


## Absolute and Relative URLs

An absolute URL contains enough information by itself to locate a resource on a
network.  It includes, at minimum, a scheme followed by the token `://`
followed by a hostname.

The **scheme** (a.k.a. protocol) is the `http`, `https`, `ftp`, `telnet`, `ssh`,
etc. which may occur before the `://` token (when present).  This indicates how
the client program (i.e. your web browser or the `crawl.py` program) will
communicate with the server.

The **hostname** comes after the optional `scheme://` at the beginning of a URL and
before the next `/` character.  A hostname identifies a machine on the
internet.  The hostname may be a plain IP address or a human-friendly string
that can be resolved to an IP address.

Following the hostname may come the optional components **path**, **query
parameters** and/or **fragment**.

### Examples of Absolute URLs

*   `https://duckduckgo.com`
*   `https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn5/-/blob/master/instructions/README.md`
*   `https://usu.instructure.com/courses/547414/assignments/2698431?module_item_id=3503120`
*   `http://dwm.suckless.org/tutorial/#content`


### Examples of Relative URLs

*   `duckduckgo.com`
    -   A hostname only, no scheme
*   `erik.falor/cs1440-falor-erik-assn5/-/blob/master/instructions/README.md`
    -   No scheme nor hostname
*   `assignments/2698431?module_item_id=3503120`
    -   No scheme nor hostname, only a partial path
    -   The presence of query parameters don't affect whether this URL is absolute or not
*   `#content`
    -   A fragment-only relative URL which refers to back the same page it is found on
    -   A URL like this should be ignored by your program

Many resources presented on websites are referred to by a relative URL, which
leave off one or more of these components.  When a relative URL is encountered,
the client combines the corresponding information from the current document to
convert the relative URL into an absolute one.  Your `crawl()` function must
therefore know the URL of its current document so that it can substitute
missing information into relative URLs.

For example, if you point your program at `http://cs.usu.edu` and encounter a
link to `/articles.aspx`, your program will convert this to the absolute URL
`http://cs.usu.edu/articles.aspx` by means of the `urljoin()` function from the
`urllib.parse` library.


### Fragment Identifiers in URLs

A part of a URL occurring after a `#` symbol is known as a fragment, and refers
to a sub-section within a document.  Our program is concerned only with entire
documents; either a document has been visited or it has not.

Fragments should be removed from an absolute URL before checking whether it has
been visited before or not.

All relative URLs beginning with `#` refer to another location within the
current document.  Because your program should not visit the same document
twice, such URLs should be discarded.


## What URLs are "the same"?

You may find examples with your browser that don't match these rules.  These rules apply to this web crawler.

-   URLs with and without a trailing `/` are *different*
    -   e.g. your program treats `http://unnovative.net` and `http://unnovative.net/` as **different** sites
-   URLs beginning with `http://` and `https://` are *different*
    -   e.g. your program treats `http://cs.usu.edu` and `https://cs.usu.edu/` as **different** sites
-   URLs which differ only in their fragment are *the same*
    -   e.g. your program treats `http://unnovative.net`, `http://unnovative.net#hello` and `http://unnovative.net#goodbye` as **the same** site
