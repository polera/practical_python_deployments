import sys; sys.path.insert(0,'/var/www/nameparts')
activate_this = '/home/james/.virtualenvs/pugip/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from app import app as application