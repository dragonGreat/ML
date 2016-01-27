#_*_ coding:utf-8 _*_
#__author__=='dragon'
# import numpy as np
# import logistic as reg
# dataArr,labelMat = reg.loadDataSet()
# weights = reg.stocGradAscent1(dataArr, labelMat)
# # weights = reg.gradAscent(dataArr, labelMat)
# # weights = weights.getA()
# print weights
# # reg.plotBestFit(weights)
# reg.colocTest()


import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

def loadDataSet():
	dataMat = []
	labelMat = []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()##去掉多余的字符串，并按默认的方式分隔
		dataMat.append([float(lineArr[0]), float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat, labelMat

dataArr,labelMat =loadDataSet()

X = ((np.array(dataArr)-np.min(dataArr)/(np.max(dataArr)-np.min(dataArr)))+np.min(dataArr))
Y = np.array(labelMat)

h = .02  # step size in the mesh

logreg = linear_model.LogisticRegression(C=1e3)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)


Z = logreg.predict(X)

# Put the result into a color plot
# Z = Z.reshape(xx.shape)
plt.figure(1)
# plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)

plt.xlabel('x2')
plt.ylabel('x1')


plt.xticks(())
plt.yticks(())

plt.show()