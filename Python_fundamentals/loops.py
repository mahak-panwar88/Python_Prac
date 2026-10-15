#for loop 
# Printing the multiplication table using the loops
n = 10
for i in range(n):
    print(n ,"X",i,"=",n*i)
 # printing the strings of the array in the list
arr = ["Eat", "well", "stay", "well"]
for i in range(len(arr)):
    print(arr[i])
# while loop
n = 0
while(n<5):
    n +=1
    print(n)
# Nested loop
for i in range(1,5):
    for j in range(i):
        print(i,end='')
    print()