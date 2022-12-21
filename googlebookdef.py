import requests

api_key = 'API KEY HERE'

#
def viewList(reading_list):
  print('Reading list:')
  for book in reading_list:
    print(f'{book["title"]} by {book["authors"]} ({book["publisher"]})')

def searchBooks(query):
  # Send a request to the Google Books API to search for books
  url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
  response = requests.get(url)
  return response.json()

def displayBookResults(results):
  # Display a list of 5 books matching the query
  for i, item in enumerate(results['items'][:5]):

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
