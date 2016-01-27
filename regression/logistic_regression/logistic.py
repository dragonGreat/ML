#_*_ coding:utf-8 _*_
#__author__=='dragon'
import numpy as np
import matplotlib.pyplot as plt
# from numpy import *

def loadDataSet():
	dataMat = []
	labelMat = []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()##去掉多余的字符串，并按默认的方式分隔
		dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat, labelMat

##sigmoid函数
def sigmoid(inX):
	return 1.0/(1+np.exp(-inX))

##梯度上升
def gradAscent(dataMatIn, classLabels):
	dataMat = np.mat(dataMatIn)
	labelMat = np.mat(classLabels).T
	# print labelMat.shape
	m,n = np.shape(dataMat)
	alpha = 0.001##步长
	maxCycles = 600##最大循环次数
	weights = np.ones((n,1))##初始化权重矩阵为1
	for k in xrange(maxCycles):
		h = sigmoid(dataMat*weights)
		# print np.shape(h)
		error = (labelMat-h)
		weights = weights+alpha*dataMat.T*error
	return weights

def plotBestFit(weights):
	# weights = weights.getA()
	dataMat,labelMat = loadDataSet()
	dataArr = np.array(dataMat)
	n = np.shape(dataArr)[0]###100
	xcord1 = []
	ycord1 = []
	xcord2 = []
	ycord2 = []
	for i in range(n):
		if int(labelMat[i]) ==1:
			xcord1.append(dataArr[i,1])
			ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1])
			ycord2.append(dataArr[i,2])
	fig =plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
	ax.scatter(xcord2,ycord2,s=30,c='green')
	x = np.arange(-3.0,3.0,0.1)
	y = (-weights[0]-weights[1]*x)/weights[2]
	ax.plot(x,y)
	plt.xlabel('X1')
	plt.ylabel('X2')
	# plt.legend()
	plt.show()



###随机梯度上升算法
def stocGradAscent0(dataMat, classLabels):
	dataMat = np.array(dataMat)
	m,n = np.shape(dataMat)
	alpha = 0.01
	weights = np.ones(n)
	for i in xrange(m):
		h = sigmoid(sum(dataMat[i]*weights))
		error = classLabels[i]-h
		weights = weights + alpha*error*dataMat[i]
	return weights


def stocGradAscent1(dataMat, classLabels, numIter=150):
	dataMat = np.array(dataMat)
	m,n = np.shape(dataMat)
	weights = np.ones(n)
	for j in xrange(numIter):
		dataIndex = range(m)
		for i in xrange(m):
			alpha = 4/(1.0+j+i)+0.01##自适应调整学习率
			randIndex = int(np.random.uniform(0,len(dataIndex)))#随机选取更新值
			h = sigmoid(sum(dataMat[randIndex]*weights))
			error = classLabels[randIndex]-h
			weights = weights + alpha*error*dataMat[randIndex]
			del(dataIndex[randIndex])
	return weights



def classifyVector(inX,weights):
	prob = sigmoid(sum(inX*weights))
	if prob>0.5:
		return 1.0
	else:
		return 0.0

def colocTest():
	frTrain = open('horseColicTraining.txt')
	frTest = open('horseColicTest.txt')
	trainingSet = []
	trainingLabels = []
	for line in frTrain.readlines():
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):##20个特征
			lineArr.append(float(currLine[i]))
		trainingSet.append(lineArr)
		trainingLabels.append(float(currLine[21]))
	trainWeights = stocGradAscent1(trainingSet, trainingLabels,500)
	errorCount =0.0
	numTestVec =0.0
	for line in frTest.readlines():
		numTestVec +=1.0
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		if int(classifyVector(lineArr,trainWeights)!=int(currLine[21])):
			errorCount +=1

	errorRate = (float(errorCount)/numTestVec)
	print "the error rate of this test is:%f" % errorRate
	return errorRate

def multiTest():
	numTests = 10
	errorSum = 0.0
	for k in range(numTests):
		errorSum += colocTest()
	print "after %d iteration the average error rate is: %f" % (numTests,errorSum/float(numTests))




if __name__ == '__main__':
	multiTest()
