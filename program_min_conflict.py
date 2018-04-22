f = open('input.txt', 'r')
Group_count = f.readline().strip('\n')
Pot_count = f.readline().strip('\n')
pot={}
for i in range(int(Pot_count)):
     l=f.readline().strip('\n')
     pot["Pot"+str(i+1)] =l.split(',')

conf={}
for i in range(6):
  t= f.readline().strip('\n')
  m = t.split(':', 2)
  conf[m[0]] = m[1].split(',')
p=[]
r=[]
for k in pot:
   r.append(int(k[3:]))
r.sort()
for x in r:
    p.append('Pot'+str(x))
f.close()
import sys
dict_final={}
#dict_final is a dictionary with country name as key and value as a string storing the pot and confederation value
for i in range(len(p)):
  if p[i] in pot:
      for x in pot[p[i]]:
        if x in conf['AFC']:
            dict_final.update({x:str(i+1)+'A'})
        elif x in conf['CAF']:
            dict_final.update({x: str(i + 1) + 'B'})
        elif x in conf['CONCACAF']:
            dict_final.update({x: str(i + 1) + 'C'})
        elif x in conf['CONMEBOL']:
            dict_final.update({x: str(i + 1) + 'D'})
        elif x in conf['OFC']:
            dict_final.update({x: str(i + 1) + 'E'})
        elif x in conf['UEFA']:
            dict_final.update({x: str(i + 1) + 'F'})
m=[]
for b in range(int(Group_count)):
    m.append('Group'+str(b+1))
from copy import deepcopy
reman_dict = deepcopy(dict_final) # reman_dict is a copy of dict_final which stores the remainig elements
# print dict_final
def nconflict(group_no,country,label):
    # Counts the number of conflicts for a particular group_no. for a particular element with country and label provided
    #Also returns the list of elements responsible for conflicts
    global d_out
    if not d_out[group_no]:
        conflict =0
        conf_elements_grp=[]
        return conflict, conf_elements_grp
    else:
      i=0
      conflict = 0
      conf_elements_grp = []
      for y in d_out[group_no]:
          el =d_out[group_no][y] # stores '4A'
          if (label[0]==el[0]) and (label[1]==el[1]):
              conflict= sys.maxint
              conf_elements_grp.append(y)
          if (label[0]!=el[0]) and (label[1]==el[1]):
              if label[1] != 'F':
                  conflict= conflict+1
                  conf_elements_grp.append(y)
              elif label[1] == 'F':
                  i=i+1
                  if i==1:
                      temp = y
                  if i==2:
                      conflict= conflict+1
                      conf_elements_grp.append(y)
                      conf_elements_grp.append(temp)
          if (label[0]==el[0]) and (label[1]!=el[1]):
              conflict = conflict + 1
              conf_elements_grp.append(y)
      return conflict,conf_elements_grp
def find_group_min_conflict(country , label):
    # Calculates the conflicts of a patricular popped out element with all the groups and returns the minimum conflict group number,
    # minimum conflict value and the elements responsible for conflict
    global m
    global d_out
    conf_dict=[] # stores values of the group conflicts ie 4,0..etc
    conf_elements_all=[] # stores the list of elements responsible for conflict for all groups(list of lists)
    for k in m: # group1 etc list
        if k in d_out:
           (val,conf_elements_grp) = nconflict(k, country , label) # for each group we calculate the number of conflicts for the given country and value
           conf_dict.append(val)
           conf_elements_all.append(conf_elements_grp)
    min_value = min(conf_dict)
    min_index = conf_dict.index(min(conf_dict))
    conf_elements = conf_elements_all[min_index]                             # elements giving conflict in minimum conflict grp
    return min_index+1, min_value ,conf_elements # this is the group number

def main_min_conflict(reman_dict_1):
    global m # list of group numbers
    global j
    global d_out
    j=j+1
    if j== 700:
        return 'No'
    else:
      if not reman_dict_1:
        return 'Yes'
      else:
            pop_item = reman_dict_1.popitem()
            (min_group_number, min_value_group , conf_elements) = find_group_min_conflict(pop_item[0],pop_item[1])
            if (min_value_group == sys.maxint):
                if reman_dict_1:
                  return 'No'
            if (min_value_group == 0):
                d_out['Group'+str(min_group_number)][pop_item[0]]=pop_item[1]
                return main_min_conflict(reman_dict_1)
            elif (min_value_group > 0):
                if min_value_group == 1:
                    #update the remaining values as the removed one from the final output
                    for x in conf_elements:
                      reman_dict_1.update({x: d_out['Group'+str(min_group_number)][x]})
                    d_out['Group' + str(min_group_number)][pop_item[0]] = pop_item[1]
                    for x in conf_elements:
                      del d_out['Group'+str(min_group_number)][x]
                    return main_min_conflict(reman_dict_1)
                if min_value_group == 2:
                    for x in conf_elements:
                       reman_dict_1.update({x: d_out['Group' + str(min_group_number)][x]})
                    d_out['Group' + str(min_group_number)][pop_item[0]] = pop_item[1]
                    for x in conf_elements:
                       del d_out['Group' + str(min_group_number)][x]
                    return main_min_conflict(reman_dict_1)
from collections import defaultdict
global d_out
#d_out is a dictionary of dictionary with the first key indicating the group number,
# and the inside dictionary contains the country name as key and value as a string indicating its pot and confederation
d_out = defaultdict(dict)
for k in m:
    d_out[k] = dict()

j=0
out = main_min_conflict(dict_final)
f = open('output.txt','w')
if out == 'Yes':
    f.write(str(out) + '\n')
    # print d_out
    for c in m:
        if not d_out[c]:
           f.write(str(None))
           f.write('\n')
        else:
          f.write(','.join(str(k) for k in d_out[c]))
          f.write('\n')
elif out == 'No':
    f.write(str(out))
f.close()

