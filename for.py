
for i in range(200):
    p=0
    for j in range(2,i):

        if i%j==0:
            p=1
            break

    if p==0:
        print(i)



