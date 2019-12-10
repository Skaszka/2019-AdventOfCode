# no a/b here because it's trivial to get back to a

sum = 0
for i in range(134792,675810):
              str_i = str(i)
              prev = str_i[0]
              adjacent_flag = 0
              decrease_flag = 0
              for j in range(1,len(str_i)):
                           if str_i[j]<prev:   # it decreased
                                         decrease_flag = 1
                                         break
                           elif (str_i[j]==prev) and (prev*3 not in str_i):    # there's a double but not more than a double
                                         adjacent_flag = 1
                           prev = str_i[j]
              if (decrease_flag==1 or adjacent_flag==0):
                           continue
              sum += 1
print(sum)