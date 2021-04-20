lst = []
numbers = int(input("How many numbers do you want to enter? "))
for i in range (0,numbers):
  user_input = int(input())
  lst.append(user_input)

x = sorted(lst)[:5]
print (sum(x))