#_*_ coding:utf-8 _*_
#__author__=="dragon"

import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets,linear_model

#从sklearn中导入数据
diabetes = datasets.load_diabetes()
print diabetes
#只用到数据集中的一种特征
diabetes_x = diabetes.data[:,np.newaxis,2]
#将数据分成训练和测试集
diabetes_x_train = diabetes_x[:-20]##442
diabetes_x_test = diabetes_x[-20:]##20
##将标签分为测试和训练集合
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
##建立一个线线回归对象
regr = linear_model.LinearRegression()
#训练
regr.fit(diabetes_x_train,diabetes_y_train)
#coefficients
print('coefficients = %f\n' % float(regr.coef_))
##均方误差（残差）
print('Residual sum of squares: %.2f' % np.mean((regr.predict(diabetes_x_test)-diabetes_y_test)**2))
##变异指数,为1时最优
print('variance score: %.2f' % regr.score(diabetes_x_test,diabetes_y_test))
##输出图
plt.scatter(diabetes_x_test,diabetes_y_test,color='red')
plt.plot(diabetes_x_test,regr.predict(diabetes_x_test),color='blue',linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()
