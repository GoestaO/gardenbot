import sys
import app
sys.stdout = sys.stderr
 
sys.path.append('/var/www') 
sys.path.append('/var/www/gardenbot')
 
from main import app as application

