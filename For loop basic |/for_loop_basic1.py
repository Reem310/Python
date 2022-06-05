for x in range(151):
    print(x)

for x in range(5, 1000):
    x=x*5
    print(x)

for x in range(1, 101):
    if x % 10 == 0:
        print("Coding")
    elif x % 5 == 0: 
        print("Coding Dojo");
    else:
        print(x)

sum=0
for x in range(0, 500000):
    if x % 2 == 1:
        sum+=x
print(sum)

for x in range(2018,0, -4):
    print(x)

lownum=2
highnum=10
for x in range(lownum, highnum):
    if x % 3 == 0:
        print(x)
        