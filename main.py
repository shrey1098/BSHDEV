from BSHDEV.wsgi import application as app
import os

def env_vars(request):
    return os.environ.get('TEXT_ANALYTICS_SUBSCRIPTION_KEY', 'Specified environment variable is not set.')
  
