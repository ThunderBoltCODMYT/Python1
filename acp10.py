Password= ''
print("welcome to the random password generator program")
length = int(input("Enter the length of the password you want it to be(max 5-10 don't ask why): "))
if length > 10:
    print("Length too long, setting to 10")
    length = 10
else:
    print("Length set to", length)
import random
import string
listNumbers=['1','2','3','4','5','6','7','8','9','0']
listSpecialCharacters=['!','@','#','$','%','^','&','*','(',')','-','=','+','_','{','}','[',']',':',';','"',"'",'<','>',',','.','?','/']
listAlphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def generate_password(length):
    # your logic here using random.choices(...)(length):
    if length == 5:
        base = length // 3
        remainder = length % 3
        count_numbers = base + (1 if remainder > 0 else 0)
        count_specials = base + (1 if remainder > 1 else 0)
        count_letters = base
        part1 = random.choices(listNumbers, k=count_numbers)
        part2 = random.choices(listSpecialCharacters, k=count_specials)
        part3 = random.choices(listAlphabets, k=count_letters)
        password = part1 + part2 + part3
        random.shuffle(password)  # Shuffle to ensure randomness
    elif length == 6:
        base = length // 3
        remainder = length % 3
        count_numbers = base + (1 if remainder > 0 else 0)
        count_specials = base + (1 if remainder > 1 else 0)
        count_letters = base
        part1 = random.choices(listNumbers, k=count_numbers)
        part2 = random.choices(listSpecialCharacters, k=count_specials)
        part3 = random.choices(listAlphabets, k=count_letters)
        password = part1 + part2 + part3
        random.shuffle(password)  # Shuffle to ensure randomness
    elif length == 7:
        base = length // 3
        remainder = length % 3
        count_numbers = base + (1 if remainder > 0 else 0)
        count_specials = base + (1 if remainder > 1 else 0)
        count_letters = base
        part1 = random.choices(listNumbers, k=count_numbers)
        part2 = random.choices(listSpecialCharacters, k=count_specials)
        part3 = random.choices(listAlphabets, k=count_letters)
        password = part1 + part2 + part3
        random.shuffle(password)  # Shuffle to ensure randomness
    elif length == 8:
        base = length // 3
        remainder = length % 3
        count_numbers = base + (1 if remainder > 0 else 0)
        count_specials = base + (1 if remainder > 1 else 0)
        count_letters = base
        part1 = random.choices(listNumbers, k=count_numbers)
        part2 = random.choices(listSpecialCharacters, k=count_specials)
        part3 = random.choices(listAlphabets, k=count_letters)
        password = part1 + part2 + part3
        random.shuffle(password)  # Shuffle to ensure randomness
    elif length == 9:
        base = length // 3
        remainder = length % 3
        count_numbers = base + (1 if remainder > 0 else 0)
        count_specials = base + (1 if remainder > 1 else 0)
        count_letters = base
        part1 = random.choices(listNumbers, k=count_numbers)
        part2 = random.choices(listSpecialCharacters, k=count_specials)
        part3 = random.choices(listAlphabets, k=count_letters)
        password = part1 + part2 + part3
        random.shuffle(password)  # Shuffle to ensure randomness
    elif length == 10:
        base = length // 3
        remainder = length % 3
        count_numbers = base + (1 if remainder > 0 else 0)
        count_specials = base + (1 if remainder > 1 else 0)
        count_letters = base
        part1 = random.choices(listNumbers, k=count_numbers)
        part2 = random.choices(listSpecialCharacters, k=count_specials)
        part3 = random.choices(listAlphabets, k=count_letters)
        password = part1 + part2 + part3
        random.shuffle(password)  # Shuffle to ensure randomness
    else:
        print("invalid length")
        pass
    return password
password = generate_password(length)
print("Your random password is ready:D")
print("Password: ", password)