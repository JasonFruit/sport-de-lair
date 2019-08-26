import os

for p in range(1, 458):
    ps = repr(p)
    ps = (3 - len(ps)) * "0" + ps
    os.system("convert p%s.JPG p%s.pdf" % (ps, ps))
    
os.system("pdftk *.pdf cat output sport-de-lair.pdf")
