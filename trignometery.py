p=int(input("Enter the perpendicular"))
b=int(input("Enter the base"))
h=int(input("Enter the hypotenuse"))
func=input("Which trignometric function do you want to use here? i.e. sin , cos or tan?")
if func==("sin"):
    print(p/h)
elif func==("cos"):
    print(b/h)
elif func==("tan"):
    print(p/b)
