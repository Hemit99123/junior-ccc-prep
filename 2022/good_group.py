# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# good groups

x = int(input())

must_be_together = {}
not_be_together = {}

# These are inputs for pairs of people that must be together
for _ in range(x):
    group = input().split(" ")

    # add group records 

    must_be_together[group[1]] = group[0]
    must_be_together[group[0]] = group[1]


y = int(input())

# These are inputs for pairs of people that must NOT be together
for _ in range(y):
    group = input().split(" ")

    # add group records 

    not_be_together[group[1]] = group[0]
    not_be_together[group[0]] = group[1]

g = int(input())

# Use a set to track violations in the current group to avoid double-counting
group_violations = set()

for _ in range(g):
    group = input().split(" ")

    person1 = group[0]
    person2 = group[1]
    person3 = group[2]

    # Check for violations involving must_be_together
    if person1 in must_be_together and must_be_together[person1] not in group:
        group_violations.add(tuple(sorted([person1, must_be_together[person1]])))

    if person2 in must_be_together and must_be_together[person2] not in group:
        group_violations.add(tuple(sorted([person2, must_be_together[person2]])))

    if person3 in must_be_together and must_be_together[person3] not in group:
        group_violations.add(tuple(sorted([person3, must_be_together[person3]])))

    # Check for violations involving not_be_together
    if person1 in not_be_together and not_be_together[person1] in group:
        group_violations.add(tuple(sorted([person1, not_be_together[person1]])))

    if person2 in not_be_together and not_be_together[person2] in group:
        group_violations.add(tuple(sorted([person2, not_be_together[person2]])))

    if person3 in not_be_together and not_be_together[person3] in group:
        group_violations.add(tuple(sorted([person3, not_be_together[person3]])))

print(len(group_violations))

