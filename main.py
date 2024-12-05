#Teacher' version 
#Ask user to input first number
count = 0
num = input("Give me your first Number: ")

#Repeat until person types q of quit 
while num != "q":
#Convert number to interger
  num = int(num)
  #update number
  count = count + num
  print(num)
#New number
  num = input("Give me another number or enter q to quit: ")

#once quit answer is given
#Convert count into a string
count = str (count)
print("your total is " + count)