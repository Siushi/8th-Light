from io import StringIO
import unittest
import unittest.mock as mock
import sys

from googlebookdef import *

class TestviewList(unittest.TestCase):
  def test_viewlist_empty(self):
    # Test the Viewlist function with an empty reading list
    reading_list = []
    expected_output = 'Reading list:\n'

    # Use the StringIO class from the io module to capture the output of the Viewlist function
    captured_output = StringIO()
    sys.stdout = captured_output

    viewList(reading_list)

    # Add an assertion to check that the Viewlist function produces the expected output
    self.assertEqual(captured_output.getvalue(), expected_output)
    
  def test_viewlist_nonempty(self):
    # Test the Viewlist function with a non-empty reading list
    reading_list = [{'title': 'Book 1', 'authors': 'Author 1', 'publisher': 'Publisher 1'}, 
                    {'title': 'Book 2', 'authors': 'Author 2', 'publisher': 'Publisher 2'}]
    expected_output = 'Reading list:\n1. Book 1 by Author 1 (Publisher 1)\n2. Book 2 by Author 2 (Publisher 2)\n'

    captured_output = StringIO()
    sys.stdout = captured_output

    viewList(reading_list)

    # Add an assertion to check that the Viewlist function produces the expected output
    self.assertEqual(captured_output.getvalue(), expected_output)

class TestAddBook(unittest.TestCase):
  def test_add_book(self):
    # Create a sample search result
    results = {
      'items': [
        {
          'volumeInfo': {
              'title': 'Book 1',
              'authors': ['Author 1'],
              'publisher': 'Publisher 1'
            }
        },
        {
          'volumeInfo': {
              'title': 'Book 2',
              'authors': ['Author 2'],
              'publisher': 'Publisher 2'
            }
        },
        {
          'volumeInfo': {
              'title': 'Book 3',
              'authors': ['Author 3'],
              'publisher': 'Publisher 3'
            }
        }
      ]
    }
    reading_list = []

    # Add the first book in the search results to the reading list
    selection = 1
    addBook(results, selection, reading_list)

    # Check if the book was added to the reading list
    self.assertEqual(len(reading_list), 1)
    self.assertEqual(reading_list[0]['title'], 'Book 1')
    self.assertEqual(reading_list[0]['authors'], ['Author 1'])
    self.assertEqual(reading_list[0]['publisher'], 'Publisher 1')

class TestSearchBooks(unittest.TestCase):
  def test_search_books(self):
    # Search for books containing the query "testing"
    query = 'testing'
    results = searchBooks(query)

    # Check if the search returned any results
    self.assertGreater(len(results['items']), 0)

    # Check if the query is present in the title of at least one book
    found = False
    for item in results['items']:
      volume_info = item['volumeInfo']
      title = volume_info['title'].lower()
      if query in title:
        found = True
        break
      self.assertTrue(found)

  def test_search_books_invalid_query(self):
    # Test the searchBooks function with an invalid query
    query = ''
    with mock.patch('builtins.input', side_effect=['valid_query']):
      captured_output = StringIO()
      sys.stdout = captured_output
      results = searchBooks(query)
      # check if the function prompts the user to enter a valid query
      self.assertIn('Invalid query, please enter a valid query: ', captured_output.getvalue())
      self.assertIsNotNone(results)


# Run the test case
if __name__ == '__main__':
  unittest.main()
