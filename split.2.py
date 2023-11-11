han = open("email")
for line in han:
    line =line.rstrip()    
    wds = line.split()

    if len(wds)<3 or wds [0] != "Ella":
     continue
   
     print(wds[2])

