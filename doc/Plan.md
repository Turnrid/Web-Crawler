# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

* A webcrawler that can take an absolute URL and crawl to the default of specified depth by the user. Will catch any
problems while crawling and not crash but continue to crawl the web.

* Getting the program to a state where it is running should be easy. What I don't totally know how to do is use the
library's needed for the assignment. Also remembering how to get the recursivness of the program working well.



## Phase 1: System Analysis *(10%)*

**Deliver:**

* Data type should be a set of strings to hold data that can be manipulated and printed when needed.
* Strings that will be printed to the console showing webpages gone to as well as printing any errors that were caught.
* Algorithm to keep track of what links have been clicked and also the depth of recursion the program is at.

## Phase 2: Design *(30%)*

**Deliver:**

* Main
  * Check if enough arguments are given from the command line
  * Check if the url given is absolute
  * Determine if default of user specified depth of recursion is to be used
  * Note the time when starting to crawl a url
  * recursion depth should be a parameter
  * Wrap crawl up in the try/catch to catch keyboard interrupt
  * When finished print how long and the number of unique urls visited

* Crawl(url, depth, set of urls)
  * Check the current depth of recursion and return if we have reached the appropriate depth.
  * Print the url with the correct indentation representing recursion depth
  * Handle any exceptions gracefully to prevent from crashing
  * Take the html and find the links in the page vist them and trim any fragments then add to a set of visited links.
  * Then call crawl() on any unvisited links

## Phase 3: Implementation *(15%)*

**Deliver:**

* Need to understand Try/Except blocks better but got it working
* Need more practice with recursion because I over think it but it is elagent


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

* Checked that duplicates are not getting "clicked"
* Checked that exceptions are being handled gracefully
* Wasn't visiting all the links found, fixed some logic so that is the case now

## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

* I feel like the main body of the program could be cleaned up a bit, as well as I could understand the 3rd partyl
libraries better as well
* Shouldn't take long to find any bugs since the program is pretty small and straight forward
* Documentation is clear and easy to understand and should be easy to add new functionality to the program if needed to
in the future
* There should be no issues with the program when upgrading hardware, OS, or new version of Python.
