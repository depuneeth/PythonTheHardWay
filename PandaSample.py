import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

#file_1 = pd.read_csv(r"C:\Users\raviteja\Desktop\innercity.csv")

#file_1.to_csv("pandacsv.csv")

df_city = pd.read_csv("pandacsv.csv")
#print(df_city.head())

#print("total no of rows and columns:",df_city.shape)

#df_city.info()
#print(*list(df_city.room_bed.unique()))
#print(*list(df_city.basement.unique()))

"""df_city['yr_sold']=df_city['dayhours'].apply(lambda x:x[:4]).astype(int)
print(df_city.head())

#ccreating a new column
df_city['age sold']=df_city.yr_sold-df_city.yr_built
print(df_city.head())

#total num of rows n columns
print(df_city.shape)

#rows containing duplicate data
duplicate_rows_df=df_city[df_city.duplicated()]
print("no of duplicate rows: ",duplicate_rows_df.shape)

##we have certain features that are displayed as integer, but we know that we need to fix them into categories
df_city.coast=pd.Categorical(df_city.coast)
df_city.condition=pd.Categorical(df_city.condition)
df_city.quality=pd.Categorical(df_city.quality)
df_city.furnished=pd.Categorical(df_city.furnished)
df_city.sight=pd.Categorical(df_city.sight)

print(df_city.info())

print(df_city.describe().T)#only displays numeric columns

Q1=df_city.room_bed.quantile(.25)
Q3=df_city.room_bed.quantile(.75)
IQR = Q3-Q1
lower_limit=Q1-(1.5*IQR)
upper_limit=Q3+(1.5*IQR)
print("Min Value",df_city.room_bed.min())
print("Max Value ",df_city.room_bed.max())
print("Q1 ",Q1)
print("Q3 ",Q3)
print("IQR ",IQR)
print('lower_limit',lower_limit)
print('upper_limit',upper_limit)
"""

def findoutliers(column):
    outliers = []
    Q1 = column.quantile(.25)
    Q3 = column.quantile(.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)
    for out1 in column:
        if out1 > upper_limit or out1 < lower_limit:
            outliers.append(out1)

    return np.array(outliers)


def plotchart(col):
    fix, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 5))
    sn.boxplot(col, orient='v', ax=ax1)
    ax1.set_ylabel = col.name
    ax1.set_title('Box plot of {}'.format(col.name))
    sn.distplot(col, ax=ax2)
    ax2.set_title('Distribution plot of {}'.format(col.name))


def analysis_column(col):
    print('count of outlier ', len(findoutliers(col)))
    print('Mean ', format(col.mean()))
    print('Median ', format(col.median()))
    print('Missing values', format(col.isnull().sum()))
    print('% of Missing values', format(round(100 * (col.isnull().sum() / len(col)), 2)))

    plotchart(col)

#print(findoutliers(df_city.room_bed))

len(findoutliers(df_city.room_bed))

# to check missing value
sn.heatmap(df_city.isnull(), cbar=False, yticklabels=False, cmap='viridis')





