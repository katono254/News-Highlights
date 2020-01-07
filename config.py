import os
class Config:
 
  NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey={8de60e91c78943d2bba5cf8a13cdbe5a}'
  ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={8de60e91c78943d2bba5cf8a13cdbe5a}'
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
