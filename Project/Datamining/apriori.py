# 根据数据库生成所有的一项集
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))


# 筛选候选集生成频繁项集   D: 事务数据库， Ck: 候选集， minsupport: 最小支持度
def scanD(D, CK, minSupport):
    ssCnt = {}
    for tid in D:
        for can in CK:
            if can.issubset(tid):
                if can not in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1

    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
            supportData[key] = support

    return retList, supportData


# 频繁项集两两组合，生成新的候选项集
def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[: k - 2]
            L2 = list(Lk[j])[: k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


# apriori算法实现
def apriori(dataSet, minSupport=0.7):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while len(L[k - 2]) > 0:
        CK = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, CK, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


# 规则生成
def generateRules(L, supportData, minConf=0.7):
    """
    生成关联规则的函数

    参数:
        L: 频繁项集列表
        supportData: 支持度字典
        minConf: 最小置信度,默认为0.7

    返回值:
        bigRuleList: 存储所有满足最小置信度要求的关联规则的列表
    """

    bigRuleList = []  # 存储所有的关联规则
    for i in range(1, len(L)):
        for freqSet in L[i]:
            # 将freqSet划分为单个元素的集合列表H1
            H1 = [frozenset([item]) for item in freqSet]
            if i > 1:
                rulesFromConseq(
                    freqSet, H1, supportData, bigRuleList, minConf
                )  # 生成关联规则
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList


# 计算满足最小置信度要求的关联规则
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    """
    计算满足最小置信度要求的关联规则的函数

    参数:
        freqSet: 频繁项集
        H: 可能的后件集合
        supportData: 支持度字典
        brl: 存储规则的列表
        minConf: 最小置信度,默认为0.7

    返回值:
        prunedH: 符合要求的后件列表
    """

    prunedH = []  # 存储符合要求的后件
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]  # 计算置信度
        if conf >= minConf:  # 满足最小置信度要求
            # print(freqSet - conseq, "--->", conseq, "conf:", conf)  # 打印关联规则
            brl.append((freqSet - conseq, conseq, conf))  # 将关联规则存储在brl中
            prunedH.append(conseq)  # 将后件添加到prunedH中
    return prunedH


# 从后件集合生成规则
def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    """
    从后件集合生成规则的函数

    参数:
        freqSet: 频繁项集
        H: 可能的后件集合
        supportData: 支持度字典
        brl: 存储规则的列表
        minConf: 最小置信度,默认为0.7

    返回值:
        None
    """

    m = len(H[0])  # 后件长度
    if len(freqSet) > (m + 1):  # 如果频繁项集的长度大于后件长度加一
        Hmp1 = aprioriGen(H, m + 1)  # 生成下一层的后件集合
        # 计算满足最小置信度要求的关联规则
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if len(Hmp1) > 1:  # 如果满足最小置信度要求的关联规则个数大于1
            # 递归调用自身，继续生成更多规则
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)
