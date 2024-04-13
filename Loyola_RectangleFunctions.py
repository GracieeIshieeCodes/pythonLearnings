#Loyola, Reylene Grace A.
#IT3C
#WEEK 13 Rectangle Functions

def rectangle(m, n):
    print("rectangle({0},{1}) {2}x{3}".format(m, n, m, n))
    for i in range(m):
        print('*' * n)

rectangle(2, 4)
rectangle(4, 6)

