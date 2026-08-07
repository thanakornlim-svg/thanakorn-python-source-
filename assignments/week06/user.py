def create_user_profile(username, age=18, premium=False):
    if premium:
        user_type = "Premium User"
    else:
        user_type = "Standard User"
 
    return f"{username} (age: {age}) - {user_type}"
 
 
ตัวอย่างการใช้งาน
print(create_user_profile("KAO"))
print(create_user_profile("MEW", 25))
print(create_user_profile("TOEY", 30, True))
