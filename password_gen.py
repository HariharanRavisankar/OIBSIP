import random as rand
import array as ar
 

maxLen = 12

symbols = ['@','#',"!","$","%","&","=","?","|",'/']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']


combined_list = Numbers + lowercase + uppercase + symbols

Random_uppercase = rand.choice(uppercase)
Random_lowercase = rand.choice(uppercase)
Random_numbers = rand.choice(Numbers)
Random_symbols= rand.choice(symbols)


password = Random_lowercase + Random_uppercase + Random_numbers + Random_symbols

for x in range(maxLen - 4):
    password = password + rand.choice(combined_list)
    password_list = ar.array('u', password)
    rand.shuffle(password_list)

generated_password =""
for x in password_list:
    generated_password = generated_password + x

print(generated_password)

f = open('Generated_pass.txt','w')
f.writelines(generated_password)

f.close()

