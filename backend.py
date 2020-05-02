#Part 1

import cache 

def get_matches(dictList,key_string,value_string):
  result  = []
  for i in dictList:
    for j in i.keys():
      if j == key_string:
        if i[j] == value_string:
           result.append(i)
  return result

def list_descriptions(data):
  acc_list = []
  for i in data:
    if i['tow_description'] not in acc_list:
      des = i['tow_description']
      acc_list.append(des)
  return acc_list

traces = list_descriptions(cache.read_cache('cached_data.csv'))

def count_by_month(x):
  acc_string = [0,0,0,0,0,0,0,0,0,0,0,0]
  for i in x:
    tow_date = i["tow_date"]
    month = int(tow_date[5]+tow_date[6])
    acc_string[month-1] += 1
  return acc_string

def count_by_day(x):
  acc_string2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for i in x:
    tow_date = i["tow_date"]
    day = int(tow_date[8]+tow_date[9])
    acc_string2[day-1] += 1
  return acc_string2
 
def some_scatter_data(x):
	count_by_day(x)
	return count_by_day(x)

def some_pie_data(x):
	A = get_matches(x,'police_district','District A')
	B = get_matches(x,'police_district','District B')
	C = get_matches(x,'police_district','District C')
	D = get_matches(x,'police_district','District D')
	E = get_matches(x,'police_district','District E')
	complete_list = [len(A),len(B),len(C),len(D),len(E)]
	return complete_list

def some_line_data(x):
  retVal = []
  des_list = list_descriptions(x)
  for i in des_list:
    dict_list = get_matches(x,'tow_description',i)
    month_count = count_by_month(dict_list)
    retVal.append(month_count)
  return retVal
