#Loyola, Reylene Grace A.
#IT3C
#WEEK 13 Addition Functions

def calculateSumOfRange(start, end):
    sumTotal = 0
    for num in range(start, end + 1):
        sumTotal += num
    return sumTotal

def addition(sum1, sum2, sum3):
    print("The sum of integers from 1 to 10 is {}".format(sum1))
    print("The sum of integers from 20 to 37 is {}".format(sum2))
    print("The sum of integers from 35 to 39 is {}".format(sum3))

sum1 = calculateSumOfRange(1, 10)
sum2 = calculateSumOfRange(20, 37)
sum3 = calculateSumOfRange(35, 39)

addition(sum1, sum2, sum3)



