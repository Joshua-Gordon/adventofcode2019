lower = 171309
upper = 643603

def check_doubles(n):
    """Returns true if there is a repeated character"""
    num = str(n)
    for c in range(1,len(num)):
        if num[c-1] == num[c]:
            return True
    return False

def check_doubles_2(n):
    """Returns true if there is a character repeated exactly twice in a row"""
    num = str(n)
    for c in set(num):
        if num.count(c) == 2:
            pos = num.find(c)
            if pos != len(num)-1 and num[pos+1] == c:
                return True
    return False

def increment(itr):
    """Returns the next number with nondecreasing digits"""
    num = str(itr)
    if len(num) == 1:
        return itr+1
    if num[-1] >= num[-2]:
        if num[-1] == '9':
            s = str(increment(int(num[:-1])))
            return int(s+s[-1])
        return itr+1
    return int(num[:-1] + num[-2])

def check_nondecreasing(n):
    num = str(n)
    for c in range(1,len(num)):
        if num[c-1] > num[c]:
            return False
    return True

def fix_lower(l):
    while not check_nondecreasing(l):
        l += 1
    return l

l2 = []
itr2 = fix_lower(lower)
while itr2 < upper:
    if check_doubles_2(itr2):
        l2.append(itr2)
    itr2 = increment(itr2)
print(l2)
print(len(l2))
