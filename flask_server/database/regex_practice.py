# import the re module to access regex functions
import re
import os


# basic steps for creating & finding 
# regular expression objects:
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 555-555-5555.')
print('Phone number found: ' + mo.group())

# explaination of ^ code:
'''
1. Import the regex module with import re.

2. Create a Regex object with the re.compile() function. (Remember to use araw string.)

3. Pass the string you want to search into the Regex object’s search() method.This returns a Match object.

4. Call the Match object’s group() method to return a string of the actualmatched text.

test online:
https://pythex.org/
'''

# adding parenthesis will create groups
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 555-555-5555.')
print(mo.group(1))
print(mo.group(2))
print(mo.group()) #returns entire matched text
print(mo.groups()) #returns a tuple

# add and escape the () chars 
# around area code so they are matched too
phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is (555) 555-5555.')
print(mo.group(1))

# using the findall method
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.findall('My number is 555-555-5555. if you cannot reach me there then 678-342-6789')
print(mo)

'''
To summarize what the findall() method returns, remember the following:

1. When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall() returns a list of string matches, 
such as ['415-555- 9999', '212-555-0000'].

2. When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\ d\d\d), the method findall() returns a list of tuples of strings (one string for each group), such as [('415', '555', '1122'), ('212', '555', '0000')].

'''

file_name_regex = re.compile(r'post_.*')
example = file_name_regex.findall('hey ./post_01 also ./post_05')
print(example)

current_path = "/Users/Laurel/Desktop/good_processing_unit/flask_server/database"
files_in_database = os.listdir(current_path)

database_files = []

for file in files_in_database:
    if len(file_name_regex.findall(file)) > 0:
        database_files.append(file)
    #database_files.append(file_name_regex.findall(file))
    
print(database_files)


