history  = []
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
        history.append(soln)
    elif selected_operation == "2":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        soln = (f"{add_1} - {add_2} = {add_1-add_2}")  
        print(soln)
        history.append(soln)
    elif selected_operation == "3":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        soln = (f"{add_1} x {add_2} = {add_1*add_2}")
        print(soln)
        history.append(soln)
    elif selected_operation == "4":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        if add_2 == 0:
            print("Division with zero isn't possible, Run again !")
            break
        soln = (f"{add_1} / {add_2} = {add_1/add_2}")
        print(soln)
        history.append(soln)
    elif selected_operation == "5":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter the power : "))
        soln = (f"{add_1} ** {add_2} = {add_1**add_2}")
        print(soln)
        history.append(soln)
    elif selected_operation == "6":
        add_1=int(input("Enter 1st number : "))
        add_2=int(input("Enter 2nd number : "))
        if add_2 == 0:
            print("Modulus with zero isn't possible, Run again !")
            break
        soln = (f"{add_1} % {add_2} = {add_1%add_2}")
        print(soln)
        history.append(soln)
    elif selected_operation == "7":
        add_1=int(input("Enter the number : "))
        soln  = (f"The square =  {add_1**2}")
        print(soln)
        history.append(soln)
    elif selected_operation == "8":
        add_1=int(input("Enter the number : "))
        soln = (f"The square root = {add_1**0.5}")
        print(soln)
        history.append(soln)
    elif selected_operation == "9":
        count=0
        if len(history)==0:
            print("History not found !")
        else :
            for task in history:
                count+=1
                print(count,task)
    elif selected_operation == "10":
        history.clear()
        print("History deleted !")
    elif selected_operation == "11":
        print("Thank you for using calculator !")
        break
    else :
        print("Invalid Choice,Try again with suitable options")
        






