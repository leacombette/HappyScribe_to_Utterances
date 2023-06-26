import re
import sys

file = sys.argv[1]
filename = file.split('.txt')[0]

data = open(file, "r").read()
b = re.sub("\[([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3})\] - ([a-zA-Z\s]*)\n\n", "", data)
blockList = re.split("\n{2}",  b.strip())

output = "time| speaker| text\n"

for block in blockList:
    timestampAndSpeakerPattern = "\[([\d:.]*)\][\s-]{0,3}(.*)?\n"
    firstLine = re.search(timestampAndSpeakerPattern, block)
    # print(block)
    # print(firstLine)
    # print('\n')
    time = firstLine.group(1)
    speaker = firstLine.group(2)
    text = re.split('\n', block)[1]
    pattern = re.compile("([^?!.]*[?!.]+)[\s]?")
    for (ut) in re.findall(pattern, text):
        output += f'{time}| {speaker}| {ut}\n'

csv = open(f'{filename}.csv', "w")
csv.write(output)
csv.close()
