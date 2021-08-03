# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

a = r'^([456]\d{3})(\-?)(\d{4})(\-?)(\d{4})(\-?)(\d{4})$'
b = r'^(?:([0-9])(?!\1{3,})){16}$'

for _ in range(int(input())):
    s = input()
    if re.match(a, s):
        s = s.replace('-', '')
        if re.match(b, s):
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
