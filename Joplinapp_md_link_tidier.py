# REVIEW

# General concept:
# 1. Make a database of all files in the notebook directory
# 2. Separate the database into files without .md and to .md files onlt
# 3. From .md database pull links from each file
# 4. increase the ability of section 3 - replace each link format 
# from: [description](../../_resources/file.filetype)
# to: [description](_resources/file.filetype)
# 5. copy all the none .md files into 'D:\del\output\_resources\
# I believe that for step 5 I need to take the none .md file database
# and make a new file with new path names
# then to run a loop for copying from database 1 to newpath database
# 6. Do the same as 5. but move .md files to 'D:\del\output\'


# First step to load the libraries I require
import os
import re

# In the next step I tested listing all the file paths in any container, the container
# for this use case is the file 'file_list' which contains in lines the file paths.
# The prepared use for this file is to make it a data base of sorts. 
# for finding all the markdown links from the database I fist need to split it into a markdown 
# only database first.
# For a directory path, get all file paths and write them to 'file_list' file
# ref: https://www.youtube.com/watch?v=PZUtUFDP_sc
filepath = "D:/del/jopMDmarchPythonTest/"
file = open("file_list", "w", encoding = 'utf-8')
for root, dirname, files in os.walk(filepath):
    for x in files:
        file.write(root + '/' + x + '\n')
file.close

# Then in this step I practiced regex for finding the pattern for a markdown link
# including the image link.
# This step can be removed from the code.
# goal: replace a string inside files:
# The string I want to find is anything wrapped between []() as a markdown link
#  ref: https://youtu.be/K8L6KVGG-7o
text_to_search = '''
[]()
[wordd](word)
[wordd word](word)
[this is 22 ](path/to\/ /file.filetype)
![this blka # asd 00213 13 µ](https://file.com)
lsdflgsdlfgl
'''
pattern = re.compile(r'!?\[[\w\s\d#]*\]\([\w\s\d#:\/.\\]*\)')
matches = pattern.finditer(text_to_search)
print("----------------------------")
for match in matches:
    print(match)

# This step is for listing the links in the files.
# Missing in this part is a separate database for .md files only.
# For each file in 'file_list' find markdown link pattern
# ref1: readlines - https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
file1 = open('file_list', 'r')
Lines = file1.readlines()
for line in Lines:
    print(line)
pattern = re.compile(r'!?\[[\w\s\d#]*\]\([\w\s\d#:\/.\\]*\)')
for line in Lines:
    print(line + "File")
    with open(line.rstrip('\n'), 'r', errors='ignore') as file:
        result = file.read()
    matches = pattern.finditer(result)
    for match in matches:
        print(match)
#print('--------------')
#for line in Lines:
#    print(line.format(line.strip()))




# Raw
import os
import re

# For a directory path, get all file paths and write them to 'file_list' file
# ref: https://www.youtube.com/watch?v=PZUtUFDP_sc
filepath = "D:/del/jopMDmarchPythonTest/"
file = open("file_list", "w", encoding = 'utf-8')
for root, dirname, files in os.walk(filepath):
    for x in files:
        file.write(root + '/' + x + '\n')
file.close

# goal: replace a string inside files:
# The string I want to find is anything wrapped between []() as a markdown link
#  ref: https://youtu.be/K8L6KVGG-7o
text_to_search = '''
[]()
[wordd](word)
[wordd word](word)
[this is 22 ](path/to\/ /file.filetype)
![this blka # asd 00213 13 µ](https://file.com)
lsdflgsdlfgl
'''
pattern = re.compile(r'!?\[[\w\s\d#]*\]\([\w\s\d#:\/.\\]*\)')
matches = pattern.finditer(text_to_search)
print("----------------------------")
for match in matches:
    print(match)

# For each file in 'file_list' find markdown link pattern
# ref1: readlines - https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
file1 = open('file_list', 'r')
Lines = file1.readlines()
for line in Lines:
    print(line)
pattern = re.compile(r'!?\[[\w\s\d#]*\]\([\w\s\d#:\/.\\]*\)')
for line in Lines:
    print(line + "File")
    with open(line.rstrip('\n'), 'r', errors='ignore') as file:
        result = file.read()
    matches = pattern.finditer(result)
    for match in matches:
        print(match)
#print('--------------')
#for line in Lines:
#    print(line.format(line.strip()))