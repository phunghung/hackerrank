n = int(input())
width = len("{:b}".format(n))


for i in range(n):
    print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i+1, width=width))


# a, b = 6,8
#
# print("%d haha %d" % (a, b))
# print("{} haha {}" .format(a, b))