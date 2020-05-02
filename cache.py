import csv  
import urllib.request
import json

#Part 2

def read_csv_header(fileObj):
    header = next(fileObj)
    return header

def read_data(fileObject,stringList):
  retVal = []
  for line in fileObject:
    someDict = {}
    for index in range(len(stringList)):
      someDict[stringList[index]] = line[index]
    retVal.append(someDict)
  return retVal

def write_csv_header(fileObj, seq):
  retVal = []
  for record in seq.keys():
    retVal.append(record)
  fileObj.writerow(retVal)
  return retVal

def write_dictionaries_to_csv(fileObj,dict_list,key_list):
  retVal = []
  for someDict in dict_list:
    acc = []
    for someKey in key_list:
      acc.append(someDict[someKey])
    retVal.append(acc)
  fileObj.writerows(retVal)
  return retVal

#Part 3

def get_data(string):
    webPage = urllib.request.urlopen(string)
    content = webPage.read().decode()
    var = json.loads(content)
    return var

def minimize_dictionaries(dict_list,string_list):
  result = []
  for each_dict in dict_list:
    dictionary = {}
    for each_string in string_list:
      value = each_dict.get(each_string,"District A")
      dictionary[each_string] = value
    result.append(dictionary)
  return result

def write_cache(dict_list,filename):
  with open(filename,"w") as f:
    writer = csv.writer(f)
    writer.writerow(dict_list[0])

    
    var = dict_list[0]
    acc2 = []
    for i in var:
      acc2.append(i)


    retVal = []
    for each_dict in dict_list:
      acc = []
      for each_key in acc2:
        acc.append(each_dict[each_key])
      retVal.append(acc)
    writer.writerows(retVal)

def read_data(fileObject,stringList):
  retVal = []
  for line in fileObject:
    someDict = {}
    for index in range(len(stringList)):
      someDict[stringList[index]] = line[index]
    retVal.append(someDict)
  return retVal

def read_csv_header(fileObj):
    header = next(fileObj)
    return header

def read_cache(filename):
  with open(filename) as f:
    reader = csv.reader(f)
    headerRow = read_csv_header(reader)
    result = read_data(reader,headerRow)
  return result
