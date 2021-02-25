from dictFns import gElment as ge


def NrChars(uniStr):  #Counts the number of each char in the string
  countDict = {uniStr[0]: 0}  #Create the dicionary
  for i in uniStr:  #Cycle through the string
    countDict[i] = 0  #Create dictionary items
  for i in uniStr:  #Cycle through the string
    countDict[i] = countDict[i] + 1  #Count the number of each char
  return countDict

def compNcd(inDict):  #Takes in a dictionary (from NrChars) and determines the binary code that each char should have after compression
  outDict = {ge(inDict,0): ''}  #Declare the dictionary to contain the encoding
  for i in inDict:  #Cycle through inDict
    outDict[i] = ''  #Create dictionary items
  while True:  #Itterate until told otherwise
    low0i = ge(inDict,0)  #Get the first (0th) item in inDict
    low0v = None  #Declare low0v
    for ind, val in inDict.items():  #for 0: Cycle through the indecies and values in inDict
      if val <= inDict[low0i]:  #If this val is less than the current minimum
        low0i = ind  #Update the lowest index
        low0v = val  #Update the lowest value
    del inDict[low0i]  #Remove the lowest valued dicionary item
    low1i = ge(inDict,0)  #Get the first (0th) (the previous second (1st)) item in inDict
    low1v = None  #Declare low1v
    for ind, val in inDict.items():  #for 1: Cycle through the indecies and values in inDict
      if val <= inDict[low1i]:  #If this val is less than the current (second) minimum
        low1i = ind  #Update the (second) lowest index
        low1v = val  #Update the (second) lowest value
    del inDict[low1i]  #Remove the (second) lowest valued dictionary item
    inDict[low0i + low1i] = low0v + low1v  #Combine low0 and low1 in inDict
    for char in low0i:  #for 0: Cicle through the chars in low1
      outDict[char] = '0' + outDict[char]  #Add a 0 to the beginning of the codes of the low0 chars
    for char in low1i:  #for 1: Cicle through the chars in low0
      outDict[char] = '1' + outDict[char]  #Add a 1 to the beginning of the codes of the low1 chars
    if len(inDict) <= 1:  #When there aren't any more items to combine
      break  #Tell otherwise (i.e. break from the while loop)
  return outDict  #Return the new encoding we made


def compress(inStr):  #Compiles the various compressed elements into one binary string to be saved
  #Imports and Aliases
  cn = compNcd
  nc = NrChars
  from binFncs import binDict as bD
  from binFncs import pad
  cntDict = nc(inStr)  #Dictionary with the number of each char in the string
  tempDic = cntDict.copy()
  encDict = cn(tempDic)  #The dictionary used for encoding the chars
  comprStr = ''  #Empty string
  for char in inStr:  #Loop through inStr
    comprStr = comprStr + encDict[char]  #Add the encodings for each char in inStr to comprStr
  comprStr = bD(cntDict) + pad('', 4) + comprStr  #Add a binary version of encDict to the beginning as well as a 4 byte seperator of all 0s
  return comprStr  #Return the compressed binary string

def uncompress(binStr):  #Given a compressed binary string, uncompress it
  #Imports and Aliases
  cn = compNcd
  from binFncs import NrChars as nc
  from dictFns import flipDic as fd
  cntDict, binStr = nc(binStr)  #A dictionary storing how many of each char are in the string and a shortened version of binStr
  encDict = fd(cn(cntDict))  #The dictionary used for (de/en)coding the chars
  out = ''  #The string we will append the chars to
  temp = ''  #The string to store each bin char until we find it in encDict
  for i in binStr:  #Cycle through binStr
    temp = temp + i  #Append the current val in binStr to temp
    if temp in encDict:  #If temp is in encDict
      out = out + encDict[temp]  #Append the apropriate char to out
      temp = ''  #Reset temp
  return out  #Rerun the uncompressed string
