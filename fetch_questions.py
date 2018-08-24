import urllib.request
import re
import pickle

QandA = urllib.request.urlopen('https://raw.githubusercontent.com/uberspot/OpenTriviaQA/master/categories/general').read(2000).decode('utf8',errors="replace")
QandA = QandA.split('#')

# questions = [i.split('A',1) for i in questions]

# for i in QandA:
#         print(i)

# for i in QandA:
#     result = re.search(re.compile(r'Q([\s\S]*)\^', re.MULTILINE), i)
#     if result:
#         print ("Match was found at {start}-{end}: {match}".format(start = result.start(), end = result.end(), match = result.group()[2:-2]))

questions = [re.search(re.compile(r'Q([\s\S]*)\^', re.MULTILINE), i).group()[2:-2] for i in QandA if re.search(re.compile(r'Q([\s\S]*)\^', re.MULTILINE), i)]

# for i in QandA:
#     result = re.search(r'\^(.*)\n', i)
#     if result:
#         print ("Match was found at {start}-{end}: {match}".format(start = result.start(), end = result.end(), match = result.group()[2:-1]))

correct_answers = [re.search(re.compile(r'\^(.*)\n', re.MULTILINE), i).group()[2:-1] for i in QandA if re.search(re.compile(r'\^(.*)\n', re.MULTILINE), i)]

A_answers = [re.search(re.compile(r'\nA(.*)\n', re.MULTILINE), i).group()[3:-1] for i in QandA if re.search(re.compile(r'\nA(.*)\n', re.MULTILINE), i)]

B_answers = [re.search(re.compile(r'\nB(.*)\n', re.MULTILINE), i).group()[3:-1] for i in QandA if re.search(re.compile(r'\nB(.*)\n', re.MULTILINE), i)]

C_answers = [re.search(re.compile(r'\nC(.*)\n', re.MULTILINE), i).group()[3:-1] for i in QandA if re.search(re.compile(r'\nC(.*)\n', re.MULTILINE), i)]

D_answers = [re.search(re.compile(r'\nD(.*)\n', re.MULTILINE), i).group()[3:-1] for i in QandA if re.search(re.compile(r'\nD(.*)\n', re.MULTILINE), i)]

data = list(zip(questions,correct_answers,A_answers,B_answers,C_answers,D_answers))

with open("general.txt", "wb") as fp:   #Pickling
    pickle.dump(data, fp)
