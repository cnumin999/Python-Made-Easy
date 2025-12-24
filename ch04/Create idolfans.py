newjeans=['철수', '영희', '민수', '지현', '서연']
ive=['영희', '민수', '지수', '서연', '하나']
aespa=['철수', '지현', '지수', '서연', '나영']

answer=[]
for x in newjeans:
    if (x in ive) and (x not in aespa):
        answer.append(x)
print(','.join(answer))
