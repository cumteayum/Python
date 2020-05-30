from colorama import Fore, Back, Style 

secure = (('i', '|'), ('a', '@'), 
        ('s', '$'), ('h', '#'), ('n', ')'),
        ('b', '*'), ('c', 'C'), ('d', '!~'),
        ('e', 'B'), ('f', 'ffsff'), ('g', ")nfV"),
        ('j', '_+='), ('k', 'bdbsa'), ('l', '@!'),
        ('m', 'feMd'), ('o', 'Z'), ('p', '{['),
        ('q', "Na dwd"), ('r', 'UIA'), ('s', '^&'),
        ('t', 'da'), ('u', '*^%#'), ('v', '$%'),
        ('x', '#1`'), ('y', 'fd'), ('z', 'A'))

password = input(Fore.GREEN + "Enter:  ")

def securepass(password):
    for i,j in secure:
        password = password.replace(i,j)
    return password

while True:
    password = securepass(password)
    print(Fore.GREEN + f'Your Password is : {password}')
    break