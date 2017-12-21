# pythonScrub

Scrubbing a dataset with a python program 

This program was built to scrub a dataset pulled from https://data.cityofnewyork.us/Education/School-Safety-Report/qybk-bjjc/data so that
it could be readily used for study.

This dataset contains the number of crimes that occurred in New York City Public schools in a given school year. 

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
