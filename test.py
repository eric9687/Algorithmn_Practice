cards = [[10,5,15],[8,9,13],[10,10,10]]
num =  len(cards)
changed = [0]*num
# print(changed)
answer = 0
# print(cards)
def change_possible(c1,c2,ii,jj):
    if changed[ii] ==0 and changed[jj] == 0:
        min_c1 = c1.index(min(c1))
        min_c2 = c2.index(min(c2))
        # print("*")
        # print(min_c1)
        if min_c1 != min_c2:
            c1[min_c1] += 1
            c2[min_c1] -= 1
            c1[min_c2] -= 1
            c2[min_c2] += 1
            min_c1_t = c1.index(min(c1))
            min_c2_t = c2.index(min(c2))
            if  min_c1_t==min_c1 and min_c2_t==min_c2:
                return [True, c1[min_c1],c2[min_c2]]
            # print(cards)
        
        return [False, 0,0]
    
for i in range(num):
    for j in range(num):
        if i!= j:
            if changed[i] ==0 and changed[j] ==0:
                cd1 = cards[i]
                cd2 = cards[j]
                possible, cc1,cc2 = change_possible(cd1,cd2,i,j)
                if possible:
                    if changed[i] == 0 and changed[j] == 0:
                        print("*")
                        print(i,j)
                        
                        answer += cc1 + cc2 
print(changed)
print(cards)
for i in range(num):
    if changed[i] == 0:
        print(cards[i])
        answer += min (cards[i])                    
print(answer)