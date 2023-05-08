



#-----------------------------------------
#----- Practical Email Slicing-------
#------------------------------------------



email = "Salar_issa@gmail.com"

print(email[0]) # S # index() 
print(email[0:5]) # salar # Slicing
print(email.index("@")) # 10 
print(email[0:email.index("@")]) # Salar_issa
print(email[:email.index("@")]) # Salar_issa



print("#" *50) # ##################################################



theName = input("what is your Name : ").strip().capitalize() #  # Hello Salar Your Email is issa.salar321@gmail.com
theEmail = input("what is your Email : ").strip() # issa.salar321@gmail.com
theUsername = theEmail[:theEmail.index("@")] # issa.salar321
theWebsite = theEmail[theEmail.index("@") +1:] # gmail.com



print(f"Hello {theName} Your Email is {theEmail}") # Hello salar Your Email is issa.salar321@gmail.com 
print(f" your Username Is {theUsername} and Your Website is ")  #  your Username Is issa.salar321 and Your Website is
print(f" your Username Is {theUsername}  and Your Website is {theWebsite} ") #   your Username Is issa.salar321 and Your Website is gmail.com 













