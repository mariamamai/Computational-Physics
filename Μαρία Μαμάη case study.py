import numpy as np
import pandas as pd
import matplotlib as plt

data=pd.read_excel('weather_data.xlsx')
df=pd.DataFrame(data)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
#print(df)




#Ερώτημα 1ο

#κάλυψη των κενών κελιών των στηλών HIGH,LOW με κυβική παρεμβολή
#print(df.loc[:,['HIGH','LOW']])
df['LOW']=df["LOW"].fillna(df["LOW"].interpolate(method="cubic"))
df['HIGH']=df["HIGH"].fillna(df["HIGH"].interpolate(method="cubic"))

#κάλυψη των κενών κελιών της στήλης MONTH με την συμβολοσειρά DEC
#print(df.loc[:,['MONTH']])
df['MONTH']=df['MONTH'].fillna("DEC")




#Ερώτημα 2ο

#μέγιστη θερμοκρασία στην στήλη HIGH
df.loc['EXTRAS','HIGH']=df['HIGH'].max()
#print(df.loc[:,['HIGH']])

#ελάχιστη θερμοκρασία στην στήλη LOW
df.loc['EXTRAS','LOW']=df['LOW'].min()
#print(df.loc[:,['LOW']])

#μέγιστη ένταση ανέμου στην στήλη WINDHIGH
df.loc['EXTRAS','WINDHIGH']=df['WINDHIGH'].max()
#print(df.loc[:,['WINDHIGH']])

#μέση θερμοκρασία στην στήλη TEMP
df.loc['EXTRAS','TEMP']=df['TEMP'].mean()
#print(df.loc[:,['TEMP']])

#συνολικά εκατοστά βροχόπτωσης στην στήλη RAIN
df.loc['EXTRAS','RAIN']=df['RAIN'].sum()
#print(df.loc[:,['RAIN']])

#συνολικά εκατοστά βροχόπτωσης στην στήλη RAIN
df.loc['EXTRAS','RAIN']=df['RAIN'].sum()
#print(df.loc[:,['RAIN']])

#άθροισμα στην στήλη HDD
df.loc['EXTRAS','HDD']=df['HDD'].sum()
#print(df.loc[:,['HDD']])

#άθροισμα στην στήλη CDD
df.loc['EXTRAS','CDD']=df['CDD'].sum()
#print(df.loc[:,['CDD']])




#Ερώτημα 3ο

#διάμεσος της στήλης TEMP
print(df['TEMP'].median())

#τυπική απόκλιση της στήλης TEMP
print(df['TEMP'].std())




#Ερώτημα 4ο

df1=pd.DataFrame(df['DIR'])
#print(df1)
df1.groupby('DIR')
gp=df1.groupby('DIR')
#print(gp)
A=gp.get_group('N').count()
B=gp.get_group('E').count()
C=gp.get_group('S').count()
D=gp.get_group('W').count()
E=gp.get_group('NW').count()
F=gp.get_group('NE').count()
G=gp.get_group('SW').count()
H=gp.get_group('SE').count()
I=gp.get_group('NNW').count()
J=gp.get_group('WNW').count()
K=gp.get_group('ENE').count()
L=gp.get_group('SSW').count()
M=gp.get_group('WSW').count()
N=gp.get_group('SSE').count()
O=gp.get_group('ESE').count()
print('Ο βόρειος άνεμος N φύσουσε ', A , 'μέρες \n')  
print('Ο ανατολικός άνεμος E φύσουσε ', B , 'μέρες\n')  
print('Ο νότιος άνεμος S φύσουσε ', C , 'μέρες\n')  
print('Ο δυτικός άνεμος W φύσουσε ', D , 'μέρες\n')  
print('Ο βορειοδυτικός άνεμος NW φύσουσε ', E , 'μέρες\n')  
print('Ο βορειοανατολικός άνεμος NE φύσουσε ', F , 'μέρες\n')  
print('Ο νοτικοδυτικός άνεμος SW φύσουσε ', G , 'μέρες\n')  
print('Ο νοτιοανατολικός άνεμος SE φύσουσε ', H , 'μέρες\n')  
print('Ο βόρειος-βορειοδυτικός άνεμος NNW φύσουσε ', I , 'μέρες\n')  
print('Ο δυτικός-βορειοδυτικός άνεμος WNW φύσουσε ', J , 'μέρες\n')  
print('Ο ανατολικός-βορειοανατολικός άνεμος ENE φύσουσε ', K , 'μέρες\n')  
print('Ο νότιος-νοτιοδυτικός άνεμος SSW φύσουσε ', L , 'μέρες\n')  
print('Ο δυτικός-νοτιοδυτικός άνεμος WSW φύσουσε ', M , 'μέρες\n')  
print('Ο νότιος-νοτιοανατολικός άνεμος SSE φύσουσε ', N , 'μέρες\n')  
print('Ο ανατολικός-νοτιοανατολικός άνεμος ESE φύσουσε ', O , 'μέρες')  

#διάγραμμα
import matplotlib.pyplot as pyplt
df2=pd.DataFrame({'Διεύθυνση':['N','E','S','W','NW','NE','SW','SE','NNW','WNW','ENE','SSW','WSW','SSE','ESE'],'Ημέρες':[103,5,31,19,14,4,28,65,9,20,2,22,17,11,15]})
pyplt.pie(df2['Ημέρες'],labels=df2['Διεύθυνση'],shadow=False,autopct='%1.1f%%')




#Ερώτημα 5ο

#η ώρα με τις μερισσότερες μέγιστες θερμοκρασίες στην στήλη TIME. Η τιμή φαίνεται στην ένδειξη top
print(df['TIME'].describe())
#top       15:20:00

#η ώρα με τις μερισσότερες ελάχιστες θερμοκρασίες στην στήλη TIME.1. Η τιμή φαίνεται στην ένδειξη top
print(df['TIME.1'].describe())
#top       00:00:00




#Ερώτημα 6ο

df['TEMPVAR']=df['HIGH']-df['LOW']
df['TEMPVAR']

dayofyear=pd.DataFrame({'month':df['MONTH'],'day':df['DAY']})
dayofyear['Day Of Year']=dayofyear['month'] + dayofyear['day'].astype(str)
#print(dayofyear)

vartem=pd.DataFrame({'DAY':dayofyear['Day Of Year'],'Var':df['TEMPVAR']})
#print(vartem)
vartem.groupby('Var').max()
print('Η μέρα με την μεγαλύτερη διακύμανση θερμοκρασίας είναι η 13η Μαΐου, με διακύμανση 15.6 βαθμούς')




#Ερώτημα 7ο

grouped_dir = dict(df.groupby('DIR')['WINDHIGH'].max())
print(grouped_dir)




#Ερώτημα 8ο

dir_max = np.array( df.groupby('DIR').max())
y = dir_max[0,0:2]
print(y)




#Ερώτημα 9ο

#η μέση θερμοκρασία για κάθε διεύθυνση 
windir=df.groupby('DIR').mean()
windir[['TEMP']]
print(windir[['TEMP']].min())
print('Η διεύθυνση του ανέμου με την μικρότερη μέση θερμοκρασία ήταν ο βορειοδυτικός άνεμος NW\n')
print(windir[['TEMP']].max())
print('Η διεύθυνση του ανέμου με την μεγαλύτερη μέση θερμοκρασία ήταν ο νοτιοδυτικός άνεμος SW')




#Ερώτημα 10ο

#ραβδόγραμμα βροχοπτώσεων/μήνα
mrain=df.groupby('MONTH').mean()
df3=mrain[['RAIN']]
df3.plot(kind='bar',y='RAIN')   




#Ερώτημα 11ο






#Ερώτημα 12ο

#ΑΝΟΙΞΗ

df['day of year']=df['MONTH']+df['DAY'].astype(str)
df['day of year']
dayspring=df.iloc[59:151,15]
meanspring=df.iloc[59:151,2]
highspring=df.iloc[59:151,3]
lowspring=df.iloc[59:151,5]


ax=pyplt.subplot(111)
ax.plot(dayspring,meanspring,'g-',label='Mean Temp')
ax.plot(dayspring,highspring,'r',label='Max Temp')
ax.plot(dayspring,lowspring,'b--',label='Min Temp')
pyplt.title('Spring')
pyplt.xlabel('Month-Day')
pyplt.ylabel('Celsius')
pyplt.legend(loc='upper left')
pyplt.show()
                        

#ΚΑΛΟΚΑΙΡΙ

daysummer=df.iloc[151:243,15]
meansummer=df.iloc[151:243,2]
highsummer=df.iloc[151:243,3]
lowsummer=df.iloc[151:243,5]


ax=pyplt.subplot(111)
ax.plot(daysummer,meansummer,'g-',label='Mean Temp')
ax.plot(daysummer,highsummer,'r',label='Max Temp')
ax.plot(daysummer,lowsummer,'b--',label='Min Temp')
pyplt.title('Summer')
pyplt.xlabel('Month-Day')
pyplt.ylabel('Celsius')
pyplt.legend(loc='upper left')
pyplt.show()


#ΦΘΙΝΟΠΩΡΟ

dayfall=df.iloc[243:334,15]
meanfall=df.iloc[243:334,2]
highfall=df.iloc[243:334,3]
lowfall=df.iloc[243:334,5]


ax=pyplt.subplot(111)
ax.plot(dayfall,meanfall,'g-',label='Mean Temp')
ax.plot(dayfall,highfall,'r',label='Max Temp')
ax.plot(dayfall,lowfall,'b--',label='Min Temp')
pyplt.title('Fall')
pyplt.xlabel('Month-Day')
pyplt.ylabel('Celsius')
pyplt.legend(loc='upper right')
pyplt.show()


#ΧΕΙΜΩΝΑΣ

daywinter1=df.iloc[:59,15]
daywinter2=df.iloc[334:365,15]

meanwinter1=df.iloc[:59,2]
meanwinter2=df.iloc[334:365,2]

highwinter1=df.iloc[:59,3]
highwinter2=df.iloc[334:365,3]

lowwinter1=df.iloc[:59,5]
lowwinter2=df.iloc[334:365,5]

ax=pyplt.subplot(111)
ax.plot(daywinter1,meanwinter1,'g-',label='Mean Temp')
ax.plot(daywinter2,meanwinter2,'g-')
ax.plot(daywinter1,highwinter1,'r',label='Max Temp')
ax.plot(daywinter2,highwinter2,'r')
ax.plot(daywinter1,lowwinter1,'b--',label='Min Temp')
ax.plot(daywinter2,lowwinter2,'b--')
pyplt.title('Winter')
pyplt.xlabel('Month-Day')
pyplt.ylabel('Celsius')
pyplt.legend(loc='lower right')
pyplt.show()




#Ερώτημα 13ο


def posovroxis(x):
    if x<400:
        print('Λειψυδρία')
    elif x>=400 and x<600:
        print('Ικανοποιητικά ποσά βροχής')
    else:
        print('Υπερβολική βροχόπτωση')

rainsum=df['RAIN'].sum()
posovroxis(rainsum)
