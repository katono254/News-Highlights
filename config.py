import os
class Config:
 
  NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=e8a9d0bb58934634b414124d91ef3e5c'
  ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources=abc-news&apiKey=e8a9d0bb58934634b414124d91ef3e5c'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  @staticmethod

  def init_app(app):
        pass
          
class ProdConfig(Config):

    pass 

class DevConfig(Config):
    DEBUG = True 

config_options = {
'development':DevConfig,
'production':ProdConfig

}       
