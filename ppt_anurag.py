from matplotlib import pyplot as plt
import pandas as pd
gender=['male', 'female']
d=pd.read_csv('hr.csv')
clean=d.loc[:,['Gender','JobSatisfaction','RelationshipSatisfaction']]
grouped=clean.groupby(['Gender']).sum()

male_job=grouped['JobSatisfaction']['Male']
female_job=grouped['JobSatisfaction']['Female']

male_relation=grouped['RelationshipSatisfaction']['Male']
female_relation=grouped['RelationshipSatisfaction']['Female']

job=[]
relation=[]

job.append(male_job)
job.append(female_job)

relation.append(male_relation)
relation.append(female_relation)
colours = ['b','#FFC0CB'] 
print(job)
plt.pie(job,labels=['Male','Female'],colors=colours,shadow=True,autopct='%1.0f%%',explode=(0,0.1))
plt.title('Gender vs Job Satisfaction')
plt.show()
plt.pie(relation,labels=['Male','Female'],colors=colours,shadow=True,autopct='%1.0f%%',explode=(0,0.1))
plt.title('Gender vs Relationship Satisfaction')
plt.show()
