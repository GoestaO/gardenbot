import sys
sys.stdout = sys.stderr
 
sys.path.append('/var/www') 
sys.path.append('/var/www/gardenbot-api')
 
from run_api import app as application
