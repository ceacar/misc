def choose_steps(n,k):
    print("choosing steps for {0} {1}".format(n, k))
    if n == 0:
        return 0
    if n == 1:
        if k != 1 and k != 0:
            return [0, 1] #max step is 0 or 1 , so it's 1
        if k ==0 :
            return [1]
        if k ==1:
            return [0]
        else:
            return [-1] #-1 means this should not be taken

    jump_steps = []

    for i in range(1, n):
        print("sub_stepping for ", n-i, k)
        total_step = choose_steps(n-i, k)
        print("sub_step res", total_step)
        if jump_steps != k:
            jump_steps.extend(total_step)
    print("jump_steps:{}".format(jump_steps))

    res = []
    for step in jump_steps:
        if step + n !=k:
            res.append(step+n)
    return res

if __name__ == '__main__':
    print(max(choose_steps(2,1)))
    print(max(choose_steps(2,2)))
    print(max(choose_steps(3,3)))
