n=int(input("enter the size"))
a=dict()
for i in range(n):
  key=input("enter the key value of " + str(i+1) + " of dictionary")
  value=input("enter the value of " + str(i+1) + " of dictionary")
  a[key]=value

print("second largest number in dictionary is ",list(sorted(a.values()))[-2])

