import csv

full = open("artColl.csv","rb")
fullReader = csv.reader(full)
fullList = list(fullReader)

work = open("cleanfiles.txt", "rb")
workList = work.read().split("\n")

matchWriter = csv.writer(open("matches.csv", "wb"))
finWriter = csv.writer(open("final.csv", "wb"))

with open("artColl.csv", "rb") as f, open("final.csv", "rb") as doodle:
    rows = [row for row in fullList if row[0] in workList]
    for row in rows:
        matchWriter.writerow(row)
        block = "\r".join(row[1:6])
        concat = []
        concat.append(block)
        rc = row+concat
        finWriter.writerow(rc)
        print(rc)