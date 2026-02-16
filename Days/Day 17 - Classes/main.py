# To create a class
class User:

    # The __init__ functions is used to initialize or create the starting values for my attributes:
    # self is the actual object that is being initialized
    def __init__(self):
        print("new user being created...")

user_1 = User()
user_1.id = "001"
user_1.username = "Simone"
print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Andrea"
print(user_2.username)


# A better way (even more compact) for creating objects:
class UserNew:

    # Remember that the __init__ function is the constructor
    def __init__(self, user_id, username):
        self.id = user_id  # note that the attribute created is called id and not user_id. It's a good practice to give the same name of the input parameters, so write self.user_id = user_id, but the current way is not wrong
        self.username = username
        self.followers = 0  # I'm setting this attribute as a default
        self.following = 0  # as default

    # I build a method of the class UserNew, it's simply a function :)
    def follow(self, user):
        user.followers += 1
        self.following += 1


# If the __init__ function of the class has input parameters, these are required whenever an object is being created!
user_1 = UserNew("001","Simone")

user_2 = UserNew("002","Andrea")

user_1.follow(user_2)

print(f"{user_1.username} has {user_1.followers} followers")
print(f"{user_1.username} follows {user_1.following} users")

print(f"{user_2.username} has {user_2.followers} followers")
print(f"{user_2.username} follows {user_2.following} users")
