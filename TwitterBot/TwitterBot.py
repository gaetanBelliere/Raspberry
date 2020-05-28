##########################################################################
# Tutorial from online, can be found here :                              #
# https://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/ #
##########################################################################

import sys
from twython import Twython

CONSUMER_KEY    = ''
CONSUMER_SECRET = ''
ACCESS_KEY      = ''
ACCESS_SECRET   = ''

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])

# TO BE CONTINUED