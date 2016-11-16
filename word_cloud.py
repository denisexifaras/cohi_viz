with open("symptoms.txt") as f:
    content = f.readlines()



symptoms = []
for line in content:
	symptoms += [x.rstrip().lstrip() for x in line.replace("\n","").split(",")]

from collections import Counter

x = Counter(symptoms)

pain = 1
tmp = dict();
for key in x:
	if key != "":
		if "ache" in key or "pain" in key:
			pain += 1
		else:
			tmp[key] = x[key]

output = list()
for key in x:
	if key != "":
		if x[key] > 5:
			print key
			tmp = dict()
			tmp["text"] = key
			print tmp	
			tmp["size"] = x[key]
			print tmp
			output.append(tmp)
