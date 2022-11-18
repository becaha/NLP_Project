import re
import numpy as np

f = open('alb_dict.txt')
corpus = f.read()
words = re.findall(r'(?<=,).*', corpus)
words_string = "\n".join(words)

matches = re.findall(r'.*[^\s\naeoiuE]{3,}.*', words_string)

def maxConsString(matches):
    matchCounts = np.zeros(len(matches))
    index = 0
    for match in matches:
        consStrings = re.findall(r'[^\s\naeoiu]{3,}', match)
        sortedCons = sorted(consStrings, key=len)
        count = len(sortedCons[len(sortedCons) - 1])
        matchCounts[index] = count
        index += 1
    maxCount = max(matchCounts)
    sortIndex = np.argsort(matchCounts)
    sortedMatches = [matches[i] for i in sortIndex]
    return sortedMatches


sortedMatches = maxConsString(matches)
sortedMatches = "\n".join(sortedMatches)
print(sortedMatches)
