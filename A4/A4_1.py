def find_first_b(a, lower, upper, pos):
    if lower > upper:
        return pos
    m = (lower+upper)//2
    if a[m] == 'b':
        return find_first_b(a, lower, m-1, m)
    else:
        return find_first_b(a, m+1, upper, pos)


def main():
    print(find_first_b("aaaaaab",0,len("aaaaaab")-1,None))
    return 0

main()