import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Create a dataset
dict = {'SVM Original': [56,61,30,99,76,98,53,74,83,82,56,81,63,88,87,39,59,78,66,65,86,50,51,88,78,92,81,22,72,95,55,97,50,96,0,0,0,0,0,0,0],
        'SVM Reduzida': [69,57,35,96,74,97,56,76,89,78,62,81,83,90,79,43,65,78,80,65,86,53,50,88,84,91,82,25,72,95,55,98,52,98,0,0,0,0,0,0,0],
        'Random Original':[56,64,34,99,82,94,63,78,86,88,56,83,63,88,84,44,58,78,89,72,87,51,53,94,97,93,85,24,82,96,90,96,60,97,0,0,0,0,0,0,0],
        'Random Reduzida':[62,70,40,99,82,95,71,86,84,75,58,89,75,90,95,47,66,78,95,70,85,55,62,93,97,93,86,24,84,96,87,99,67,97,0,0,0,0,0,0,0],
        'C4.5 Original':[44,52,21,98,75,99,50,68,81,75,46,74,60,75,75,35,57,70,70,58,85,51,42,79,92,85,80,33,78,67,83,59,32,74,0,0,0,0,0,0,0],
        'C4.5 Reduzida':[54,72,12,99,76,99,62,76,86,80,48,77,60,71,82,47,66,70,70,59,79,51,49,80,94,87,77,36,78,72,84,62,36,75,0,0,0,0,0,0,0]}
df = pd.DataFrame(data = dict,index=['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos'])

# plot a heatmap with annotation
selena = sns.heatmap(df, cmap = "Reds" ,annot=False, xticklabels=True, yticklabels=True ,annot_kws={"size": 8.5})
sns.set(font_scale=1.9)
plt.xticks(rotation=0)
plt.xticks(size = 10)
plt.yticks(size = 10)
plt.show()



# Create a dataset
dict1 = {'SVM Original': [71,83,22,99,88,86,80,82,89,74,80,83,77,93,82,47,68,84,75,60,91,59,76,93,88,94,89,39,81,97,70,96,55,96,0,0,0,0,0,0,0],
        'SVM Reduzida': [82,83,40,95,83,86,89,81,93,79,83,84,90,94,84,59,74,85,84,67,91,59,81,93,92,95,90,41,80,96,72,97,61,98,0,0,0,0,0,0,0],
        'Random Original':[71,80,44,99,90,94,67,83,91,78,79,85,74,93,94,59,53,85,92,80,91,63,80,97,92,95,90,38,87,97,86,96,65,96,0,0,0,0,0,0,0],
        'Random Reduzida':[76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0],
        'C4.5 Original':[56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0],
        'C4.5 Reduzida':[70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0]}
df1 = pd.DataFrame(data = dict1 ,index=['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos'])

# plot a heatmap with annotation
selena1 = sns.heatmap(df1, cmap = "Reds"  ,annot=False, xticklabels=True, yticklabels=True ,annot_kws={"size": 8.5})
sns.set(font_scale=1.9)
plt.xticks(rotation=0)
plt.xticks(size = 10)
plt.yticks(size = 10)
plt.show()





# Create a dataset
dict2 = {'SVM Original': [55,88,43,99,88,75,67,83,90,76,73,86,63,89,82,50,76,81,73,74,87,63,78,92,82,94,88,35,74,95,55,95,51,96,0,0,0,0,0,0,0],
        'SVM Reduzida': [81,77,36,91,91,75,65,79,93,80,75,89,86,95,83,54,78,83,82,78,87,63,93,92,88,96,91,34,73,95,55,98,58,98,0,0,0,0,0,0,0],
        'Random Original':[56,79,57,99,87,90,73,79,86,86,71,89,66,89,94,53,70,80,93,72,89,59,74,96,93,97,85,42,84,96,87,90,83,95,0,0,0,0,0,0,0],
        'Random Reduzida':[76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0],
        'C4.5 Original':[56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0],
        'C4.5 Reduzida':[70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0] }
df2 = pd.DataFrame(data = dict2 ,index=['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos'])

# plot a heatmap with annotation
selena2 = sns.heatmap(df2, cmap = "Blues" ,annot=False, xticklabels=True, yticklabels=True ,annot_kws={"size": 8.5})
sns.set(font_scale=1.9)
plt.xticks(rotation=0)
plt.xticks(size = 10)
plt.yticks(size = 10)
plt.show()



# Create a dataset
dict3 = {'SVM Original': [60,79,43,99,82,97,63,82,89,76,87,89,85,97,71,49,72,86,76,74,95,63,80,95,96,95,90,40,90,99,99,97,77,96,0,0,0,0,0,0,0],
        'SVM Reduzida': [82,91,57,99,78,94,70,83,93,82,92,93,95,93,76,65,73,89,87,76,96,63,93,95,96,93,91,45,90,99,99,99,79,98,0,0,0,0,0,0,0],
        'Random Original':[56,79,57,99,87,90,73,79,86,86,71,89,66,89,94,53,70,80,93,72,89,59,74,96,93,97,85,42,84,96,87,90,83,95,0,0,0,0,0,0,0],
        'Random Reduzida':[76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0],
        'C4.5 Original':[56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0],
        'C4.5 Reduzida':[70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0] }
df3 = pd.DataFrame(data = dict3 ,index=['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos'])

# plot a heatmap with annotation
selena3 = sns.heatmap(df3, cmap = "Greens" ,annot=False, xticklabels=True, yticklabels=True ,annot_kws={"size": 8.5})
sns.set(font_scale=1.9)
plt.xticks(rotation=0)
plt.xticks(size = 10)
plt.yticks(size = 10)
plt.show()

