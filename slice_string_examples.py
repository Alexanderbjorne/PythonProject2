s = "ajfjskfkmsidis"
print(s)
print(s[1:4], s[6:9])
print(s[:4], s[7:])
print(s[1:10:2])
print(s[::-1])


### This is how we replace a letter in a string
s = "cat"

s = "r" + s[1:]
print(s)

s = "seven"
s = s[:2] + "7" + s[3:]
print(s)

