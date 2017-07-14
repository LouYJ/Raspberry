phonebook = {"Admain":123456}
while 1:
    print("You can:")
    print("1.Add new contact")
    print("2.Edit an exit contact")
    print("3.Lookup a contact")
    print("Please input your choice:")
    a = input()
    n = int(a)
    
    if (n == 1) :
        print("Please input the name:")
        name = input()
        print("Please input the phone number:")
        num = input()
        phonebook[name] = num
        
    elif (n == 2) :
        print("Please input the name you want to edit:")
        name = input()
        print("Please input the new phone number:")
        num = input()
        phonebook[name] = num
        
    elif(n == 3) :
        print("Who do you want to lookup:")
        name = input()
        print(phonebook[name])
  
        
        