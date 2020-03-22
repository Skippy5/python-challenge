import os
import csv

# Path and file to open for analysis
Polling_csv = os.path.join('Resources', 'election_data.csv')

#Define variables to be used during analysis
candidates = []
candidate_votes = []
overall_votes = 0

#open file and define EOL
with open(Polling_csv, newline = '') as csvfile:
    #define file and delminiter
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #used to skip the hearer row in the anlaysis
    next(csvreader, None)

    #Read file, check each result and write results to a list
    # add a vote if the cadidate exists or a new entry if not
    for row in csvreader:
        if row[2] in candidates:
            candidate_votes[candidates.index(row[2])]=candidate_votes[candidates.index(row[2])]+1
        else:
            candidates.append(row[2])
            candidate_votes.append(1)


    #print the results in the desired format
    print('Election Results')
    print('-------------------------')
    total_votes=sum(candidate_votes)#I added this line, because I can't figure out how to do full calcualation in one line below
    print('Total Votes: ' + str(total_votes)) 
    print('-------------------------')
    for name in range(len(candidates)):
        #Calculate percentage for each Candidate
        v_percent = round(candidate_votes[name]/total_votes*100, 3)
        #Write candiate information and results of above
        print(candidates[name]+ " : " + str(v_percent) + "% : (" + str(candidate_votes[name])+")")
    print(f'-------------------------')
    #find which position in the list has be move votes and output that value 
    Winnerpos = candidate_votes.index(max(candidate_votes))
    print('Winner: ' + candidates[Winnerpos])
    print(f'-------------------------')


#same as above, but write results to text file
f = open("results.txt", "a")
f.write('Election Results\n')
f.write('-------------------------\n')
f.write('Total Votes:'  + str(total_votes) + '\n')
f.write('-------------------------\n')
for name in range(len(candidates)):
    v_percent = round(candidate_votes[name]/total_votes*100, 3)
    f.write(candidates[name]+ " : " + str(v_percent) + "% : (" + str(candidate_votes[name])+")\n")
f.write('-------------------------\n')
f.write('Winner: ' + candidates[Winnerpos] + '\n')
f.write('-------------------------\n')
f.close()