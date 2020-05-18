n=int(input("enter the size of tuple"))
print("Enter the elements of tuple")
arr=[]
for i in range(n):
  arr.append(input())

arr=tuple(arr)
x=input("enter the element whose occurence is to be found")
print("the occurence of the element is ",arr.count(x))
