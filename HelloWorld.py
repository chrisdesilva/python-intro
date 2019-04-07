parrot = "Norwegian Blue"
print(parrot[3])
age = 24
print("My age is " + str(age) + " years old")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}".format(31, "January", "March", "May", "July", "August", "October", "December"))

for i in range(1, 12):
    print("{0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.50}".format( 22 / 7 ))