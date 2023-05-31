
websites = [] #creates an empty list called websites    
usernames = [] #creates an empty list called usernames
passwords = [] #creates an empty list called passwords
while True: #forever loop
    entry = input("Do you want to add an entry? yes/no: ") #asks user if they want to add website, username and password 

    if entry == "no": #if user does not want to add an entry
        break #stop the loop
    elif entry == "yes": #if user wants to add an entry
        website = input("enter website name") #prompts user to enter name of desired website
        websites.append(website) #adds the website to the websites list
        username = input("enter desired username") #prompts user to enter desired username
        usernames.append(username) #adds the username to the username list
        password = input("enter desired password") #prompts user to enter desired password
        passwords.append(password) #adds the password to the password list
    else:#if user types in anything other than "yes" or "no"
        print("Invalid") #tell user this is an "invalid" response

    #iterate through all the possible indexes in the websites list and for each do the following
    for index in range(len(usernames)): 
        print(f"website {index + 1 }: {websites[index]}") #print name of website at specified index
        print(f"username {index + 1}: {usernames[index]}") #print username at specified index
        print(f"password {index + 1}: {passwords[index]}") #print password at specified index