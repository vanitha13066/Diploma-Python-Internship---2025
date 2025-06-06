def evenodd(n):
    if(n%2==0):
        print('even')
    else:
        print('odd')
n = int(input())

def palindrom(s):
    if(s==s[::-1]):
        print('palindrom')
    else:
        print('not palindrom')
s = input()