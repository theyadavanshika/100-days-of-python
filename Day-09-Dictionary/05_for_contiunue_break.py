for i in range(7):
    print("------")
    print("This is iteration: ", i)
    for j in range(i):
        if(j == 3):
            break
        elif(j==1):
            continue
        print("-----This is nested iteration ", j)
    
    if(i == 5):
        break # stops the current and future iterations
    if(i==4):
        continue # stops the current iteration
    print("This is doing something: ", i * 2) # not printed in 4 