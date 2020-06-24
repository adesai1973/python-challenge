
import os
import csv

candidate_name = " "
vote_count = 0
total_votes = 0
candidate_list = []
candidate_unique_list = []
candidate_votes = {}

csvpath = os.path.join('.', 'Resources', 'election_data.csv')


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        candidate_list.append(row[2])

    candidate_unique_list = list(set(candidate_list))
    #print(candidate_unique_list)

    for unique in candidate_unique_list:
        for candidate in candidate_list:  
            if candidate == unique:
                vote_count += 1
        candidate_votes[unique] = vote_count
        vote_count = 0

for candidate in candidate_votes.items():
    total_votes += int(candidate[1])

banner_line = "=" * 40
banner_line_lite = "-" * 40
print(banner_line)
print('{:~^40}'.format("Election Results"))
print(banner_line)
print(f"Total Votes:   {total_votes}")
print(banner_line_lite)

sorted_candidate_votes = sorted(candidate_votes.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    
for item in sorted_candidate_votes:
    percent = "{:.0%}".format(item[1]/total_votes)
    print('{:<10s}{:>10s}{:>10s}'.format(str(item[0]), str(item[1]), percent))
print(banner_line)
print(f"Winner of this election is:  {sorted_candidate_votes[0][0]}")
print(banner_line)

# Specify the file to write to
output_path = os.path.join(".", "analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text:
    text.write(banner_line +'\n')
    text.write('{:~^40}'.format("Election Results") +'\n')
    text.write(banner_line +'\n')
    text.write(f"Total Votes:   {total_votes}\n")
    text.write(banner_line_lite +'\n')

    #sorted_candidate_votes = sorted(candidate_votes.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
        
    for item in sorted_candidate_votes:
        percent = "{:.0%}".format(item[1]/total_votes)
        text.write('{:<10s}{:>10s}{:>10s}'.format(str(item[0]), str(item[1]), percent) +'\n')
    text.write(banner_line +'\n')
    text.write(f"Winner of this election is:  {sorted_candidate_votes[0][0]}\n")
    text.write(banner_line +'\n')