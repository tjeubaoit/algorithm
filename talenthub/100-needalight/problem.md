Brad is having some problem with the light bulbs. They could not be switched off normally. There are n light bulbs in his house, each connected with a switch. Currently, one switch has malfunctioned and there are only n-1 switches available. Things get complicated when Brad uses switch i but has the modes of both light bulbs i and i+1 changed at the same time, in opposite manners (one from on to off, the other from off to on and vice versa). Brad wants to have all the light turned off, however it costs a certain amount of money everytime a light bulb is turned on or off, and his family is trying to lower the electricity bill. He wants to spend as little money as possible. Let's help Brad.

Given that the costs for turning on/ off of the light bulbs does not exceed 100.

Input:

+ The first line contains an integer N ( n <= 16), followed by n lines, in which line i contains 2 values as the costs for turning on and turning off light bulb i.

+ The last line contains n numbers representing current modes of the light bulbs (valued as 0 if turned on and 1 if turned off).

Output:

+ Print the minimum cost, otherwise "INF".

Example:
Input
5
1 1
1 1
1 1
1 1
1 1
0
1
0
0
1

Output
6