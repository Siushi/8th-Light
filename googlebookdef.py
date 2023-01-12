import requests

api_key = 'Your API key'

#
def viewList(reading_list):
  print('Reading list:')
  for i, book in enumerate(reading_list):
    print(f'{i+1}. {book["title"]} by {book["authors"]} ({book["publisher"]})')

def searchBooks(query):
  while True:
    if query == "":
      print("Invalid query, please enter a valid query: ")
      query = input()
    else:
      # Send a request to the Google Books API to search for books
      url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
      response = requests.get(url)
      if response.status_code != 200:
        print("Invalid query, please enter a valid query: ")
        query = input()
      else:
        return response.json()

def displayBookResults(results):
  # If reutrn none
  items = results.get('items', [])
  if not items:
    return True 
  # If more then 5
  if len(items) >= 5:
    items = items[:5]

  # Display a list of 5 books matching the query
  for i, item in enumerate(items):

    volume_info = item['volumeInfo']
    title = volume_info['title']
    
    # Check if the book has an authors field
    if 'authors' in volume_info:
      authors = volume_info['authors']
      
      # Join the list of authors into a single string
      authors = ', '.join(authors)
      
      # Remove syntax from the authors field
      authors = authors.replace('[', '').replace(']', '')
    else:
      authors = ''

    # Check if the book has an publisher field
    if 'publisher' in volume_info:
      publisher = volume_info['publisher']
    else:
      publisher = ''
    
    print(f'{i+1}. Title: {title}')
    print(f'   Authors: {authors}')
    print(f'   Publisher: {publisher}')

def addBook(results, selection, reading_list):
  # Add the selected book to the reading list
  selected_book = results['items'][int(selection) - 1]
  volume_info = selected_book['volumeInfo']
  title = volume_info['title']
  if 'authors' in volume_info:
    authors = volume_info['authors']
  else:
    authors = '*NA*'
  if 'publisher' in volume_info:
    publisher = volume_info['publisher']
  else:
    publisher='*NA*'
  reading_list.append({
    'title': title,
    'authors': authors,
    'publisher': publisher
  })
  return reading_list
