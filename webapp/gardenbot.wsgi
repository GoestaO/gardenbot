import sys
sys.stdout = sys.stderr
 
sys.path.append('/var/www') 
sys.path.append('/var/www/gardenbot')
 
from app import app as application

