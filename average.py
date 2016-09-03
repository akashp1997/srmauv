average = 0
count = 0
while True:
    choice = raw_input("Do you wanna continue(y/n)? ")
    if choice.lower()=="y":
        break
    num = raw_input("Enter the number: ")
    count += 1
    average += (average*count+num)/count
    
