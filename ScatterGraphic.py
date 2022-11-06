from cProfile import label
import matplotlib.pyplot as plt 
import numpy as np


plt.rcParams.update({'font.size': 10})

bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho = [71,83,22,99,88,86,80,82,89,74,80,83,77,93,82,47,68,84,75,60,91,59,76,93,88,94,89,39,81,97,70,96,55,96,0,0,0,0,0,0,0]
desempenho2 = [82,83,40,95,83,86,89,81,93,79,83,84,90,94,84,59,74,85,84,67,91,59,81,93,92,95,90,41,80,96,72,97,61,98,0,0,0,0,0,0,0]
desempenho3 = [71,80,44,99,90,94,67,83,91,78,79,85,74,93,94,59,53,85,92,80,91,63,80,97,92,95,90,38,87,97,86,96,65,96,0,0,0,0,0,0,0]
desempenho4 = [76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0]
desempenho5 = [56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0]
desempenho6 = [70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0]
plt.scatter(desempenho, bases, label='SVM Original', alpha=0.5)
plt.scatter(desempenho2, bases,  marker='^', label='SVM Reduzida', alpha=0.5)
plt.scatter(desempenho3, bases, marker='P',label='Random Original', alpha=0.5)
plt.scatter(desempenho4, bases, marker='*',label='Random Reduzida', alpha=0.5)
plt.scatter(desempenho5, bases, marker='X',label='Árvore Original', alpha=0.5)
plt.scatter(desempenho6, bases, marker='D',label='Árvore Reduzida', alpha=0.5)

plt.legend(loc='upper left', prop={'size': 6})
plt.title('F-Measure')
plt.show()

"""
plt.rcParams.update({'font.size': 10})

bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho = [71,83,22,99,88,86,80,82,89,74,80,83,77,93,82,47,68,84,75,60,91,59,76,93,88,94,89,39,81,97,70,96,55,96,0,0,0,0,0,0,0]
desempenho2 = [82,83,40,95,83,86,89,81,93,79,83,84,90,94,84,59,74,85,84,67,91,59,81,93,92,95,90,41,80,96,72,97,61,98,0,0,0,0,0,0,0]

plt.scatter(desempenho, bases, label='SVM Original')
plt.scatter(desempenho2, bases, label='SVM Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('F-Measure SVM')
plt.show()

plt.rcParams.update({'font.size': 10})

bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']


desempenho3 = [71,80,44,99,90,94,67,83,91,78,79,85,74,93,94,59,53,85,92,80,91,63,80,97,92,95,90,38,87,97,86,96,65,96,0,0,0,0,0,0,0]
desempenho4 = [76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0]
plt.scatter(desempenho3, bases, label='Random Original')
plt.scatter(desempenho4, bases, label='Random Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('F-Measure Random Forest')
plt.show()


plt.rcParams.update({'font.size': 10})

bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho5 = [56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0]
desempenho6 = [70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0]
plt.scatter(desempenho5, bases, label='Árvore Original')
plt.scatter(desempenho6, bases, label='Árvore Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('F-Measure Árvore de Decisão')
plt.show()

##################################################################### Precision #####################################################


bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho = [55,88,43,99,88,75,67,83,90,76,73,86,63,89,82,50,76,81,73,74,87,63,78,92,82,94,88,35,74,95,55,95,51,96,0,0,0,0,0,0,0]
desempenho2 = [81,77,36,91,91,75,65,79,93,80,75,89,86,95,83,54,78,83,82,78,87,63,93,92,88,96,91,34,73,95,55,98,58,98,0,0,0,0,0,0,0]
desempenho3 = [56,79,57,99,87,90,73,79,86,86,71,89,66,89,94,53,70,80,93,72,89,59,74,96,93,97,85,42,84,96,87,90,83,95,0,0,0,0,0,0,0]
desempenho4 = [76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0]
desempenho5 = [56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0]
desempenho6 = [70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0]
plt.scatter(desempenho, bases, label='SVM Original')
plt.scatter(desempenho2, bases, label='SVM Reduzida')
plt.scatter(desempenho3, bases, label='Random Original')
plt.scatter(desempenho4, bases, label='Random Reduzida')
plt.scatter(desempenho5, bases, label='Árvore Original')
plt.scatter(desempenho6, bases, label='Árvore Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('Precision')
plt.show()

bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho = [55,88,43,99,88,75,67,83,90,76,73,86,63,89,82,50,76,81,73,74,87,63,78,92,82,94,88,35,74,95,55,95,51,96,0,0,0,0,0,0,0]
desempenho2 = [81,77,36,91,91,75,65,79,93,80,75,89,86,95,83,54,78,83,82,78,87,63,93,92,88,96,91,34,73,95,55,98,58,98,0,0,0,0,0,0,0]
plt.scatter(desempenho, bases, label='SVM Original')
plt.scatter(desempenho2, bases, label='SVM Reduzida')
plt.legend(loc='upper left', prop={'size': 6})
plt.title('Precision SVM')
plt.show()


bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']


desempenho3 = [56,79,57,99,87,90,73,79,86,86,71,89,66,89,94,53,70,80,93,72,89,59,74,96,93,97,85,42,84,96,87,90,83,95,0,0,0,0,0,0,0]
desempenho4 = [76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0]
plt.scatter(desempenho3, bases, label='Random Original')
plt.scatter(desempenho4, bases, label='Random Reduzida')
plt.legend(loc='upper left', prop={'size': 6})
plt.title('Precision Random Forest')
plt.show()



bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho5 = [56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0]
desempenho6 = [70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0]
plt.scatter(desempenho5, bases, label='Árvore Original')
plt.scatter(desempenho6, bases, label='Árvore Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('Precision Árvore de Decisão')
plt.show()


##################################################################### Recall #####################################################

bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho = [60,79,43,99,82,97,63,82,89,76,87,89,85,97,71,49,72,86,76,74,95,63,80,95,96,95,90,40,90,99,99,97,77,96,0,0,0,0,0,0,0]
desempenho2 = [82,91,57,99,78,94,70,83,93,82,92,93,95,93,76,65,73,89,87,76,96,63,93,95,96,93,91,45,90,99,99,99,79,98,0,0,0,0,0,0,0]
desempenho3 = [56,79,57,99,87,90,73,79,86,86,71,89,66,89,94,53,70,80,93,72,89,59,74,96,93,97,85,42,84,96,87,90,83,95,0,0,0,0,0,0,0]
desempenho4 = [76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0]
desempenho5 = [56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0]
desempenho6 = [70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0]
plt.scatter(desempenho, bases, label='SVM Original')
plt.scatter(desempenho2, bases, label='SVM Reduzida')
plt.scatter(desempenho3, bases, label='Random Original')
plt.scatter(desempenho4, bases, label='Random Reduzida')
plt.scatter(desempenho5, bases, label='Árvore Original')
plt.scatter(desempenho6, bases, label='Árvore Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('Recall')
plt.show()

bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho = [60,79,43,99,82,97,63,82,89,76,87,89,85,97,71,49,72,86,76,74,95,63,80,95,96,95,90,40,90,99,99,97,77,96,0,0,0,0,0,0,0]
desempenho2 = [82,91,57,99,78,94,70,83,93,82,92,93,95,93,76,65,73,89,87,76,96,63,93,95,96,93,91,45,90,99,99,99,79,98,0,0,0,0,0,0,0]
plt.scatter(desempenho, bases, label='SVM Original')
plt.scatter(desempenho2, bases, label='SVM Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('Recall SVM')
plt.show()


bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho3 = [56,79,57,99,87,90,73,79,86,86,71,89,66,89,94,53,70,80,93,72,89,59,74,96,93,97,85,42,84,96,87,90,83,95,0,0,0,0,0,0,0]
desempenho4 = [76,84,56,99,91,95,69,91,90,82,83,90,84,94,88,61,75,84,92,82,90,65,86,97,92,96,91,36,88,97,91,98,70,97,0,0,0,0,0,0,0]
plt.scatter(desempenho3, bases, label='Random Original')
plt.scatter(desempenho4, bases, label='Random Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('Recall Random Forest')
plt.show()



bases = ['Post Operation','Hijacked','Higher Education','Iris','TDAH - Leitura','Drug','Glass','TDAH - Aritmética'
,'TDAH - Escrita','Heart Failure','Cleveland Clinic','Heart Attack','Haberman','Lung Cancer','Ionosphere','Cirrhosis','Data Science', 'Diabetes'
,'Tic Tac Toe','Cyber Security','Titanic','Contraceptive','Yeast','Fetal Health','Marketing','Splice','Vaccine','Abalone','Employee',
'Brain Stroke','Banana','Optdigits','Wine','Twonorm','Mushroom','Zomato','Home Equity','Phishing Website','Video Game Ratings','Body Performance'
,'Presos']

desempenho5 = [56,73,50,95,85,99,67,75,88,70,67,77,67,85,81,49,75,74,72,54,89,58,60,85,82,90,87,35,84,79,81,78,57,74,0,0,0,0,0,0,0]
desempenho6 = [70,88,40,99,86,99,83,85,91,77,77,79,72,81,84,61,75,76,71,57,86,54,77,88,88,91,89,32,82,83,85,85,58,76,0,0,0,0,0,0,0]
plt.scatter(desempenho5, bases, label='Árvore Original')
plt.scatter(desempenho6, bases, label='Árvore Reduzida')

plt.legend(loc='upper left', prop={'size': 6})
plt.title('Recall Árvore de Decisão')
plt.show()
"""