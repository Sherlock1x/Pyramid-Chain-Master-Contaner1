

#File timer.py
""""""
Homegrown timing tools for function calls.
Does total time,best of time,and best of total time.
""""""
import time sys
timer=time.clock if sys.platform[:3]=='win'else time.time
def total(reps,func,*pargs,**kargs):
    """"""
    Total time to run func()reps times
    Return(total time,last results)
    """"""
    repslist=list(range(reps))  #Hoist out equalize 2x,3x
    start=timer()               #Or perf__counter/other in 3.3+
    for i in repslist:
        ret=func(pargs.**kargs)
    elapsed=timer()-start
    return(elapsed,ret)
def best of(reps,func,*pargs,*pargs,**kargs):
    """"""
    Quickest func()among reps runs.
    Return(best time,last results)
    """"""
    best=2**32                    #136 years seems large enough
    for i in range(reps)          #range usage not times here
    start=timed()
    ret=func(*pargs,**kargs)
    elapsed=timer()-start         #Or call total()with reps=1
    if elapsed < best:best=elapsed
return(best,ret)                  #Or add to list and take min()
def best of total(reps1,reps2,func,*pargs,**kargs):
    """"""
    Best of totals:
    (best of reps1 runs of(total of reps2 run of func))
    """"""
    return best of(reps1,total,reps,func,*pargs,**kargs)
    
 import timer                                    #Pg.632
 timer.total(1000,pow,2,1000)[0]
 #  0.0029542985410557776
 timer.total(1000,str.upper,'spam')
 #  (0.000050484531709686, 'SPAM')
 timer.bestof(1000,str.upper,'spam')
 #  (4.88717702751273350-07,'spam')
 timer.bestof(1000,pow,2,10000)[0]
 #  0.00393515497972885
 timer.bestof(50,timer,total,1000,str.upper,'spam'))
 #  (0.00054687514577,(0.0005004469323637295)
 timer.bestoftotal(50,1000,str.upper,'spam')
 #(0.000566912540591600,(0.0005195069228989269,'SPAM'))
 
 min(timer.total(1000,str.upper,'spam')for i in range(50))   #Pg.633
 #(0.0005155971812769167,'SPAM')
 
