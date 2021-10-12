import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(L, l, u, target):
    mid = int((l + u) / 2)
    if l < u:
        if target < L[mid]:
            return recbinsearch(L, l, mid-1, target)
        elif target > L[mid]:
            return recbinsearch(L, mid+1, u, target)
    elif l == u:
        if (target == L[l]) and (target == L[u]):
            return mid
    else:
        return -1


numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
