from inspect import isdatadescriptor


class News:
  '''
  News class to define News Objects
  '''

  def __init__(self, id, name, author, title, description, url, urlToImage, time):
    
    self.id = id 
    self.name = name
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.time = time
