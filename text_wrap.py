import textwrap

def wrap(string, max_width):
    i = 0
    l=[]
    while(i<len(string)):
        print(string[i:i+max_width])
        i = i + max_width
    return ""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
