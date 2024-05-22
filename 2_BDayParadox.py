from random import randint
import datetime

def generate_birthdays(numberOfBDays: int) -> list:
    birthdays = []
    for i in range(numberOfBDays):
        startOfYear = datetime.date(2001,1,1)
        randomDayOfYear = datetime.timedelta((randint(0,364)))
        randomBirthday = startOfYear + randomDayOfYear
        birthdays.append(randomBirthday)
    return birthdays

def dateConvertation(date: datetime) -> str:
    months = ["Jan","Feb","Mar","Apr",
              "May","Jun","Jul","Aug",
              "Sep","Oct","Nov","Dec",]
    return f"{date.day} {months[int(date.month)-1]}"

def print_birthdays(newListOfBDays: list):
    string = ""
    for i, birthday in enumerate(newListOfBDays):
        if (i+1)%10==0 and i != 0:
            string = string + birthday + "\n"
        else:
            string = string + birthday + "\t"
    print(string)
    print()
    
def is_birthday_matches(listOfBirthdays: list) -> bool:
    if len(listOfBirthdays) != len(set(listOfBirthdays)):
        return True
    else:
        return False
    
def generating_process(listOfBirthdays: list, numberOfBDays: int):
    print(f"Generating {len(listOfBirthdays)} random birthdays 100,000 times...")
    input("Press Enter to begin...")
    matchTimes = 0
    for simulation in range (0,100_000):
        if simulation % 10000 == 0:
            print(f"{simulation} simulations ran")
        generationList = generate_birthdays(numberOfBDays)
        if is_birthday_matches(generationList) == True:
            matchTimes += 1
    print(matchTimes)
    print(f"""Out of 100,000 simulations of {numberOfBDays} people, there was a
    matching birthday in that group {matchTimes} times. This means
    that {numberOfBDays} people have a {round(matchTimes/100000,4)*100} % chance of
    having a matching birthday in their group.
    That's probably more than you would think!""")
    
while True:
    numberOfBDays = int(input("Enter the number of birthdays you want to generate (max 100): "))
    if 0 < numberOfBDays <= 100:
        break
    else:
        print("Please, enter a valid number!")

listOfBDays = generate_birthdays(numberOfBDays)
newListOfBDays = [dateConvertation(date) for date in listOfBDays]
print(f"Here are {numberOfBDays} birthdays:")
print_birthdays(newListOfBDays)
generating_process(listOfBDays,numberOfBDays)