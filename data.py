def spaces(n,y,t):
    count = 0
    for i in range (n):
        if y[i] == "C" and t[i] == "C":
            count += 1
    print(count)

spaces(5,"CC..C",".CC..")
