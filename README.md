# Min-conflict-for-FIFA-team-distribution
Dividing the user defined teams into groups based on the user specified pots and confederation of the teams

Refer to problem description to know more about the problem!

The INPUT FILE FORMAT given to the program is of the form:

<GROUP COUNT>: The number of groups for the 2018 FIFA World Cup draw.
<POT COUNT>: The number of pots for the 2018 FIFA World Cup draw.
<POTS DIVISION>: It contains <POTS COUNT> lines, where the first line is a
comma-separated list of the teams belonging to Pot 1, and the following lines show the
teams of Pots 2 to <POTS COUNT>, respectively.
<TEAMS CONFEDERATION>: It contains 6 lines where each line begins with the
name of one of the continental confederations (AFC, CAF, CONCACAF, CONMEBOL,
OFC, or UEFA) followed by a colon “:” and then the names of the teams from this
continental confederation separated by commas “,”. If there is no team from a
continental confederation, it is denoted by “None”.


INTERPRET THE OUTPUT OF THE PROGRAM AS:

<YES/NO> : A single line containing “Yes” or “No” to indicate whether or not there is a
solution for this instance of the 2018 FIFA World Cup draw. 

<A SOLUTION> : If there is a solution, then the program provides just one of the possible
solutions. In this case, after the first line (which is “Yes”), the program output contains
<GROUP COUNT> number of lines, where the first line indicates the names of
teams for group 1 separated by commas “,” and so on for groups 2 to <GROUP
COUNT>. If there is no team in a specific group, the output displays “None” for the line
corresponding to that group.
