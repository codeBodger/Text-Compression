def gElment(dict,element):  #Allows for integer indexing of dictionaries
  i = 0  #Make an iterating variable
  for ind in dict:  #Cycle through the indicies of the dictionary
    if i == element:  #Check if it's the right item in the dictionary
      return ind  #Return the apropriate index
    i = i + 1  #Increment i

def flipDic(inDict):  #Flips the roles of all values to indecies and indecies to values
  outDict = {}  #Create an empty dictionary
  for ind, val in inDict.items():  #Loop through inDict
    outDict[val] = ind  #Add elements to outDict with the roles flipped
  return outDict


def nicPrnt(inDict):  #A nice way to print dictionaries
  for ind, val in inDict.items():  #Cycle through the indecies an values of the dictionary
    print(str(ind) + "\t:\t" + str(val))  #Print the index and value with a colon between.  Works best with similar (±2) lengthed indecies
