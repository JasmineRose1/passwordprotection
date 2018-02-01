#always define functions at the top if you're using functions

#def password():
#    password = raw_input("Enter password")
#    user_password = password.lower()
#    user_input = raw_input("Enter password.") #prompt user with raw input function

#    while(user_input!=user_password):
#        user_input=raw_input("Incorrect password, try again: ")


#    user_input = user_input.lower()

#using a while loop incase they get the password wrong

def password():
        password = raw_input("Enter a password: ")
        user_password = password.lower()
        user_input = raw_input("Enter password: ")
        user_input = user_input.lower()
        attemps = 1
        while(user_input!=user_password):
            user_input=raw_input("Incorrect password, try again: ")
            attempts +=1
            if attempts == 3:
                print "locked out"
                break
        if user_password==user_input:
                print "correct password"
        return None

password()
