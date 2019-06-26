import soco
from soco.discovery import by_name
from time import sleep
from random import randint

dr = by_name("Dining Room") 
print(dr.player_name)

while True:
    dr.play()
    s = randint(20,35)
    print('sleeping {}'.format(s))
    sleep(s)
    dr.pause()
    input('>')
    dr.next()
