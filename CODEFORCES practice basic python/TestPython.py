n = int(input())
listperson = []
num = 0
numm = 0
for i in range(n):
    candidate_id, test_score, challenges_solved, forum_posts = [int(j) for j in input().split()]
    listper = []
    listper.append(candidate_id)
    listper.append(test_score+challenges_solved+forum_posts)
    listperson.append(listper)
for q in range(len(listperson)):
    if listperson[q][1] > num :
        num = listperson[q][1]
        numm = listperson[q][0]
print(numm)