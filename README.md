# Min-conflict-for-FIFA-team-distribution
Dividing the user defined teams into groups based on the user specified pots and confederation of the teams

Refer to problem description to know more about the problem!

# INPUT FILE FORMAT:

GROUP COUNT: The number of groups for the 2018 FIFA World Cup draw.

POT COUNT: The number of pots for the 2018 FIFA World Cup draw.

POTS DIVISION: It contains POTS COUNT lines, where the first line is a
comma-separated list of the teams belonging to Pot 1, and the following lines show the
teams of Pots 2 to POTS COUNT, respectively.
  
TEAMS CONFEDERATION: It contains 6 lines where each line begins with the
name of one of the continental confederations (AFC, CAF, CONCACAF, CONMEBOL,
OFC, or UEFA) followed by a colon “:” and then the names of the teams from this
continental confederation separated by commas “,”. If there is no team from a
continental confederation, it is denoted by “None”.

# Sample input
8  
4  
Russia,Germany,Brazil,Portugal,Argentina,Belgium,Poland,France  
Spain,Peru,Switzerland,England,Colombia,Mexico,Uruguay,Croatia  
Denmark,Iceland,Costa Rica,Sweden,Tunisia,Egypt,Senegal,Iran  
Serbia,Nigeria,Australia,Japan,Morocco,Panama,South Korea,Saudi Arabia  
AFC:South Korea,Saudi Arabia,Iran,Japan,Australia   
CAF:Tunisia,Egypt,Senegal,Morocco,Nigeria 
CONCACAF:Mexico,Panama,Costa Rica  
CONMEBOL:Brazil,Argentina,Uruguay,Colombia,Peru  
UEFA:France,Germany,England,Russia,Portugal,Belgium,Poland,Switzerland,Croatia,Denmark,Iceland,Serbia,Spain,Sweden  
OFC:None  

# OUTPUT FORMAT:

<YES/NO> : A single line containing “Yes” or “No” to indicate whether or not there is a
solution for this instance of the 2018 FIFA World Cup draw. 

A SOLUTION : If there is a solution, then the program provides just one of the possible
solutions. In this case, after the first line (which is “Yes”), the program output contains
GROUP COUNT number of lines, where the first line indicates the names of
teams for group 1 separated by commas “,” and so on for groups 2 to GROUP
COUNT. If there is no team in a specific group, the output displays “None” for the line
corresponding to that group.

# Output for the Sample input
Yes
Brazil,Denmark,Croatia,Morocco  
Poland,Costa Rica,Peru,Nigeria  
Mexico,Sweden,Australia,France  
Switzerland,Serbia,Argentina,Iran  
Tunisia,Japan,England,Russia  
Iceland,South Korea,Portugal,Uruguay  
Egypt,Panama,Germany,Colombia  
Belgium,Senegal,Saudi Arabia,Spain  

# Illustration for Sample input:
In order to make the problem description clearer, consider the following example with 32  
national teams which are supposed to be divided into 8 groups. The classification of  
teams based on their continental confederations has been shown in the figure below.   

