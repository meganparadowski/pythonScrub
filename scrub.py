"""
Link to data source: https://data.cityofnewyork.us/Education/School-Safety-Report/qybk-bjjc/data
Records I am working with: first 1100

Accomplishments of this program:
1. change N/A's to blanks
2. remove all calculated averages
3. change the "Schools in Building" column from the names separated by '|' to
   a python array so that it could be easier manipulated later
4. remove schools with a blank "Register" column (schools with no registered students)
5. remove building name from "Schools in Building" list where it was added unnecessarily
   to many records
NOTE: schools with blank or unavailable crime numbers I have left as blank (I do
not want to simply assume there were 0 crimes - this is something that would need
fact-checking)
"""

#import csv module to read and write with csv reader and writer
import csv

def main():

    file = "School_Safety_Report.csv"
 
    try:
        read_file = open(file, "r")
        read = csv.reader(read_file)

    except Exception as e:
        print("File does not exist")
        print(e)

    else:
        write_to = open("School_Safety_Report_out.csv", "w")
        write = csv.writer(write_to, delimiter = ",")

        lines_read = 0
        lines_written = 0
        #empty array variable to store the index values of columns that hold
        #calculated averages
        avgs = []
        #variables to store the index values of schools in building, register,
        #and building name columns
        sib = 0
        register = 0
        bname = 0
        
        for line in read:
            lines_read += 1
            #empty array variable to later store the names of schools in a list
            #(as opposed to text separated by | which is how they are originally)
            schools = []
            #variable to track whether or not schools in building index has been
            #captured yet
            no_change = 0
            
            for x in line:
                #change N/A data cells to empty so they will not interfere
                #with calculating data later
                if "N/A" in x:
                    line[line.index(x)] = ''
                #store index values where averages are located
                if "Avg" in x:
                    avgs.append(line.index(x))
                #store which index schools in building are located so we can
                #change them to a list
                if x == "Schools in Building":
                    sib = line.index(x)
                    no_change = 1
                #store which index the number of registered students is located
                #in so we can remove schools with no registered students
                if x == "Register":
                    register = line.index(x)
                #store the index where the building name is located so we can
                #remove it if it appears in schools in building list
                if x == "Building Name":
                    bname = line.index(x)

            #if we have already captured the schools in building index...
            if no_change == 0:
                line[sib] = line[sib].split('|')
                for i in line[sib]:
                    i = i.strip()
                    #remove building name if it appears unnecessarily in list of
                    #school names
                    if line[bname] in i:
                        i = i.replace(line[bname], "")
                    if i != '':
                        schools.append(i)
                line[sib] = schools

            #remove columns with calculated averages
            stop = avgs[0]
            start = avgs[-1]
            line = line[0:stop] + line[start+1:]

            #only write rows with schools that have registered students
            if line[register] != '':
                write.writerow(line)
                lines_written += 1

    print("Lines read: " + str(lines_read))
    print("Lines written: " + str(lines_written))
    
main()
