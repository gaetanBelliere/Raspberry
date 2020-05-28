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

if sys.argv[1] != None:
	tweet = sys.argv[1]
else:
	tweet = "It's a long way to the top, if you wanna Rock'N'Roll"
api.update_status(status=)

# TO BE CONTINUED