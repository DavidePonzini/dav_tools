from time import sleep

from dav_utils_DAVIDE_PONZINI import messages


messages.message('downloading data...', icon=' ', end='\r')
sleep(1)
messages.message('slow network', icon=' ', end='\r')
sleep(2)
messages.info('downloaded')
messages.message('downloading data...', icon=' ', end='\r')
sleep(1)
messages.message('slow network', icon=' ', end='\r')
sleep(2)
messages.info('downloaded')