import re
s = "A man, a plan, a canal: Panama"
r = ''
rev = s[::-1]
print(rev)

for i in reversed(range(len(s))):
    r = r + s[i]

print("Reversed string is :",r)

# s = re.sub(r'[,:\s+]','',s)
# s = s.replace(',','')
# print(s)
# s = s.lower()
# print(s)
# str_rev = s[::-1]
# print(str_rev)