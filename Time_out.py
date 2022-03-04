print('Welcome to Pranker count down time_out')
import time
t=int(65)
#int(input('Enter'))
while t:
    mins, secs=divmod(t,60)
    timer='{:0f}:{:0.1f}'.format(mins, secs)
    print(timer,end="\r")
    time.sleep(1)
    t-=1
    print(t)
    