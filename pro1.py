a=input()
for i in range(1, int(a)+1):
    x = ""
    x = x + str(i)
    if(i%3==0) :
        x = x + "Fizz"
    if(i%5==0) :
        x = x + "Buzz"
    print(x)
        