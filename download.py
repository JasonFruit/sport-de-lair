from urllib2 import urlopen
from time import sleep

base_url = "http://www.pouguide.org/bouquin/800/pages/p%s.JPG"

def page_url(p):
    ps = repr(p)
    ps = (3 - len(ps)) * "0" + ps
    return base_url % ps

for i in range(501, 601):
    f = urlopen(page_url(i))
    data = f.read()
    open(page_url(i).split("/")[-1], "wb").write(data)
    sleep(1)
