print("Welcome in RoboticsTech")
print("Hello,i'm memobot")
print("Our services:")
print("Software")
print("Hardware")

q_input = input("Please chose on of the options. How can i help you? ")

if q_input.lower() != "software" and "hardware":
    print("Thanks for using our services!")
    print("Habe a nice day! See You!")
    quit()

print("Okay! Yo have been chosen ", q_input)
score = 0

answer = input("Are you new customer? ")
if answer.lower() == "yes":
    print("Hello ... ")
    score += 1
else:
    print("If you want you can sign up later, and join our platform")

answer = input("Can describe the problem please? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
