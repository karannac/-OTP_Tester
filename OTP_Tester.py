import random 

def otp():
  a = random.randint(1111, 9999)

  return a

b = otp()
print('Your OTP is: ', b)


c = input('Enter phone number: ')
d = input('Enter your OTP: ')



if d == str(b):
  print('Your OTP is correct')
else:
  print('Your OTP is wrong ')


u = otp()
print('Your OTP is: ', u)

f = input('Enter phone number: ')
t = input('Enter your OTP: ')


if t == str(u):
  print('Your OTP is correct')
else:
  print('Your OTP is wrong ')





