import string
import random

userInput = int(input("Enter the password length: \n"))
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase # ye poora aako lowercase uppercase character ko print kartaso
s3 = string.digits
s4 = string.punctuation

s = []
s.extend(list(s1))
s.extend(list(s2))  #ye sabko list ka andaar daldalteso
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s) #s ko shuffle karleteso

# random.sample(s, userInput) ye aako shuffle nai karenga, direct uska choice ka letter utako denga

print("".join(s[0:userInput]))
'''
string module se lowercase uppercase digits poora lelako, ye poora s1,s2,s3,s4 ko sabko ek saat
list mein daldalteso, wo list ko shuffle karlako password generator banjaga. ab ki join likehe katho
s ko slice karteso usse wo list return karenga usse join likdale katho str mein aanga
'''