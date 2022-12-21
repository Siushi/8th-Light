from googlebookdef import *

reading_list = []

while True:
  query = input('Enter a query (or enter "l" to view the current reading list): ')
  
  if query == 'l':
    # View the reading list
    viewList(reading_list)
    continue

  results = searchBooks(query)

  displayBookResults(results)  

  while True:
    # Prompt the user to select a book to add to the reading list
    selection = input('Enter which # of book to add to the reading list (or enter "q" to quit): ')
    
    # Check if the input is a digit and in the range 1-5
    if selection.isdigit() and 1 <= int(selection) <= 5:
      # The input is a valid number in the range 1-5
      reading_list = addBook(results, selection, reading_list)
      break
    elif selection == 'q':
      break
    else:
      # The input is not a valid number in the range 1-5
      print('Invalid input. Please try again.')

  if selection == 'q':
    break

# View the reading list
viewList(reading_list)