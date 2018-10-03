def function(tn, t1, t2):
    tr = tn
    Fedor = Pifagor(tn, t1)
    post = Pifagor(tn, t2)
    min_dist = Fedor + post
    for i in range(-1,2):
        for j in range(-1,2):
            t_new = (tn[0] + i, tn[0] + j)
            new_Fedor = Pifagor(t_new, t1)
            new_post = Pifagor(t_new, t2)
            if new_Fedor+new_post < min_dist:
                min_dist =new_Fedor+new_post
                tr = t_new
    return tr


def Pifagor(a, b):
    x = (a[0] - b[0])**2
    y = (a[1] - b[1])**2
    return(x + y)

if __name__ == '__main__':
    t0 = (0,0)
    t1 = tuple(map(int,input().split()))
    t2 = tuple(map(int,input().split()))
    print(t0, t1, t2)
    answer = function(t0, t1, t2)
    print(answer)

