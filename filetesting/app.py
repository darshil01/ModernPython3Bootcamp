import pdb

with open("nltest.txt", "r") as f:
    results = []
    data = f.readlines()
    for line in data:
        results.append((line.split(" ")[6]).split(":")[0])

b = (set(results))

with open("results.txt", "a+") as f:
    f.write(f"{len(b)} Devices connected to NL thru Irvine DC\n")
    for obj in b:
        f.write(obj + "\n")

# pdb.set_trace()
