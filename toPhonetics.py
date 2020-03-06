# cat dataNounsMini.txt | flookup -ix albPhon.foma def > dataNounsPhons.txt

from subprocess import Popen, PIPE
from shlex import split
import sys

filename = sys.argv[1]
# arg2 = sys.argv[2]

file = open(filename)
fileStr = file.read()
print(fileStr)

first = Popen(['cat', filename], stdout=PIPE)


# p2 = Popen(split("cat "), stdin=fileStr)
# p2 = Popen(split("flookup -ix albPhon.foma def"), stdin=fileStr)

# subprocess.call("tar c my_dir | md5sum",shell=True)
