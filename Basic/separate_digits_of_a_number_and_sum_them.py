num = 123
fdigit = num % 10

num = num // 10
sdigit = num % 10
num = num // 10
tdigit = num % 10
print("Digits:",tdigit,sdigit,fdigit,'\n',"Sum:",fdigit+sdigit+tdigit)
