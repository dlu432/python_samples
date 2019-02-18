mystr = 'BANANA'

vowels = 'AEIOU'
kevsc = 0
stusc = 0

for i in range(len(mystr)):
    if mystr[i] in vowels:
        kevsc += len(mystr)-i
    else:
        stusc += len(mystr)-i

if kevsc == stusc:
    print("Draw")
elif kevsc > stusc:
    print("Kevin {}".format(kevsc))
elif kevsc < stusc:
    print("Stuart {}".format(stusc))
