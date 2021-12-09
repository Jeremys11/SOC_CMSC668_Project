from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

survey_len = 26

clf = load('SOC_model.joblib')

#format(age,gender,country,state,selfemp,famhist,treat,workinter,noemp,remote,techcomp,benefits,care,wellprog,help,anonymity,leave,menconsequences,phyconsequences,coworkers,supervisor,meninterview,phyinterview,menvsphy,obsconsq,comments)

object_cols = ['Gender', 'self_employed', 'family_history',
               'work_interfere', 'no_employees', 'remote_work', 'tech_company',
               'benefits', 'care_options', 'wellness_program', 'seek_help',
               'anonymity', 'leave1', 'mental_health_consequence',
               'phys_health_consequence', 'coworkers', 'supervisor',
               'mental_health_interview', 'phys_health_interview',
               'mental_vs_physical', 'obs_consequence']

                #age country state comments family history

values = ['Male','No','No','No','10','No','Yes','Yes','Yes','Yes','Yes','Yes','Yes','No','No','Yes','No','No','Yes','Yes','Yes']

df = {}
#label_encoder = LabelEncoder()
counter = 0
for i in object_cols:
    #label_encoder.fit(df[i])
    df[i] = values[counter]
    counter += 1

#print("nonono")
#df = pd.DataFrame.from_dict(df)

#print('here')
#d.items(), columns=['Date', 'DateValue']

#predict = clf.predict(df.items(), index=[0])
#print(predict)
temp = []
for i in range(22):
    temp.append(6)

temp = [temp]
#temp.reshape(1,-1)
print(clf.predict(temp))