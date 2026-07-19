#Password checker


password = input("Enter password: ")

score = 0

# check length


if len(password) >= 8:
    score = score + 20
    print("length ok")
else:
    print("password too short at least 8 chr.")

# check for numbers


has_number = False
for char in password:
    if char in "0123456789":
        has_number = True
if has_number:
    score = score + 20
    print("has number")
else:
    print("add numbers please")

# check for uppercase


has_upper = False
for char in password:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        has_upper = True
if has_upper:
    score = score + 20
    print("has uppercase")
else:
    print("add uppercase letters")

# check for lowercase


has_lower = False
for char in password:
    if char in "abcdefghijklmnopqrstuvwxyz":
        has_lower = True
if has_lower:
    score = score + 20
    print("has lowercase")
else:
    print("add lowercase letters")

# check for special


has_special = False
for char in password:
    if char in "!@#$%^&*()":
        has_special = True
if has_special:
    score = score + 20
    print("has special char.")
else:
    print("add special chars like")

# final scpre


print("")
print("You got : " + str(score) + " out of 100")

if score == 100:
    print("PERFECT PASSWORD!!!")
elif score >= 80:
    print("Strong password")
elif score >= 60:
    print("Decent password")
elif score >= 40:
    print("Weak password")
else:
    print("Very weak password - try again")

