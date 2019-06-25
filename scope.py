def a_func():

    a = 5

    def inner_func():
        a = 3
        print('inner_func has ran')
    
    
    
    inner_func()
    print(a)

    print('a func has ran')
    

    




#a_func()
 #print a_func  

# after function runs, when you leave the scope you lose the given value, and the value changes depending on code block

#counter = 0
#while counter < 25:
#    print(counter)
#    counter += 1
#counter +=10
#print(counter)



#def login():
   # while True:
   #     username = input('Username: ')
   #     password = input('Password: ')
   #     if username == 'Justing':
  #          if password == 'password':
 #               return username


#user = login()
#print(user)

#do not use global 
#allows you to point to outer scopes


def login():
    while True:
        username = input('Username: ')
        password = input('Password: ')
        if username == 'Justin':
            if password == 'password':
                return username
                
                
# user = login()
# print(user)
