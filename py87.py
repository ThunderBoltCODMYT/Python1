import matplotlib.pyplot as pt
Physics = [56,79,48,97,26]
Chemistry = [86,69,58,90,66]
Biology = [50,70,40,80,46]
Maths = [65,37,57,72,69]
English = [90,59,89,63,80]
Exam = ['E1','E2','E3','E4','E5']
pt.plot(Exam,Physics,marker = '^',markersize = '15', markeredgecolor = 'b', ls = 'dotted', color = 'r', linewidth = '3')
pt.plot(Exam,Chemistry,marker = '>',markersize = '15', markeredgecolor = 'g', ls = 'dashed', color = 'b', linewidth = '3')
pt.plot(Exam,Biology,marker = '<',markersize = '15', markeredgecolor = 'm', ls = 'dashdot', color = 'g', linewidth = '3')
pt.plot(Exam,Maths,marker = '+',markersize = '15', markeredgecolor = 'y', ls = 'dotted', color = 'k', linewidth = '3')
pt.plot(Exam,English,marker = '*',markersize = '15', markeredgecolor = 'c', ls = 'dashed', color = 'y', linewidth = '3')
pt.xlabel('Name of Exam')
pt.ylabel('Marks Scored')
pt.title('result')
pt.show()