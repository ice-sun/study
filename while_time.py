#!/usr/bin/python
import time
count = 0
run_forever = True
while run_forever:
    count += 1
    print 'loop ',count
    if count == 3:
        run_forever = False
        # break
    time.sleep(2)