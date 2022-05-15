def toString(List):
    return ''.join(List)

def permute(a, l, r):
    count = 0
    if l==r:
        count +=1
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] 
    return count

string = "teloi"
n = len(string)
a = list(string)
permute(a, 0, n-1)

