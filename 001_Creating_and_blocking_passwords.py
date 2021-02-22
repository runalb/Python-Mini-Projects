password = "1234"
your_answer = ""
no_of_trays = 0
no_of_max_trays = 3
max_try = "not reched"

while your_answer!=password and max_try!="reached":
    if no_of_trays < no_of_max_trays:
        your_answer = input("Enter password:")
        no_of_trays = no_of_trays + 1
    else:
        max_try = "reached"

if max_try == "reached" :
    print("Account locked!, Max try:", no_of_max_trays )

else:
    print("Login succesfully")
