# Explain regular expression methods match and search with its parameters.
# https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match#:~:text=re.search%20searches%20the%20entire%20string%2C%20as%20the%20documentation%20says%3A&text=Python%20offers%20two%20different%20primitive,what%20Perl%20does%20by%20default).
# https://youtu.be/_2kY-lHjbh4
# https://www.youtube.com/watch?v=Dkiz0z3bMg0

# What is Regular Expression in Python?
"""
A Regular Expression(RE) in a programming language is a special text string used for describing a search pattern.
It is extremly  useful for extracting information from text such as code, files, log, spreadsheets or even documents.

While using the regular expression the first thing is to recognize is that everything is essentially a character, 
and we are writing patterns to match a specific sequence of characters also referring as string. 
Ascii or latin letters are those that are on your keyboards and Unicode is used to match the foregin text. 
It includes digits and punctuation and all special characters like $#@!%, etc.

The "re" package provides several methods to actually perform queries on an input string.

Note: Based on the regular expressions, Python offers two different primitive operations. 
The match method checks for a match only at the beginning of the string while search checks for a match anywhere in the string.
#####################################################################

re.match() returns after looking only beginning of the string
re.match(pattern, string, flags)

re.search() searches anywhere in the sentence and returns the first occurence
re.search(pattern, string, flags) 
"""
import re

# returns none because only looks at the start of the string
re.match("c", "abcdef")

# re.search()
re.search("c", "abcdef")  # searches anywhere

bool(re.match("c", "abcdef"))  # no match returns boolean false

bool(re.match("a", "abcdef"))  # match returns true

re.search("c", "abcdef")  # tells you where it matched first and only first

re.search("c", "Abcdefc")  # multiple 'c's first instance only

re.search("c", "abcdef\nc")  # multiline works with search

# match doesn't work with newline | re.match only works with the beginning beginning of a string
re.match("c", "abcdef\nc")


# Printing the output of match and search

# Outputs match object <_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.match("a", "abcdef"))

# Outputs a
print(re.match("a", "abcdef").group())  # string output #default value is 0
# Outputs a
print(re.match("a", "abcdef").group(0))  # string output #default value is 0

# Outputs n
print(re.search("n", "abcdefnc abcd").group())

# pull out different types of string depending on the wildcards you use
print(re.search("n.+", "abcdefnc abcd").group())
