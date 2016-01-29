#_*_ coding:utf-8 _*_
#__author__=='dragon'

##用来测试的简单数据集合
def loadDataSet():
	return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

##构建大小为1的所有集合的候选集合
def createC1(dataSet):
	C1 = []
	for val in dataSet:
		for item in val:
			if not [item] in C1:
				C1.append([item])
	C1.sort()
	return map(frozenset, C1)

def scanD(D, Ck, minSupport):
	####D:数据集，Ck:候选项集列表 minSupport：最小的支持度
	####输出：retList:满足最小支持度的集合L（频繁项集）   supportData:包含支持度的字典
	ssCnt = {}
	for tid in D:
		for can in Ck:
			if can.issubset(tid):###can是否是tid的一个子集
				if not ssCnt.has_key(can): 
					ssCnt[can]= 1
				else:
					ssCnt[can] += 1
	numItems = float(len(D))
	retList = []
	supportData = {}
	for key in ssCnt:
		support = ssCnt[key]/numItems
		if support >= minSupport:
			retList.insert(0,key)
		supportData[key] = support

	return retList, supportData

def aprioriGen(Lk, k):
	###Lk:频繁项集列表（Lk） K：项集元素个数
	###输出 retList:候选项集（CK）
	retList = []
	lenLk = len(Lk)
	for i in range(lenLk):
		for j in range(i+1, lenLk):
			L1 = list(Lk[i])[:k-2]
			L2 = list(Lk[j])[:k-2]
			# print k
			# print 'l1',L1
			# print 'l2',L2
			L1.sort()
			L2.sort()
			if(L1==L2):
				retList.append(Lk[i]| Lk[j])
	return retList



def apriori(dataSet, minSupport=0.5):
	C1 = createC1(dataSet)###候选集列表
	D = map(set, dataSet)##数据集合
	L1, supportData = scanD(D, C1, minSupport)
	L = [L1]
	k=2
	while(len(L[k-2])>0):
		Ck = aprioriGen(L[k-2], k)
		Lk, supK = scanD(D, Ck, minSupport)
		supportData.update(supK)
		L.append(Lk)
		k+=1
	return L, supportData

###生成候选集合
def rulesFromConseq(freqSet, H, supportData, br1, minConf=0.7):
	m = len(H[0])
	if (len(freqSet)>(m+1)):
		Hmp1 = aprioriGen(H, m+1)
		Hmp1 = calcConf(freqSet, Hmp1, supportData, br1, minConf)
		if(len(Hmp1)>1):
			rulesFromConseq(freqSet, Hmp1, supportData, br1, minConf)

####对规则进行评估
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf: 
            print freqSet-conseq,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def generateRules(L, supportData, minConf=0.7):
	####L：频繁项集列表 supportData:包含频繁项集支持数据的字典 minConf:最小可信度阈值
	####bigRuleList:可信度规则列表
	bigRuleList = []
	for i in range(1,len(L)):
		for freqSet in L[i]:
			H1 = [frozenset([item]) for item in freqSet]
			if(i>1):
				rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
			else:
				calcConf(freqSet, H1, supportData, bigRuleList, minConf)####频繁项集只有2个
	return bigRuleList			




if __name__ == '__main__':
	dataSet = loadDataSet()
	L, suppData = apriori(dataSet,minSupport=0.5)
	# print L[1]
	rules = generateRules(L, suppData, minConf=0.7)

	print rules
