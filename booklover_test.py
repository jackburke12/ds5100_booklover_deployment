import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # Add a book and test if it is in `book_list`.
        dummy = BookLover("John", "john@gmail.com", "mystery")
        dummy.add_book("test book", 5)
        
        self.assertIn('test book', dummy.book_list['book_name'].values)
        self.assertIn(5, dummy.book_list['book_rating'].values)

    def test_2_add_book(self):
        # Add the same book twice. Test if it's in `book_list` only once.
        dummy = BookLover("John", "john@gmail.com", "mystery")
        dummy.add_book("test book", 5)
        dummy.add_book("test book", 5)
        
        self.assertEqual(dummy.num_books_read(), 1)
        
    def test_3_has_read(self): 
        # Pass a book in the list and test if the answer is `True`.
        dummy = BookLover("John", "john@gmail.com", "mystery")
        dummy.add_book("test book", 5)
                      
        self.assertTrue(dummy.has_read('test book'))
        
    def test_4_has_read(self): 
        # Pass a book NOT in the list and use `assertFalse` to test the answer is `False`.
        dummy = BookLover("John", "john@gmail.com", "mystery")
        dummy.add_book("test book", 5)
                      
        self.assertFalse(dummy.has_read('The Great Gatsby'))
        
    def test_5_num_books_read(self): 
        # Add some books to the list, and test num_books matches expected.
        dummy = BookLover("John", "john@gmail.com", "mystery")
        dummy.add_book("test book", 5)
        dummy.add_book("The Great Gatsby", 7)
        dummy.add_book("Dune", 10)
        dummy.add_book("The Call of the Wild", 9)
        
        self.assertEqual(dummy.num_books_read(), 4)

    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some of them have rating > 3. 
        # Check that the returned books have rating > 3.
        dummy = BookLover("John", "john@gmail.com", "mystery")
        dummy.add_book("test book", 5)
        dummy.add_book("The Great Gatsby", 7)
        dummy.add_book("Dune", 10)
        dummy.add_book("The Call of the Wild", 9)
        dummy.add_book("For what?", 1)
        dummy.add_book("This was bad", 2)
        
        fav_books = dummy.fav_books()

        #.gt() returns a series of booleans that tests if each element is > 3. .all() returns whether all elements of that series are True
        #if all book ratings are higher than 3, the method will return true and assertTrue will pass
        self.assertTrue((fav_books['book_rating'] > 3).all())
        self.assertIn("The Great Gatsby", fav_books['book_name'].values)
        self.assertNotIn("This was bad", fav_books['book_name'].values)
            
if __name__ == '__main__':
    unittest.main(verbosity=3)
