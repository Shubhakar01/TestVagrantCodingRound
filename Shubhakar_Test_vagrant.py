def sub(budget):
    sub = {
        "TOI": [3, 3, 3, 3, 3, 5, 6],
	"Hindu": [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
        "ET": [4, 4, 4, 4, 4, 4, 10],
	"BM": [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
        "HT": [2, 2, 2, 2, 2, 4, 4]
    }
    result=[]
    sums = {
        "TOI": sum(sub["TOI"]),
         "HT": sum(sub["HT"]),
        "Hindu": sum(sub["Hindu"]),
        "ET": sum(sub["ET"]),
        "BM": sum(sub["BM"]),
       
    }
    sums = dict(sorted(sums.items(), key=lambda item: item[1]))
    result = []
    for i in range(0,len(sums)):
      for j in range(i+1, len(sums)):
        if sums[list(sums)[i]] + sums[list(sums)[j]] <= budget:
          result.append([list(sums)[i], list(sums)[j]])
        else :
          break
    print (result)
sub(35)