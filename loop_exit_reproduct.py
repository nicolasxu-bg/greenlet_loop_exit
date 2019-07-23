import gevent
import time

def idler1():
	while True:
		print ('idler1 working...')
		time.sleep(3)
		g1.kill()

def idler2():
	while True:
		print ('idler2 working...')
		gevent.sleep(1)

g1 = gevent.Greenlet(idler1)
g1.start()

# g2 = gevent.Greenlet(idler2)
# g2.start()

g1.switch() # will trigger the whole thing
# without g2(the 2nd greenlet), g1.kill() will trigger an LoopExit error.

# To fix the error, uncomment line 18 and 19
