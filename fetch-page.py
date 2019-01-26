import sys
from urllib2 import urlopen
from time import sleep

base_url = "http://www.pouguide.org/bouquin/800/pages/p%s.JPG"

page_num = int(sys.argv[1])

def page_url(p):
    ps = repr(p)
    ps = (3 - len(ps)) * "0" + ps
    return base_url % ps

f = urlopen(page_url(page_num))
data = f.read()
open("%s.jpg" % page_num, "wb").write(data)

