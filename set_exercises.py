inputlist = [1, "hello", 6, 8]

print(inputlist)
print(len(set(inputlist)))
print(list(set(inputlist)))

if len(list(set(inputlist))) == len(inputlist):
    print("No dupes")
else:
    print("Dupes found")