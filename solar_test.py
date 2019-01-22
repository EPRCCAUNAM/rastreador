from datetime import datetime
import solarPos
import math
from datetime import timedelta

dtime = datetime(2015, 2,19,8,0,0)
i=0
while(i<=5):
    atime=dtime+timedelta(hours=i*2)
    sol = solarPos.solarPos(19.4, -99.149999, atime, -6)
    print '*'*40
    print atime, math.degrees(sol.lon), math.degrees(sol.lat), sol.tzone
    print 'eq_time:',sol.eq_time
    print 'decl:',math.degrees(sol.decl)
    print 'az:',math.degrees(sol.az)
    print 'el:',math.degrees(sol.el)
    i+=1
