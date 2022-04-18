#!/usr/bin/env python3  	         	  

def usage():  	         	  
    print("""CS1440 Recursive Web Crawler testing server

Usage:
  python testing_server.py [-host localhost] [-port 8000] [-timeout 3] [-verbose]
  python testing_server.py -help

Example: Listen on http://localhost:8000 and stay running for 3 seconds
  python testing_server.py

Example: Listen on http://localhost:4444 and stay running for 30 seconds
  python testing_server.py -port 4444 -timeout 30

Example: Listen on http://0.0.0.0:8000 forever
  python testing_server.py -host 0.0.0.0 -timeout 0

Example: Listen on http://0.0.0.0:8888 for 20 seconds, and provide a verbose report
  python testing_server.py -host 0.0.0.0 -port 8888 -timeout 20 -verbose

`-host 0.0.0.0` makes the server accessible from OUTSIDE your computer,
  provided that you know your computer's IP address and your firewall allows
  it.  Do this ONLY if you understand what this entails and accept the risk!
""")  	         	  
    exit(0)  	         	  


from http.server import HTTPServer, BaseHTTPRequestHandler  	         	  
import sys  	         	  
import threading  	         	  
import time  	         	  


class Tracker(HTTPServer):  	         	  
    def __init__(self, server_address, request_handler, verbose):  	         	  
        super().__init__(server_address, request_handler)  	         	  
        self.verbose = verbose  	         	  

        # The initial set of pages that exist in the server  	         	  
        # New pages are created as the server is explored  	         	  
        self.pages = {  	         	  
                "/": 0,  	         	  
                "/deadend": 0,  	         	  
                }  	         	  
        self.non_existant = {}  	         	  

        self.timeout = timeout  	         	  
        if self.timeout == 0:  	         	  
            # When a timeout of 0 is specified the server runs forever  	         	  
            self.snoozed = True  	         	  
            print(f"Serving from http://{server_address[0]}:{server_address[1]}/ forever\nPress Ctrl-C or visit http://{server_address[0]}:{server_address[1]}/shutdown/ to quit\n")  	         	  
        else:  	         	  
            self.snoozed = False  	         	  
            print(f"Serving from http://{server_address[0]}:{server_address[1]}/ for {self.timeout} second{plural(self.timeout, '', 's')} after first contact\nPress Ctrl-C or visit http://{server_address[0]}:{server_address[1]}/shutdown/ to quit\n")  	         	  

    def report(self):  	         	  
        zero = []  	         	  
        once = []  	         	  
        many = []  	         	  
        for page in self.pages:  	         	  
            if self.pages[page] == 0:  	         	  
                zero.append(page)  	         	  
            elif self.pages[page] == 1:  	         	  
                once.append(page)  	         	  
            else:  	         	  
                many.append(page)  	         	  

        l = len(once)  	         	  
        if l > 0:  	         	  
            print(f"{l} page{plural(l, ' was', 's were')} visited exactly once")  	         	  
            if self.verbose:  	         	  
                for page in once:  	         	  
                    print(f"\t{page}")  	         	  

        l = len(zero)  	         	  
        if l > 0:  	         	  
            print(f"\n{l} page{plural(l, ' was', 's were')} not visited at all")  	         	  
            if self.verbose:  	         	  
                for page in zero:  	         	  
                    print(f"\t{page}")  	         	  

        l = len(many)  	         	  
        if l > 0:  	         	  
            print(f"\n{l} page{plural(l, ' was', 's were')} visited many times")  	         	  
            for page in many:  	         	  
                print(f"\t{page}: {self.pages[page]}")  	         	  

        l = len(self.non_existant)  	         	  
        if l > 0:  	         	  
            print(f"\n{l} page{plural(l, ' was', 's were')} visited before they were created:")  	         	  
            for page in self.non_existant:  	         	  
                print(f"\t{page}")  	         	  


class Based(BaseHTTPRequestHandler):  	         	  
    def snoozer(self):  	         	  
        """  	         	  
        Prevent a broken crawler from running forever by shutting this server  	         	  
        down after a few seconds  	         	  
        """  	         	  
        while self.server.timeout > 0:  	         	  
            print(f"Server will shutdown in {self.server.timeout} second{plural(self.server.timeout, '', 's')}...")  	         	  
            self.server.timeout -= 1  	         	  
            time.sleep(1)  	         	  
        self.server.shutdown()  	         	  

    def listOfAnchors(self, urls):  	         	  
        """  	         	  
        Form an HTML list of anchor tags (links) pointing to input urls  	         	  
        """  	         	  
        return "\n".join([ f'<li>Visit <a href="{link}">{link}</a></li>' for link in urls.keys() ])  	         	  

    def listOfAnchorsWithFragments(self, urls):  	         	  
        """  	         	  
        Form an HTML list of anchor tags (links) pointing to input urls which contain fragments  	         	  
        """  	         	  
        return "\n".join([ f'<li>Visit <a href="{link}#fragment">{link}</a></li>' for link in urls.keys() ])  	         	  

    def serve(self):  	         	  
        """  	         	  
        Called when a valid page is requested to form an HTTP response.  	         	  
        """  	         	  
        self.server.pages[self.path] += 1  	         	  

        if self.path == "/deadend":  	         	  
            new_pages = { }  	         	  
        else:  	         	  
            # Given my URL, what new pages can you visit from here?  	         	  
            new_pages = {  	         	  
                    f"{self.path}a": 0,  	         	  
                    f"{self.path}b": 0,  	         	  
                    f"{self.path}c": 0,  	         	  
                    }  	         	  

            for path in new_pages:  	         	  
                if path not in self.server.pages:  	         	  
                    self.server.pages[path] = new_pages[path]  	         	  

        self.send_response(200)  	         	  
        self.send_header('Connection', 'close')  	         	  
        self.end_headers()  	         	  
        self.wfile.write(  	         	  
                bytes(f"""  	         	  
                <head>  	         	  
                    <title>Welcome to {self.path}</title>  	         	  
                </head>  	         	  
                <body>  	         	  
                    <h1>Welcome to {self.path}</h1>  	         	  
                    <h2>From here you can visit<h2>  	         	  
                    <ul>  	         	  
                        <li><a href="/deadend">A dead end</a></li>  	         	  
                        {self.listOfAnchorsWithFragments(new_pages)}  	         	  
                        <li><a href="/">Return home</a></li>  	         	  
                        {self.listOfAnchors(new_pages)}  	         	  
                    </ul>  	         	  
                </body>  	         	  
                """, encoding="utf_8"))  	         	  

    def do_404(self):  	         	  
        """  	         	  
        Called when a non-existant page is requested.  	         	  
        """  	         	  
        if self.path not in self.server.non_existant:  	         	  
            self.server.non_existant[self.path] = 1  	         	  
        else:  	         	  
            self.server.non_existant[self.path] += 1  	         	  

        self.send_response(404)  	         	  
        self.send_header('Connection', 'close')  	         	  
        self.end_headers()  	         	  
        self.wfile.write(  	         	  
                bytes(f"""  	         	  
                <head>  	         	  
                    <title>404, Dude!</title>  	         	  
                </head>  	         	  
                <body>  	         	  
                    <h1>Error 404!</h1>  	         	  
                    <h2>Sorry dude, wrong file!</h2>  	         	  
                    <p>You wanted to visit <code>{self.path}</code>, but that's not a place I can take you</p>  	         	  
                </body>  	         	  
                """, encoding="utf_8"))  	         	  

    def do_GET(self):  	         	  
        """  	         	  
        Called when the server receives an HTTP GET request  	         	  
        """  	         	  
        if not self.server.snoozed:  	         	  
            self.server.snoozed = True  	         	  
            threading.Thread(target=self.snoozer).start()  	         	  

        if self.path.endswith('/shutdown') or self.path.endswith('/shutdown/'):  	         	  
            print("Shutting down immediately...")  	         	  
            self.server.timeout = 0  	         	  
            self.server.manual_shutdown = True  	         	  
            threading.Thread(target=self.server.shutdown).start()  	         	  
        elif self.path in self.server.pages:  	         	  
            self.serve()  	         	  
        else:  	         	  
            self.do_404()  	         	  


def plural(n, singular, plural):  	         	  
    return singular if n == 1 else plural  	         	  


if __name__ == '__main__':  	         	  
    host, port, timeout = 'localhost', 8000, 3  	         	  

    if '-help' in sys.argv:  	         	  
        usage()  	         	  

    if '-host' in sys.argv:  	         	  
        p = sys.argv.index('-host') + 1  	         	  
        if p < len(sys.argv) and sys.argv[p] != '':  	         	  
            host = sys.argv[p]  	         	  
        else:  	         	  
            usage()  	         	  

    if '-port' in sys.argv:  	         	  
        p = sys.argv.index('-port') + 1  	         	  
        if p < len(sys.argv) and sys.argv[p].isdigit():  	         	  
            port = int(sys.argv[p])  	         	  
        else:  	         	  
            usage()  	         	  

    if '-timeout' in sys.argv:  	         	  
        p = sys.argv.index('-timeout') + 1  	         	  
        if p < len(sys.argv) and sys.argv[p].isdigit():  	         	  
            timeout = int(sys.argv[p])  	         	  
        else:  	         	  
            usage()  	         	  

    verbose = '-verbose' in sys.argv  	         	  

    keep_going = True  	         	  
    while keep_going:  	         	  
        based = Tracker((host, port), Based, verbose)  	         	  
        try:  	         	  
            based.serve_forever()  	         	  
        except KeyboardInterrupt:  	         	  
            print('except KeyboardInterrupt')  	         	  
            based.shutdown()  	         	  
            keep_going = False  	         	  
        finally:  	         	  
            based.report()  	         	  
            based.server_close()  	         	  
            keep_going = keep_going and not hasattr(based, 'manual_shutdown')  	         	  

        if keep_going:  	         	  
            print("\nRestarting...\n\n")  	         	  
