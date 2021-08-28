#to find the velocity of electron in n^th orbit
atomic_number= int(input("To find the velocity of an electron please enter the atomic number"))
shell_number=int(input("Enter the shell/orbit number"))
velocity = float(2.18*atomic_number*(10**6))/ shell_number
print("velocity of the given electron is:", velocity, "m/s")
