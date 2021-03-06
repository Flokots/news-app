import unittest
from app.models import NewsSource

class NewsTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the News Class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    
    self.new_news = NewsSource("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")
  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_news, NewsSource))


  def test_init(self):
    '''
    test_init case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_news.id, "abc-news")
    self.assertEqual(self.new_news.name, "ABC News")
    self.assertEqual(self.new_news.description, "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
    self.assertEqual(self.new_news.url, "https://abcnews.go.com")
    self.assertEqual(self.new_news.category, "general")
    self.assertEqual(self.new_news.language, "en")
    self.assertEqual(self.new_news.country, "us")
