with open("datasets/corporate-small/communities-source.txt") as c:
    comms = list(l.strip() for l in c.readlines())
with open("datasets/corporate-small/nodes.txt") as n:
    nodes = list(l.strip() for l in n.readlines())

lines = []

for x in comms:
    if x.split(' ')[0] in nodes:
        lines.append(f"{x}\n")

with open("datasets/corporate-small/communities.txt", "w") as w:
    w.writelines(lines)
