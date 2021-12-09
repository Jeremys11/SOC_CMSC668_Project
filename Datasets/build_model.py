
import pymysql as pymysql
import pandas as pd

db_connection = pymysql.connect(host='localhost', database='SOC', user='root', password='mansipatel')
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM survey')

table_rows = db_cursor.fetchall()
# result = cur.fetchall()
num_fields = len(db_cursor.description)
field_names = [i[0] for i in db_cursor.description]
# print(field_names)
# columns = db_cursor.description
# result = [{columns[index][0]:column for index, column in enumerate(value)} for value in db_cursor.fetchall()]

df = pd.DataFrame(table_rows, columns=field_names)
# print(db_cursor.column_names)
# df = pd.read_csv("/Users/mansi/Documents/UMBC/Fall 2021/SOC/Datasets/TestFile.csv")
print(df)
# In[142]:

# df.drop(columns=['Timestamp', 'Country', 'state', 'comments'], inplace=True)
df.drop(columns=['id','treatment','Country', 'state', 'comments'], inplace=True)

# In[143]:


# df.drop(df[df['Age'] < 0].index, inplace=True)
# df.drop(df[df['Age'] > 100].index, inplace=True)
df['Age'].unique()

df['Gender'].replace(['Male ', 'male', 'M', 'm', 'Male', 'Cis Male',
                      'Man', 'cis male', 'Mail', 'Male-ish', 'Male (CIS)',
                      'Cis Man', 'msle', 'Malr', 'Mal', 'maile', 'Make', ], 'Male', inplace=True)

df['Gender'].replace(['Female ', 'female', 'F', 'f', 'Woman', 'Female',
                      'femail', 'Cis Female', 'cis-female/femme', 'Femake', 'Female (cis)',
                      'woman', ], 'Female', inplace=True)

df["Gender"].replace(['Female (trans)', 'queer/she/they', 'non-binary',
                      'fluid', 'queer', 'Androgyne', 'Trans-female', 'male leaning androgynous',
                      'Agender', 'A little about you', 'Nah', 'All',
                      'ostensibly male, unsure what that really means',
                      'Genderqueer', 'Enby', 'p', 'Neuter', 'something kinda male?',
                      'Guy (-ish) ^_^', 'Trans woman', ], 'Other', inplace=True)

df['Gender'].value_counts()

# In[148]:


df['work_interfere'] = df['work_interfere'].fillna('Don\'t know')
print(df['work_interfere'].unique())

# In[149]:


df['self_employed'] = df['self_employed'].fillna('No')
print(df['self_employed'].unique())

# In[150]:


print(df.isnull().sum())

# In[151]:


list_col = ['Age', 'Gender', 'self_employed', 'family_history',
            'work_interfere', 'no_employees', 'remote_work', 'tech_company',
            'benefits', 'care_options', 'wellness_program', 'seek_help',
            'anonymity', 'leave1', 'mental_health_consequence',
            'phys_health_consequence', 'coworkers', 'supervisor',
            'mental_health_interview', 'phys_health_interview',
            'mental_vs_physical', 'obs_consequence']

for col in list_col:
    print('{} :{} '.format(col.upper(), df[col].unique()))

from sklearn.preprocessing import LabelEncoder

object_cols = ['Gender', 'self_employed', 'family_history',
               'work_interfere', 'no_employees', 'remote_work', 'tech_company',
               'benefits', 'care_options', 'wellness_program', 'seek_help',
               'anonymity', 'leave1', 'mental_health_consequence',
               'phys_health_consequence', 'coworkers', 'supervisor',
               'mental_health_interview', 'phys_health_interview',
               'mental_vs_physical', 'obs_consequence']
label_encoder = LabelEncoder()
for col in object_cols:
    label_encoder.fit(df[col])
    df[col] = label_encoder.transform(df[col])
df.columns

# In[138]:
# import load
from joblib import dump, load


clf = load('SOC_model.joblib')


predict = clf.predict(df)
print(predict)
# predict = model.predict(df)
# predict

