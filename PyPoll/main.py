import os
import csv
votes = 0
candidates = []
cand_vote = []
percentage = []
csvpath = os.path.join("election_data.csv")

with open (csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    for row in csvreader:
        votes = votes +1
        candidates.append(row[2])
        candidates = list(dict.fromkeys(candidates))
        if candidates.index(row[2]) <= ((len(cand_vote))-1):
            cand_vote[candidates.index(row[2])] = cand_vote[candidates.index(row[2])]+1
        else:
             cand_vote.append(int(1))
print("Election Results\n")
print("___________________________\n")
print(f"Total Votes: {votes}")
print("___________________________\n")
for i in range(len(cand_vote)):
    percentage.append((cand_vote[i]/votes)*100)
    print(f"{candidates[i]}: {round(percentage[i],3)}% ({cand_vote[i]})")
print("___________________________\n")
print(f"Winner: {candidates[percentage.index(max(percentage))]}")
print("___________________________\n")

output_path = os.path.join("election_results.txt")
with open(output_path, 'w', newline='') as csvfile:
    csvfile.write("Election Results\n")
    csvfile.write("________________________\n\n")
    csvfile.write(f"Total votes: {votes}\n")
    csvfile.write("________________________\n\n")
    for i in range(len(cand_vote)):
        percentage.append((cand_vote[i]/votes)*100)
        csvfile.write(f"{candidates[i]}: {round(percentage[i],3)}% ({cand_vote[i]})\n")
    csvfile.write("___________________________\n\n")
    csvfile.write(f"Winner: {candidates[percentage.index(max(percentage))]}\n")