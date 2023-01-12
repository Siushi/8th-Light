from googlebookdef import *

reading_list = []

while True:
  query = input("1: Search for a book\n2: View current list\n3: Quit\nPlease make a selection: ")

  if query =='1': #1: Search for a book
    book = input("Enter a query: ")
    results = searchBooks(book)

    if displayBookResults(results):
      print(f'No results please try again')
      continue

    while True:
      # Prompt the user to select a book to add to the reading list
      selection = input('Enter which # of book to add to the reading list or 0 to skip: ')
      
      # Check if the input is a digit and in the range 1-5
      if selection.isdigit() and 1 <= int(selection) <= 5:
        # The input is a valid number in the range 1-5
        reading_list = addBook(results, selection, reading_list)
        break
      elif selection == '0':
        break
      else:
        # The input is not a valid number in the range 1-5
        print('Invalid input. Please try again.')
  elif query =='2': #2: View current list
    # View the reading list
    viewList(reading_list)
    continue
  elif  query =='3': #3: Quit
    break
  else:
    print("Not a valid choice please try again")

# View the reading list
viewList(reading_list)