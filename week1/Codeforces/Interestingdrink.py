import bisect
n = int(input())
shops = list(map(int,input().split()))
shops.sort()
d = int(input())
for i in range(d):
    target = int(input())
    possible_shop = bisect.bisect_right(shops,target)
    print(possible_shop)