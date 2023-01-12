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

Edits 1/11/23 per feedback
Some problematic inputs cause the app to crash, like " " or submitting blank input
	Forces users to enter valid input loops until

What would happen if the API returns fewer than five items? Or no items at all (in the case that api call returned an error)?
	if less then 5 will display all. No items will say no items try again and invalid will say invalid

It would be great to see some tests which handle these cases which cause the app to crash, testing the sad paths as well as the happy path.
	Created test that test sad path but program should not crash I believe. Didn't bother to add a sad test for addBook as it will never be called unless it has proper inputs

Also, once you make a query, you cannot make another query without adding a book to the reading list or quitting. Is there a way to refactor so that you can make another request without having to quit the program or add to the reading list
	Refactor the code so that there are more choices in the start and still shows list at the end