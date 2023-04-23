import time


bar = [
    " [=     ]",
    " [ =    ]",
    " [  =   ]",
    " [   =  ]",
    " [    = ]",
    " [     =]",
    " [    = ]",
    " [   =  ]",
    " [  =   ]",
    " [ =    ]",
]
i = 0

for i in range():
    print(bar[i % len(bar)], end="\r")
    time.sleep(.2)
    i += 1