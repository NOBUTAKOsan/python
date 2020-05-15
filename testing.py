from Data.Access.UserAccess import UserAccess

userAccess = UserAccess()
user = userAccess.GetUser(3)
print(user.username)


userAccess.DeleteUser(3)

for usr in user:
    print(usr.username)