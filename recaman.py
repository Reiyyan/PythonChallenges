def recaman(n):
  myDict = {}
  previousValue = 0

  for x in range(1,n+1):
    # print()
    previousValue = myDict.get(x-1,0)
    currentValue = previousValue - x

    if(currentValue > 0 and currentValue not in myDict.values()):
      myDict[x] = currentValue

    else:
      currentValue = previousValue + x
      myDict[x] = currentValue

  return(myDict.values())

x = recaman(1000)

print(x)