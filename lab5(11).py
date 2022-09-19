import re
 
s = input()
findN = max(re.findall(r'(?i)n+', s), key=len)
print(f'Max n length: {len(findN)} ({findN})')
print(f'Replaced: {re.sub(r"!", r".", s)}')
