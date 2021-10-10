s = 'abcde'
print(s[:-0])
print(s[:-1])
print(s[:-2])

print("========")
print(s[::-1])

print(s[1:-1])

print(s[0:-1:1])

print(s[0:-1:2])

import os
ZVT_HOME = os.environ.get('ZVT_HOME')
print(ZVT_HOME)