import sys
n=int(sys.argv[1])
count=1
rem=1
#exhaust all 1,11,111,1111,11111,etc... to match a number can be divided by n
while rem > 0:
    rem= (rem*10+1)%n
    print("new rem", rem)
    count+=1
while count > 0:
    print("1")
    count -= 1
