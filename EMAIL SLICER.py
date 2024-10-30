#EMAIL SCILER ....


emailId = input("Enter the email id: ")

username = emailId[ :emailId.index('@')]

domain  = emailId[emailId.index('@')+1: ]

print("Username = " , username)
print("Domain name = " , domain)

