# Using the Testing server

`testing_server.py` is a little HTTP server that can run on your own computer.

It makes up new webpages as you browse and counts every visited page,
displaying a report when it shuts down.  Because infinite loops can easily
occur in recursive programs it shuts itself down after a few seconds.

This program lets you work on the assignment when the internet is unavailable
as well as helps you troubleshoot tricky crawler problems.


## Quickstart

In one console run:

```
$ python demo/testing_server.py
Serving from http://localhost:8000/ for 3 seconds after first contact
Press Ctrl-C or visit http://localhost:8000/shutdown/ to quit

```

In another console run your crawler directed at the URL indicated:

```
$ python src/crawler.py http://localhost:8000/
```

## Command line interface

### Usage:

*   `python testing_server.py [-host localhost] [-port 8000] [-timeout 3] [-verbose]`
*   `python testing_server.py -help`

#### Example: Listen on http://localhost:8000 and stay running for 3 seconds

`python testing_server.py`

#### Example: Listen on http://localhost:4444 and stay running for 30 seconds

`python testing_server.py -port 4444 -timeout 30`

#### Example: Listen on http://0.0.0.0:8000 forever

`python testing_server.py -host 0.0.0.0 -timeout 0`

#### Example: Listen on http://0.0.0.0:8888 for 20 seconds, and provide a verbose report

`python testing_server.py -host 0.0.0.0 -port 8888 -timeout 20 -verbose`

`-host 0.0.0.0` makes the server accessible from OUTSIDE your computer,
provided that you know your computer's IP address and your firewall allows it.
Do this ONLY if you understand what this entails and accept the risk!


### Specify a different address and port on the command line:

If port `8000` is unavailable on your computer you will get an `OSError`:

```
OSError: [Errno 98] Address already in use
```

This happens when another program on your computer is using that port.  Try
other port numbers until you find one that is available.  Valid port numbers
run from `1024` to `65535`.

```
$ python demo/testing_server.py -port 4321
Serving from http://localhost:4321/ for 3 seconds after first contact
Press Ctrl-C or visit http://localhost:4321/shutdown/ to quit
```


### Make the server run forever

This testing server shuts itself down after a few seconds.  Specify a timeout
of `0` and you can explore it yourself in your browser.  This will help you
understand what your crawler sees and how it should behave.

```
$ python demo/testing_server.py -timeout 0
Serving from http://localhost:8000/ forever
Press Ctrl-C or visit http://localhost:8000/shutdown/ to quit
```


## Understanding the report

After the server shuts down it prints a report of pages visited with the number
of times each was visited.  Your crawler should visit each page once and *only*
once.  Your crawler *cannot* visit every link it sees.  It must respect its
base case and quit at some point.

This is what a visit by a good crawler to `http://localhost:8000/` will look
like (notice the trailing `/` in the URL):

```
41 pages were visited exactly once

81 pages were not visited at all
```

Because URLs that don't end in `/` can mean the same thing as URLs that do,
this is also good output from a crawler to `http://localhost:8000`:

```
4 pages were visited exactly once

9 pages were not visited at all

1 page was visited many times
	/: 2
```

The page `/` is visited twice is because your crawler thinks
`http://localhost:8000` and `http://localhost:8000/` are different pages while
the server thinks they are the same.  Don't worry about this, life is too short
and precious to waste on this inconsistency.

If your crawler just doesn't know when to quit you'll see output like this:

```
81 pages were not visited at all

41 pages were visited many times
	/: 68
	/deadend: 67
	/a: 20
	/b: 20
	/c: 20
	/aa: 8
	/ab: 8
    ...
```

If your crawler is just wildly guessing URLs it will visit pages before they
exist.  If you see `N pages were visited before they were created` you need to
seriously re-think your approach.
