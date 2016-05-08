


#Timing Script
#File timeseqs.py "Test the relative speed of iteration tool alternatives"

import sys,timer              #Import timer func 
reps-1000
repslist=list(range(reps))     #Hoist out, list in both 2.x/3.x
def for loop():
    res=[]
    for x in repslist:
        res.append(abs(x))
    return res
def list Comp():
    return[abs(x)for x in repslist]
def mapCall()
    return list(map(abs,repslist))   #Use list()here in 3.x only
  #return map(abs,repslist)
def gen Expr():
    return list(abs(x)for x in repslist)   #List()required to force results
def gen Func():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())                  #List()required to force results
print(sys,version)
for test in(for loop,listComp,mapCall,genExpr,genFunc):
    (best of(total,results))=timer.best of totals(51000test)
print('%-9s':'%.5f'=>[%s...%s]'%'(test.__name__,best of,results[-1]))

##"Timing Results" PartIV Chapter21 Pg.635/1540
"The Benchmarking Interlude"
*Timing Iteration Alternatives*
**Timing Module: Homegrown**

c:\code>c:\python33\python timeseqs.py
3.3.0(v3.3.0)bd8af90ebf2, Sep 29 2012
10:57:17) [MSC v.1600 64bit(AMD64)]

forLoop : 1.33290 = > [0000.9999]
listComp: 0.69658 = > [         ]
mapCall : 0.56483 = > [         ]
genExpr : 1.08457 = > [         ]
genFunc : 1.07623 = > [         ]

return[abs(x) for x in repslist]          #0.69sec  abs=(absolute value)  Pg.636
return[list(abs(x) for x in repslist]     #1.08sec

c:\code>c\python27\python timeseqs.py
2.7.3(default, Apr 10 2012,23:24:47 
[MSC v.1500 64bit (AMD64)]

        : 1.24902 = > [0000.9999]
		: 0.66970
		: 0.57018
		: 0.90339
		: 0.90542
		
c:\code>c:\pypy\pypy-1.9\pypy.exe timeseqs.py
2.7.2(341e3821ff,Jun 07 2010. 15:43:00
[pypy1.0.0 with MSC v.1500 32bit]

        : 0.10106 = > [0000.9999]
		: 0.05629
		: 0.10022
		: 0.17234
		: 0.17519
        
        
