'''import re

text = input()
regex_pattern = r"[,.£]"
#print(re.split(text))
result = re.split(r",", input())
print(result)
'''
import re

string = input()
pattern = r"[, . £]"  # Split on comma, space, or exclamation mark

result = re.split(pattern, string)
print("\n".join(result))
