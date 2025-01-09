x = int(input())

must_be_together = {}
not_be_together = {}

for _ in range(x):
    group = input().split(" ")

    # add group records 

    must_be_together[group[1]] = group[0]
    must_be_together[group[0]] = group[1]


y = int(input())

for _ in range(y):
    group = input().split(" ")

    # add group records 

    not_be_together[group[1]] = group[0]
    not_be_together[group[0]] = group[1]

