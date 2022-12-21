All the function are in googlebookdef and to run the program run googlebookrun.py

Removed my api key as I don't want it to be stolen

There are unit test to make sure my function are working properly

Thought process:<br />
First get an api key from google dont upload the api key<br />
Try a get request online to see what the json returns so I can break it down create that object<br />
Define a searchbook that takes a query and return a list of books <br />
Create a main loop in a different file because the test calls the main loop if they are in the same file<br />
Lets the user choice a book from the list of books and add it to the list<br />
Lets the user view the list any time <br />
After quitting prints out the list the user made<br />

Quality:<br />
Remove "" and [] from the author list

EdgeCases:<br />
Some books don't have authors<br />
Some books don't have publishers <br />
Some books could have more then 1 author<br />

If the user choices more then 5 it will grab it. Need to limit user to 1-5
