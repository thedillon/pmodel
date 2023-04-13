with open("flightperf.txt", "r") as f:
    content = f.read()
    content = content.replace("|", ",")
    content = content.replace("\t", ",")

with open("performance.csv", "w") as f:
    f.write(content)
