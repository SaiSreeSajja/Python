from calendar import *
print(month(2003,10))
print(calendar(2003,3,1,9))
print(leapdays(1980,2024))
print(isleap(2020))

'''
output:
    October 2003    
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31      

                                                2003

          January                             February                             March
Mon Tue Wed Thu Fri Sat Sun         Mon Tue Wed Thu Fri Sat Sun         Mon Tue Wed Thu Fri Sat Sun
          1   2   3   4   5                               1   2                               1   2
  6   7   8   9  10  11  12           3   4   5   6   7   8   9           3   4   5   6   7   8   9
 13  14  15  16  17  18  19          10  11  12  13  14  15  16          10  11  12  13  14  15  16
 20  21  22  23  24  25  26          17  18  19  20  21  22  23          17  18  19  20  21  22  23
 27  28  29  30  31                  24  25  26  27  28                  24  25  26  27  28  29  30
                                                                         31

           April                                May                                 June
Mon Tue Wed Thu Fri Sat Sun         Mon Tue Wed Thu Fri Sat Sun         Mon Tue Wed Thu Fri Sat Sun
  7   8   9  10  11  12  13           5   6   7   8   9  10  11           2   3   4   5   6   7   8
 14  15  16  17  18  19  20          12  13  14  15  16  17  18           9  10  11  12  13  14  15
 21  22  23  24  25  26  27          19  20  21  22  23  24  25          16  17  18  19  20  21  22
 28  29  30                          26  27  28  29  30  31              23  24  25  26  27  28  29
                                                                         30

            July                               August                            September
Mon Tue Wed Thu Fri Sat Sun         Mon Tue Wed Thu Fri Sat Sun         Mon Tue Wed Thu Fri Sat Sun
      1   2   3   4   5   6                           1   2   3           1   2   3   4   5   6   7
  7   8   9  10  11  12  13           4   5   6   7   8   9  10           8   9  10  11  12  13  14
 14  15  16  17  18  19  20          11  12  13  14  15  16  17          15  16  17  18  19  20  21
 21  22  23  24  25  26  27          18  19  20  21  22  23  24          22  23  24  25  26  27  28
 28  29  30  31                      25  26  27  28  29  30  31          29  30

          October                             November                            December
Mon Tue Wed Thu Fri Sat Sun         Mon Tue Wed Thu Fri Sat Sun         Mon Tue Wed Thu Fri Sat Sun
          1   2   3   4   5                               1   2           1   2   3   4   5   6   7
  6   7   8   9  10  11  12           3   4   5   6   7   8   9           8   9  10  11  12  13  14
 13  14  15  16  17  18  19          10  11  12  13  14  15  16          15  16  17  18  19  20  21
 20  21  22  23  24  25  26          17  18  19  20  21  22  23          22  23  24  25  26  27  28
 27  28  29  30  31                  24  25  26  27  28  29  30          29  30  31

11
True
'''