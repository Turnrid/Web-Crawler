# CS 1440 Assignment 5 Rubric

| Points | Criteria
|:------:|-----------------------------------------------------------------------------------------------------------
| 25pts | Software Development Plan is comprehensive and well-written <br/>DuckieCorp project conventions are followed
| 5pts | `Signature.md` is filled out correctly & repo is clone of starter code
| 5pts | All 5 git tags (analyzed, designed, implemented, tested, deployed) are present
| 10pts | User Manual explains how to run the crawler program.<br/>Written for an end-user, not a programmer (like a board game manual)
| 15pts | User interface meets requirements<br/>Format of output meets requirements (correct indentation)<br/>Runtime duration and count of visited sites are printed to STDERR when crawler exits;  both invalid and valid input are handled
| 10pts | Exception Handling protects the crawler from crashing when encountering invalid/uncooperative sites or other problems<br/>Program gracefully exits upon receipt of KeyboardInterrupt exception<br/>Catch other exceptions, display an error message, and continue on to the next URL<br/>DO NOT PENALIZE FREEZING/HANG UPS on broken websites
| 15pts | `crawl()` is a recursive function and is implemented such that it meets requirements (visit URLS once, etc.)

**Total points: 85**


## Penalties
**IMPORTANT NOTE: This assignment is *not* eligible for the grading gift.  This due date cannot be moved.**

*Please read the "How To Submit Assignments" page of Canvas (found under the DuckieCorp Employee Handbook Module) for more information on these penalties and what we expect.*

***Penalties for this assignment***:

0.  **85 point penalty** if your program imports any modules **except**:
    *   `sys`
    *   `time`
    *   `requests`
    *   `bs4` specifically `BeautifulSoup`
    *   `urllib.parse` specifically `urlparse` and `urljoin`
    *   modules that are provided by the starter code
    *   or modules you wrote yourself
    *   This assignment is about the experience of solving this puzzle for yourself without leaning on code written by others, no matter how "real-world" it would be to do so.
1. `ModuleNotFoundError`s count as crashing code, as they indicate imports of libraries that are not allowed.
2.  **10 point penalty** if a `print("TODO...")` statement is left inside of the program
    * This becomes a **20 point penalty** if the `print("TODO...")` statement is inside crawl and prints more than once.

***Penalties for all assignments***:

#### Project Layout
0. **10 point penalty** if the repository does not follow the Git Repository Naming Convention
1. **10 point penalty** if the submitted project is not a clone of the starter code repository.
2. **10 point penalty** if there is an omission of required files and directories (missing, renamed, or moved from their expected location)
3. **10 point penalty** if there are forbidden files and directories in the submission
4. **10 point penalty** if there is no `.gitignore` file (whether it is missing or corrupted)
5. **Late Penalty**:
    *   \<24hrs late = -25% total points
    *   \>=24hrs & <48hrs = -50% total points
    *   \>=48hours = -100% total points

#### Modules and Functions
0. **10 point penalty** if a module fails to import due to misspelling or incorrect capitalization.
1. **10 point penalty** if the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
2. **10 point penalty** `eval()` or a similar function is used by your program; use type constructor functions such as `int()` and `float()` instead
3. **\<Varies\> point penalty** A library which the grader doesn't happen to have installed is imported; The resulting `ModuleNotFoundError` is treated as a crash and penalized accordingly
4. **20 point penalty** A library not permitted by the instructions is used, but doesn't result in a crash

#### Files and Paths
0. **10 point penalty** if the program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
1. **10 point penalty** if one or more data files are not closed after being processed in *ordinary* situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they will automatically be closed as your program exits.
2. **100% point penalty** if external programs are called upon to do the work.  Our customer has hired you to create a pure-Python solution, not a shell script that relies on external programs.
    - Do not use `os.system()`, `subprocess`, `pipes` or similar functions and libraries
    - Write a pure Python solution, not a script that leverages external programs

#### All Else
0. **Crashing Code Penalty**:
    * *Reminder: it is your responsibility to test and ensure that your program works on the graders computer*
    *   Code that is crashing and cannot be quickly & easily fixed by the grader will receive a 0% point cap penalty on the implementation portion of the rubric (0 points on implementation)
    *   Code that is crashing and CAN be quickly & easily fixed by the grader (or is only crashing some of the time) will receive a 50% point cap penalty on the implementation portion of the rubric
    * `ModuleNotFoundError`s count as crashing code, as they indicate imports of libraries that are not allowed.
