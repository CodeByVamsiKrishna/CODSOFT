# history  = []
def save_history(result):
    with open("history.txt","a")as file:
        file.write(result +"\n")
while True:
    all_operations = [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Modulus",
        "Square",
        "Square root",
        "View history",
        "Clear history",
        "Exit"
    ]
    count= 0
    for task in all_operations:
        count+=1
        print(count,task)
    selected_operation = (input("Enter number to select the operation : "))
    if selected_operation == "1":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        soln = (f"{add_1} + {add_2} = {add_1+add_2}")
        print(soln)
        # history.append(soln)
        save_history(soln)
    elif selected_operation == "2":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        soln = (f"{add_1} - {add_2} = {add_1-add_2}")  
        print(soln)
        # history.append(soln)
        save_history(soln)

    elif selected_operation == "3":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        soln = (f"{add_1} x {add_2} = {add_1*add_2}")
        print(soln)
        # history.append(soln)
        save_history(soln)
    elif selected_operation == "4":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        if add_2 == 0:
            print("Division with zero isn't possible, Run again !")
            continue
        soln = (f"{add_1} / {add_2} = {add_1/add_2}")
        print(soln)
        # history.append(soln)
        save_history(soln)
    elif selected_operation == "5":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter the power : "))
        if add_2 >100:
            print("NUmber too large ")
            continue
        soln = (f"{add_1} ** {add_2} = {add_1**add_2}")
        print(soln)
        # history.append(soln)
        save_history(soln)
    elif selected_operation == "6":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        if add_2 == 0:
            print("Modulus with zero isn't possible, Run again !")
            continue
        soln = (f"{add_1} % {add_2} = {add_1%add_2}")
        print(soln)
        # history.append(soln)
        save_history(soln)
    elif selected_operation == "7":
        add_1=int(input("Enter the number : "))
        soln  = (f"The square =  {add_1**2}")
        print(soln)
        # history.append(soln)
        save_history(soln)
    elif selected_operation == "8":
        add_1=int(input("Enter the number : "))
        soln = (f"The square root = {add_1**0.5}")
        print(soln)
        # history.append(soln)
        save_history(soln)
    elif selected_operation == "9":
        with open("history.txt","r")as file:
            content =file.read()
        if content==" ":
            print("History not found !")
        else :
                print(content)
    elif selected_operation == "10":
        # history.clear()
        with open("history.txt","w")as file:
            pass
        print("History deleted !")
    elif selected_operation == "11":
        print("Thank you for using calculator !")
        break
    else :
        print("Invalid Choice,Try again with suitable options")
        






