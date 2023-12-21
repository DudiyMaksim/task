# task 1
a,b=map(int, input().split())
for i in range(a,b+1):
    if i%7==0:
        print(i, end=' ')
# task 2
x=0
a,b=map(int, input().split())
for i in range(a, b+1):
    print(i, end=' ')
print('')
for i in range(b, a-1, -1):
    print(i, end=' ')
print('')
for i in range(a,b+1):
    if i%7==0:
        print(i, end=' ')
print('')
for i in range(a,b+1):
    if i%5==0:
        x+=1
print(x)
# task 3
a,b=map(int, input().split())
for i in range(a,b+1):
    if i%3==0 and i%5==0:
        print('Fizz Buzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)