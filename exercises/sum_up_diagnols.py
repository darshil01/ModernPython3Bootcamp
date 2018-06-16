'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
];
 
sum_up_diagonals(list1); # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
];
 
sum_up_diagonals(list2); # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
];

sum_up_diagonals(list3); # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
];
 
sum_up_diagonals(list4); # 68
'''
import pdb

def sum_up_diagonals(lst1):
    hnw = len(lst1)
    nums_to_sum = []
    for x in range(hnw):
        nums_to_sum.append(lst1[x][x])
        nums_to_sum.append(lst1[x][-1 - x])
    return sum(nums_to_sum)

list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]

print(sum_up_diagonals(list1)) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
print(sum_up_diagonals(list2)) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

print(sum_up_diagonals(list3)) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
print(sum_up_diagonals(list4)) # 68

