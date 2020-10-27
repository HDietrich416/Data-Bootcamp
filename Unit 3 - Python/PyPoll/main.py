import os
import csv

election_csv=os.path.join("Resources", "Python_PyPoll_Resources_election_data.csv")

with open(election_csv, 'r') as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=',')
    next(csv_reader,None)
    num_rows = 0
    candidate=[]
    votes = []
    first_candidate=0
    second_candidate=0
    third_candidate=0
    fourth_candidate=0
    for row in csv_reader:
        num_rows += 1
        if row[2] not in candidate:
            candidate.append(row[2])
        if row[2] == candidate[0]:
            first_candidate = int(first_candidate +1)
        elif row[2] == candidate[1]:
            second_candidate = int(second_candidate +1)
        elif row[2] == candidate[2]:
            third_candidate = int(third_candidate +1)
        elif row[2] == candidate[3]:
            fourth_candidate = int(fourth_candidate + 1)

votes=[first_candidate, second_candidate, third_candidate, fourth_candidate]
result=zip(candidate, votes)

first_candidate_percent = round(first_candidate/num_rows*100,3)
second_candidate_percent =round(second_candidate/num_rows*100,3)
third_candidate_percent = round(third_candidate/num_rows*100,3)
fourth_candidate_percent = round(fourth_candidate/num_rows*100,3)

winner = max(votes)
winnerindex=votes.index(winner)
winnername = candidate[winnerindex]


print("Election Results")
print("-------------------------------")
print(f"Total Votes: {num_rows}")
print("-------------------------------")
print(f"{candidate[0]} {first_candidate_percent}% : ({first_candidate})")
print(f"{candidate[1]} {second_candidate_percent}%: ({second_candidate})")
print(f"{candidate[2]} {third_candidate_percent}%: ({third_candidate})")
print(f"{candidate[3]} {fourth_candidate_percent}%: ({fourth_candidate})")
print("-------------------------------")
print(f"Winner: {winnername}")
print("-------------------------------")

output_csv= os.path.join("PyPoll","Analysis", "Election_Results_Output.csv")

with open(output_csv, 'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow([f'Total Votes: {num_rows}'])
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow([f'{candidate[0]} {first_candidate_percent}% : ({first_candidate})'])
    csvwriter.writerow([f'{candidate[1]} {second_candidate_percent}%: ({second_candidate})'])
    csvwriter.writerow([f'{candidate[2]} {third_candidate_percent}%: ({third_candidate})'])
    csvwriter.writerow([f'{candidate[3]} {fourth_candidate_percent}%: ({fourth_candidate})'])
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow([f'Winner: {winnername}'])
    csvwriter.writerow(['-------------------------------'])


