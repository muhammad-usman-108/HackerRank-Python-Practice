def swap_case(s):
    name=list(s)
    for i in range(0,len(s)):
        if s[i].islower():
            name[i]=s[i].upper()
        elif s[i].isupper():
            name[i]=s[i].lower()
        else:
            name[i]=s[i]
    name = ''.join(name)
    return name

if __name__ == '__main__':