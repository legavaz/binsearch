

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

i=1
while i<=20:
    print('Факториал {0} = {1}'.format(i,fact(i)))    
    i+=1


