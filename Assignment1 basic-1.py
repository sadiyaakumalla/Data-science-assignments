# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:35:49 2024

@author: DELL
"""
#7q
import pandas as pd
import numpy as np
df= pd.read_csv('C:/Users/DELL/Downloads/Q7.csv')
df
Out[1]: 
             Unnamed: 0  Points  Score  Weigh
0             Mazda RX4    3.90  2.620  16.46
1         Mazda RX4 Wag    3.90  2.875  17.02
2            Datsun 710    3.85  2.320  18.61
3        Hornet 4 Drive    3.08  3.215  19.44
4     Hornet Sportabout    3.15  3.440  17.02
5               Valiant    2.76  3.460  20.22
6            Duster 360    3.21  3.570  15.84
7             Merc 240D    3.69  3.190  20.00
8              Merc 230    3.92  3.150  22.90
9              Merc 280    3.92  3.440  18.30
10            Merc 280C    3.92  3.440  18.90
11           Merc 450SE    3.07  4.070  17.40
12           Merc 450SL    3.07  3.730  17.60
13          Merc 450SLC    3.07  3.780  18.00
14   Cadillac Fleetwood    2.93  5.250  17.98
15  Lincoln Continental    3.00  5.424  17.82
16    Chrysler Imperial    3.23  5.345  17.42
17             Fiat 128    4.08  2.200  19.47
18          Honda Civic    4.93  1.615  18.52
19       Toyota Corolla    4.22  1.835  19.90
20        Toyota Corona    3.70  2.465  20.01
21     Dodge Challenger    2.76  3.520  16.87
22          AMC Javelin    3.15  3.435  17.30
23           Camaro Z28    3.73  3.840  15.41
24     Pontiac Firebird    3.08  3.845  17.05
25            Fiat X1-9    4.08  1.935  18.90
26        Porsche 914-2    4.43  2.140  16.70
27         Lotus Europa    3.77  1.513  16.90
28       Ford Pantera L    4.22  3.170  14.50
29         Ferrari Dino    3.62  2.770  15.50
30        Maserati Bora    3.54  3.570  14.60
31           Volvo 142E    4.11  2.780  18.60

df.head()
Out[2]: 
          Unnamed: 0  Points  Score  Weigh
0          Mazda RX4    3.90  2.620  16.46
1      Mazda RX4 Wag    3.90  2.875  17.02
2         Datsun 710    3.85  2.320  18.61
3     Hornet 4 Drive    3.08  3.215  19.44
4  Hornet Sportabout    3.15  3.440  17.02

df['Points'].mean()
Out[3]: 3.5965625

df['Points'].median()
Out[4]: 3.6950000000000003

df['Points'].mode()
Out[5]: 
0    3.07
1    3.92
Name: Points, dtype: float64

df['Points'].std()
Out[6]: 0.5346787360709716

df['Points'].describe()
Out[7]: 
count    32.000000
mean      3.596563
std       0.534679
min       2.760000
25%       3.080000
50%       3.695000
75%       3.920000
max       4.930000
Name: Points, dtype: float64

df['Points'].hist()
Out[8]: <Axes: >
￼

df['Points'].skew()
Out[9]: 0.29278021324083486

df['Score'].mean()
Out[10]: 3.2172500000000004

df['Score'].mode()
Out[11]: 
0    3.44
Name: Score, dtype: float64

df['Score'].var()
Out[12]: 0.9573789677419356

df['Score'].hist()
Out[13]: <Axes: >
￼

df['Score'].skew()
Out[14]: 0.4659161067929858

df['Weigh'].mean()
Out[15]: 17.848750000000003

df['Weigh'].median()
Out[16]: 17.71

df['Weigh'].mode()
Out[17]: 
0    17.02
1    18.90
Name: Weigh, dtype: float64

df['Weigh'].std()
Out[18]: 1.7869432360968431

df['Weigh'].var()
Out[19]: 3.193166129032258

df['Weigh'].describe()
Out[20]: 
count    32.000000
mean     17.848750
std       1.786943
min      14.500000
25%      16.892500
50%      17.710000
75%      18.900000
max      22.900000
Name: Weigh, dtype: float64

df['Weigh'].hist()
Out[21]: <Axes: >
￼

df['Weigh'].skew()
Out[22]: 0.4063466292404903

range_points = df['Points'].max() - df['Points'].min()
range_Score = df['Score'].max() - df['Score'].min()
range_weigh = df['Weigh'].max() - df['Weigh'].min()


print("Range of Points:", range_points)
print("Range of Score:", range_Score)
print("Range of Weig:", range_weigh)
Range of Points: 2.17
Range of Score: 3.9110000000000005
Range of Weig: 8.399999999999999
############################################################################

#9a
import pandas as pd
df1 = pd.read_csv('C:/Users/DELL/Downloads/Q9_a.csv')
df1
Out[24]: 
    Index  speed  dist
0       1      4     2
1       2      4    10
2       3      7     4
3       4      7    22
4       5      8    16
5       6      9    10
6       7     10    18
7       8     10    26
8       9     10    34
9      10     11    17
10     11     11    28
11     12     12    14
12     13     12    20
13     14     12    24
14     15     12    28
15     16     13    26
16     17     13    34
17     18     13    34
18     19     13    46
19     20     14    26
20     21     14    36
21     22     14    60
22     23     14    80
23     24     15    20
24     25     15    26
25     26     15    54
26     27     16    32
27     28     16    40
28     29     17    32
29     30     17    40
30     31     17    50
31     32     18    42
32     33     18    56
33     34     18    76
34     35     18    84
35     36     19    36
36     37     19    46
37     38     19    68
38     39     20    32
39     40     20    48
40     41     20    52
41     42     20    56
42     43     20    64
43     44     22    66
44     45     23    54
45     46     24    70
46     47     24    92
47     48     24    93
48     49     24   120
49     50     25    85

# Calculate Skewness

df1['speed'].skew()
Out[25]: -0.11750986144663393
df1['dist'].skew()
Out[26]: 0.8068949601674215
# Calculate Kurtosis

df1['speed'].kurtosis()
Out[27]: -0.5089944204057617

df1['dist'].kurtosis()
Out[28]: 0.4050525816795765
###############################################################################

#9b
df2= pd.read_csv('C:/Users/DELL/Downloads/Q9_b.csv')
df2
Out[29]: 
    Unnamed: 0          SP         WT
0            1  104.185353  28.762059
1            2  105.461264  30.466833
2            3  105.461264  30.193597
3            4  113.461264  30.632114
4            5  104.461264  29.889149
..         ...         ...        ...
76          77  169.598513  16.132947
77          78  150.576579  37.923113
78          79  151.598513  15.769625
79          80  167.944460  39.423099
80          81  139.840817  34.948615

[81 rows x 3 columns]
# Calculate Skewness

df2['SP'].skew()
Out[30]: 1.6114501961773586

df2['WT'].skew()
Out[31]: -0.6147533255357768

df2['SP'].kurtosis()
Out[32]: 2.9773289437871835

df2['WT'].kurtosis()
Out[33]: 0.9502914910300326
####################################################################
#11qn
import numpy as np
from scipy import stats

stats.norm.interval(0.94,loc=200,scale=30/np.sqrt(2000).round(3))
Out[90]: (198.73831514848644, 201.26168485151356)

stats.norm.interval(0.96,loc=200,scale=30/np.sqrt(2000).round(3))
Out[91]: (198.6222922716631, 201.3777077283369)

stats.norm.interval(0.98,loc=200,scale=30/np.sqrt(2000).round(3))
Out[92]: (198.43942585762338, 201.56057414237662)
#############################################################################
#12q
import numpy as np

scores = [34, 36, 36, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 42,
          42, 45, 49, 56]

mean = np.mean(scores)

median = np.median(scores)

variance = np.var(scores)

standard_deviation = np.std(scores)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard deviation:", standard_deviation)
Mean: 41.0
Median: 40.5
Variance: 24.11111111111111
Standard deviation: 4.910306620885412
###############################################################################
#20q

import pandas as pd

df=pd.read_csv("C:/Users/DELL/Downloads/Cars.csv")
df
Out[9]: 
     HP        MPG  VOL          SP         WT
0    49  53.700681   89  104.185353  28.762059
1    55  50.013401   92  105.461264  30.466833
2    55  50.013401   92  105.461264  30.193597
3    70  45.696322   92  113.461264  30.632114
4    53  50.504232   92  104.461264  29.889149
..  ...        ...  ...         ...        ...
76  322  36.900000   50  169.598513  16.132947
77  238  19.197888  115  150.576579  37.923113
78  263  34.000000   50  151.598513  15.769625
79  295  19.833733  119  167.944460  39.423099
80  236  12.101263  107  139.840817  34.948615

[81 rows x 5 columns]

df.shape
Out[10]: (81, 5)

df.head()
Out[11]: 
   HP        MPG  VOL          SP         WT
0  49  53.700681   89  104.185353  28.762059
1  55  50.013401   92  105.461264  30.466833
2  55  50.013401   92  105.461264  30.193597
3  70  45.696322   92  113.461264  30.632114
4  53  50.504232   92  104.461264  29.889149

df['MPG'].mean()
Out[12]: 34.42207572802469

mpg=df["MPG"]

mpg_data = df['MPG']

print(mpg_data)
0     53.700681
1     50.013401
2     50.013401
3     45.696322
4     50.504232
   
76    36.900000
77    19.197888
78    34.000000
79    19.833733
80    12.101263
Name: MPG, Length: 81, dtype: float64

prob_mpg_greater_than_38 = len(mpg_data[mpg_data > 38]) / len(mpg_data)
print("P(MPG>38):", prob_mpg_greater_than_38)
P(MPG>38): 0.4074074074074074

prob_mpg_less_than_40 = len(mpg_data[mpg_data < 40]) / len(mpg_data)
print("P(MPG<40):", prob_mpg_less_than_40)
P(MPG<40): 0.7530864197530864

prob_mpg_between_20_and_50 = len(mpg_data[(mpg_data > 20) & (mpg_data < 50)]) / len(mpg_data)
print("P(20<MPG<50):", prob_mpg_between_20_and_50)
P(20<MPG<50): 0.8518518518518519
#21(a)
import matplotlib.pyplot as plt
MPG=df["MPG"]
plt.hist(MPG)
plt.show()

￼

df['MPG'].skew()
Out[20]: -0.17794674747025727

df['MPG'].kurtosis()
Out[22]: -0.6116786559430913
###########################################################################
#21(b)
import pandas as pd
import numpy as np
from scipy.stats import shapiro

df1=pd.read_csv("C:/Users/DELL/Downloads/wc-at.csv")
df1
Out[25]: 
      Waist      AT
0     74.75   25.72
1     72.60   25.89
2     81.80   42.60
3     83.95   42.80
4     74.65   29.84
..      ...     ...
104  100.10  124.00
105   93.30   62.20
106  101.80  133.00
107  107.90  208.00
108  108.50  208.00

[109 rows x 2 columns]

df1.head()
Out[26]: 
   Waist     AT
0  74.75  25.72
1  72.60  25.89
2  81.80  42.60
3  83.95  42.80
4  74.65  29.84

df1.hist()
Out[27]: 
array([[<Axes: title={'center': 'Waist'}>,
        <Axes: title={'center': 'AT'}>]], dtype=object)
￼

data = df1['Waist']

stat, p = shapiro(data)

print('Shapiro-Wilk test results:')
print('Statistic:', stat)
print('p-value:', p)
Shapiro-Wilk test results:
Statistic: 0.9558579921722412
p-value: 0.0011704873759299517

if p > 0.05:
    print('The data appears to be normally distributed.')
else:
    print('The data does not appear to be normally distributed.')
The data does not appear to be normally distributed.
##############################################################################
#22q
from scipy.stats import norm

z_90 = norm.ppf(0.95)

# Calculate the Z scores for a 94% confidence interval

z_94 = norm.ppf(0.97)

# Calculate the Z scores for a 60% confidence interval

z_60 = norm.ppf(0.8)

# Print the Z scores

print("Z score for 90% confidence interval:", z_90)
Z score for 90% confidence interval: 1.6448536269514722

print("Z score for 94% confidence interval:", z_94)
Z score for 94% confidence interval: 1.8807936081512509
print("Z score for 60% confidence interval:", z_60)
Z score for 60% confidence interval: 0.8416212335729143
##############################################################################
#23q
from scipy.stats import t

# Sample size

n = 25

# Calculate the t scores for a 95% confidence interval

t_95 = t.ppf(0.975, n-1)

# Calculate the t scores for a 96% confidence interval

t_96 = t.ppf(0.98, n-1)

# Calculate the t scores for a 99% confidence interval