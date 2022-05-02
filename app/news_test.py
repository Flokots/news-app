import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the News Class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_news = News(1234, "Flask Has Evolved", "A thrilling article on the evolution of Flask", "https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/PZDEVWWJ6QI6ZN7OOTYJ3AT4UY.jpg&w=1440")

  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_news, News))



if __name__ == '__main__':
  unittest.main()