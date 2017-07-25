S = "I had a cat named amanda when I was little"

count = 0
"""
for i in S:
    if i == "a":
        count += 1
print(count)
"""

while count < len(S):
    if S[:] == "a":
        count += 1

print(count)