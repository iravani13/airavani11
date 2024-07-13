import lab4a

set1 = {1,2,3,4,5}
set2 = {2,1,0,-1,-2}
print (lab4a.join_sets(set1,set2))
# Will output {-2, -1, 0, 1, 2, 3, 4, 5}
print (lab4a.match_sets(set1,set2))
# Will output {1, 2}
print (lab4a.diff_sets(set1,set2))
# Will output {-2, -1, 0, 3, 4, 5}
