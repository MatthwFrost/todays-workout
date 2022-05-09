lines = []

with open('setup_doc.txt') as f:
    for line in f:
        lines.append(line.strip())


print(lines[8])

f.close()
