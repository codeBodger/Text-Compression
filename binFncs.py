from dec2bin import dec2bin as db

from bin_txt import uni2bin as ub
from bin_txt import bin2uni as bu

from colorama import Fore as text
from colorama import Style as stl


def bin2dec(binStr):  #converts binary strings to decimal ints
  return int(binStr,2)

def pad(binStr, a = ''):  #Pads the beginning of a binary string with a 1 and 0s so it's in perfect bytes
  if a == '':  #With no argument/default
    binStr = '1' + binStr  #Add the 1
    while len(binStr)%8 != 0:  #While it still isn't perfect bytes
      binStr = '0' + binStr  #Add zeros
  elif a == 'rm':  #If 'rm' is specified
    while binStr[0] == '0':  #While the first digit is 0
      binStr = binStr[1:]  #Remove that 0
    binStr = binStr[1:]  #Remove the 1
  elif a == 'st':  #If 'st' is specified
    while len(binStr)%8 != 0:  #While it still isn't perfect bytes
      binStr = '0' + binStr  #Add zeros
  elif type(a) == int:  #If it's an integer
    if len(binStr) > 8 * a:  #If too long
      print(text.RED + 'String is already longer than the specified length to pad to.\nNot padded, input returned:\n' + binStr + stl.RESET_ALL)  #Error message
    while len(binStr) < 8 * a:  #While it still has fewer than the specified bytes
      binStr = '0' + binStr  #Add zeros
  else:  #Error catch
    print(text.RED + 'Improper second argument\nNot padded, input returned:\n' + binStr + stl.RESET_ALL)  #Error message
  return binStr  #return the (padded) string

def binDict(inDict):  #Make the dictionary able to be saved
  out = ''  #Empty string
  for char, val in inDict.items():  #Cycle through inDict
    out = out + ub(char)  #Add the binary representation of the current char to out
    binVal = db(val)  #Change the decimal value to binary
    binVal = pad(binVal, 4)  #Pad binVal
    out = out + binVal  #Add the binary value of the current char to out
  return out  #Return the binary form of the dictionary

def getChar(binStr):  #Gets the next char in the count dictionary portion of the encoded string
  l = 1 if binStr[0] == '0' else 0  #If it's a standard ascii char, it will be one byte
  for i in binStr:  #Loop through binStr
    if i == '0': break  #Until the char isn't 1
    l = l + 1  #And count the number of bytes the char will take
  out = ''  #An string to have the binary encoding of the char appened to it
  for i in range(8*l):  #Loop through binStr, but only the relevant area
    out = out + binStr[i]  #Append the bits to out
  return out  #Return the binary encoding of the char

def get_Val(binStr):  #Get the number of that specific char in the string
  out = ''  #A string to have the binary form of the number appened to it
  for i in range(32):  #Loop through binStr and get the first 32 bits
    out = out + binStr[i]  #And put them in out
  return bin2dec(out)  #Convert out to an int and return it

def NrChars(binStr):  #Creates a dictionary with the number of each char in as specified in the relevent area of binStr
  outDict = {}  #Empty dictionary
  while True:  #Loop until told otherwise
    char = getChar(binStr)  #Get the binary representation of the char
    binStr = binStr[len(char):]  #Trim binStr
    val  = get_Val(binStr)  #Get the value
    binStr = binStr[32:]  #Trim binStr
    outDict[bu(char)] = val  #Add these to the dictionary
    if pad('', 4) == binStr[:32]:  #If we've gotten to the separator
      binStr = binStr[32:]  #Trim binStr
      break  #Tell otherwise
  return outDict, binStr  #Return the dictionary and the trimmed binStr

def saveBin(binStr, filename):  #Saves the binary string
  binStr = pad(binStr)  #Pads in a way it can be removed
  binStr = bytearray(int(binStr[x:x+8], 2) for x in range(0, len(binStr), 8))  #bytearray!!
  f = open(filename,'wb')  #create new file
  f.write(binStr)  #Save it
  f.close()  #Close it

def loadBin(filename):  #Loads the binary string
  f = open(filename, 'rb')  #Open the file
  binFile = f.read()  #Read it
  f.close()  #Close it
  binFile = bytearray(binFile)  #bytearray!!
  binStr = ''  #Empty string
  for i in binFile:  #Loop through the items in binFile
    a = pad(str(db(i)), 'st')  #Pad them with 0s
    binStr = binStr + a  #Append the next byte
  binStr = pad(binStr, 'rm')  #Remove the removeable padding
  return binStr  #Return the binary string
