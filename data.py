# """ def spaces(n,y,t):
#     count = 0
#     for i in range (n):
#         if y[i] == "C" and t[i] == "C":
#             count += 1
#     print(count)

# spaces(5,"CC..C",".CC..") """



def language(N,sentence):
    for i in range(N):
        if "T" + "t" > "s" + "S":
            print("English")
        if "s" + "S" > "t" + "T":
            print("French")
        if "s" + "S" == "t" + "T":
            print("French")


def N(numbers):
    input (numbers):("0<N<10000")

N("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")