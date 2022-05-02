from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''

  # Getting Top Headlines News
  top_headlines = get_news('top-headlines')
  print(top_headlines)
  title = "The Nightngale News App"
  return render_template('index.html', title = title, top_headlines = top_headlines)


@app.route('/news/<id>')
def news(id):
  '''
  View news page function that returns the news articles pages and its data
  '''

  return render_template('news.html', id=id)