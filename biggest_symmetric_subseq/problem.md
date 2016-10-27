Given a string that consists of numeric characters from ′0′ to ′9′. A string c is called a substring of the string a if it is possible to delete some characters from a to obtain c. For example, ‘ac’ is a substring of ‘abc’ because we can obtain ‘ac’ by deleting character ‘b’ from ‘abc’. A string x = c1c2 ... cL with length L is called symmetric if the string x and its reversed string cL cL−1 ... c1 are the same.

#### Requirements: 
- Write a program that find the symmetric substring that represents largest value. This string cannot have 0 as its first character unless it has only 1 character.

#### Input: 
- The first line is the positive integer L which is the length of the string (1 ≤ L ≤ 2 000). 
- The second line is the given string consists of L characters from ‘0’ to ‘9’.

#### Output: 
- Print the symmetric substring that represents largest value.

### FOR EXAMPLE: 
#### Input: 
6 
128921

#### Output: 
12921 
