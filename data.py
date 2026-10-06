# """ def spaces(n,y,t):
#     count = 0
#     for i in range (n):
#         if y[i] == "C" and t[i] == "C":
#             count += 1
#     print(count)

# spaces(5,"CC..C",".CC..") """



# """ def language(N,sentence):
#     for i in range(N):
#         if "T" + "t" > "s" + "S":
#             print("English")
#         if "s" + "S" > "t" + "T":
#             print("French")
#         if "s" + "S" == "t" + "T":
#             print("French")


# def N(numbers):
#     input (numbers):("0<N<10000")

# N("The red cat sat on the mat. Why are you so sad cat? Don't ask that.") """


# x = (float(input("How much is the Bill?")))
# tip = [1.0 , 1.2 , 1.25, 2.0]

def wizards(N,start,duels):
    owner = start
    changed_hands = 1
    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
            changed_hands += 1
    print(owner, changed_hands)





wizards(3, "A", ["BA", "CB", "DA"])
