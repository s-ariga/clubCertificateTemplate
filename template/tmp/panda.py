import pandas as pd 
#df = pd.DataFrame([[1,2,3],[4,5,6]])

#print(df[0])
#print(df)

#data = {'score':[10, 20, 30, 40, 50], 'team':['AAA', 'BBB', 'CCC','DDD','EEE']}

#df = pd.DataFrame(data)
#print(df)

#print(df['score'])#
#for col in df:
#    print(col)

#for row in df.iterrows():
#    print(row)
#    print(row[0])
#    print(row[1])

df = pd.read_excel("../../results/team_all.xlsx")

print(df)
print("###\n")

for col in df:
    print(col)
    
print("###\n")

rank = df.loc[df['Rank'] == 1]

print(rank)

print("###\n")

for index, item in df.iterrows():
    print(index)
    print(item)
    print("Score : {0}".format(item['Score']))


'''
dt = df.T

print(dt)

for d in dt:
    print(d['Score'])
)))
'''
