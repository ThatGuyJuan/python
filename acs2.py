#asc2.py cwc
for i in range (32,127):
    c = chr(i)
    print("[",i,"=",c,"]",end="")
    if (i % 5 == 0):
        print()
