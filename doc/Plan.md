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

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


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

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.
