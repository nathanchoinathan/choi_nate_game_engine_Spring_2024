# This file was created by: Nate Choi

# this is not very abstract
def multiplier (x,y):
    return x*y

def printer (t): 
    return str(t) + "I concatenated"

print(multiplier(10,10)) 

print(printer(multiplier(5,5)))

i = 0

while True:
    print("this will happen 10 times")
    i+=1
    if i > 10:
        break
# j = 0
j = 0
while j < 10:
    j = 0
    # j = 0
    print("this will happen 10 times")
    j+=1
    # j = 1