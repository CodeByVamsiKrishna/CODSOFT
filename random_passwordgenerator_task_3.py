import random
characters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K",
    "L","M","N","O","P",'Q',"R","S","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","?","+","-","_","<",">",",",".","1","2","3","4","5","6",
    "7","8","9","`","~"
    ]
history = []
while True :

    available_options = [
    "Generate password",
    "Check Password Strength",
    "View History",
    "Clear History",
    "Exit"
]
    count = 0
    for task in available_options:
        count+=1
        print(count,task)
    option_selection =(input("Select the option :"))
    if option_selection == "1":
        password=""
        password_length = int(input("Enter the password length : "))
        for i in range(0,password_length):
            choosen_character = random.choice(characters)
            password = password + choosen_character
        print("Created Password is : ", password)
        history.append(password)
    elif option_selection == "2":
        user_password=input("Enter your password : ")
        upper = 0
        lower =0
        number = 0
        special_character=0
        for char in user_password:
            if char.isupper():
                upper+=1
            elif char.islower():
                lower+=1
            elif char.isdigit():
                number+=1
            else:
                special_character+=1
        if len(user_password) >=12 and upper >0 and lower >0 and number >0 and special_character >0:
            print("Strong Password !")
        elif len(user_password)>= 8 and upper >0 and lower >0 and number >0:
            print("Medium Password ! ")
        else :
            print("Weak Password ! ")
    
    elif option_selection == "3":
        count2 =count=0
        for task in history:
            count2+=1
            count+=1
            print(count2,task)
        if count == 0:
            print("History is empty")
    elif option_selection == "4":
        history.clear()
        print("History Cleared !! ")
    elif option_selection == "5":
        print("Thanks for using Password Generator ! ")
        break
    else :
        print("Invalid Choice !! ")

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
