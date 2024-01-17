import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)

    candidate_list = [candidate[2] for candidate in csvreader]

total_votes = len(candidate_list)

candidates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

candidates_info = sorted(candidates_info, key=lambda x: x[1], reverse=True)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f"{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})")

print("-------------------------")
print(f"Winner: {candidates_info[0][0]}")
print("-------------------------")

csvpath = os.path.join("Resources", "analysis")
with open(csvpath, "w") as text_file:
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print(f"Total Votes: {total_votes}", file = text_file)
    print("-------------------------", file = text_file)

    for candidate in candidates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f"{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})", file = text_file)

    print("-------------------------", file = text_file)
    print(f"Winner: {candidates_info[0][0]}", file = text_file)
    print("-------------------------", file = text_file)

