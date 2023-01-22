import pandas as pd

# panda read file
p = pd.read_csv(
    './metrics/g_failsize1495.csv',
    header=None,
    names=['id', 'fail size'],
)

# print(p)

# creating data frame
p = pd.DataFrame(p, columns=['id', 'fail size'])
# converting to csv file
p.to_csv('./metrics/p_failsize1495.csv', index=False)
