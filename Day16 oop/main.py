from turtle import Turtle, Screen

timmy = Turtle() # I'm constructing an object from the blueprint Turtle (that is a class)
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
my_screen = Screen()

print(my_screen.canvheight)   # canvheight is an attribute of the object
my_screen.exitonclick()  # I call a function of the object (called "method")

from prettytable import PrettyTable
# TODO Create a prettytable object and save it to a variable called table:
table = PrettyTable()

# TODO Calling methods
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

# TODO Calling attributes
table.align = "l" # to access an attribute of table and assign a value to it

print(table)

