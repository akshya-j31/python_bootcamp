FSeriesLength = 10

def main(FSeriesLength):
    FSeries = fSeriesCalculator(FSeriesLength)
    print(FSeries)

def fSeriesCalculator(FSeriesLength):
    InitialNum = 0
    FirstNum = 1
    FSeries = [InitialNum, FirstNum]
    # print(type(FSeries[1]))
    for num in range(1, FSeriesLength):
        newnum = FSeries[num-1] + FSeries[num]
        FSeries.append(newnum)
    return FSeries

if __name__== "__main__" :
    main(FSeriesLength)