l1 = [[3,6,9], [6,8,5], [9,7,2]]

def sum_val_list(l1):
    sum_r=[sum(i) for i in l1]
    print (sum_r)
    sum_col = [sum([row[i] for row in l1]) for i in range(0,len(l1[0]))]
    print(sum_col)
    sum_all = sum([sum(i) for i in l1])
    print(sum_all)

sum_val_list(l1)