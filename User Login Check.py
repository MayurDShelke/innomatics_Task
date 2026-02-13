# 1. User Login Check

username = input("Enter your username:") 
password = input("Enter your Password:") 

if username == "admin" and password =="1234" :
    print("Login Successful")
else:
    print("Invalid Credentials")


# 2. Pass / Fail Analyzer

pass_student = 0
fail_student = 0

marks = [45, 78, 90, 33, 60]

for m in marks:
    if m >= 50:
        pass_student += 1
    else:
        fail_student += 1

print("total number of pass students: ", pass_student)
print("total number of fail students: ", fail_student)
print("Final Result")
print("Pass Student:", pass_student ,"Fail student:",fail_student)

#3. Simple Data Cleaner

clean_list = []
names = [" Alice ", "bob", " CHARLIE "]
for name in names:

    clean = name.strip().lower()
    clean_list.append(clean)
    
print(clean_list)


# 4. Message Length Analyzer

messages = ["Hi", "Welcome to the platform", "OK"]

for m in messages:
    length = len(m)

    print("Message:", m)
    print("Length:", length)

    if length > 10:
        print("Flag: This message is longer than 10 characters")


# 5. Error Message Detector

logs = ["INFO", "ERROR", "WARNING", "ERROR", "ERROR"]
msg = "ERROR"
count = 0
for m in logs:
    if m == msg:
        print("Error detected") 
        count +=1

print("Count of error:", count)
    


