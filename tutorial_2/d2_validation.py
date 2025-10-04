email = "arun.kumar@gmail.com"
# email = "arun_kumar_gmail.com"
# email = "arun@kumar.gmail.com"
# email = "@arun_kumar_gmail.com"
# email = "arun_kumar_gmail.com@"
# email = "arun@kumar@gmail.com"
# email = "arun.kumar@gmail"

if "@" not in email:
    print("Invalid email: '@' is missing")
elif email.count('@')>1:
    print("Invalid email: More than 1 '@' found")
elif email.startswith('@'):
    print("Invalid email: 'Starts with '@' is wrong")
elif email.endswith('@'):
    print("Invalid email: 'Ends with '@' is wrong")
elif "." not in email:
    print("Invalid email: '.' is missing")
elif email.startswith('.'):
    print("Invalid email: 'Starts with '.' is wrong")
elif email.endswith('.'):
    print("Invalid email: 'Ends with '.' is wrong")
else:
    indexOfAt = email.index('@')
    domain = email[indexOfAt:]
    print(domain)
    if "." not in domain:
        print("Invalid email: '.' is missing in domain")
    # after @ first char can not be .
    else:
        print("Valid email")