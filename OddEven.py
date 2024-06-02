print("Program to display Odd number in the given range")

lower= int(input("Enter lower limit: "))
upper= int(input("Enter upper limit: "))

for item in range(lower,upper+1):
    if item%2 != 0:
        print(item)
