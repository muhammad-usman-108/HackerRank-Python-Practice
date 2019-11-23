if __name__ == '__main__':
    student = []
    score_list = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        score_list.append(score)
        temp = [name,score]
        student.append(temp)
m = min(score_list)

for _ in range(n):
    if m in score_list:
        score_list.remove(m)

name = [value[0] for value in student if value[1] == min(score_list)]

for n in sorted(name):
    print(n)
