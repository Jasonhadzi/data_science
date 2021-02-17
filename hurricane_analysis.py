#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:40:10 2021

@author: jasonhadzikostas
"""

import collections
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(array):
  for i in range(len(array)):
    if array[i] == 'Damages not recorded':
      pass
    elif array[i][-1] == 'B':
      array[i] =float(array[i][:-1])*1000000000
    elif array[i][-1] == 'M':
      array[i] =float(array[i][:-1])*1000000
  return array



update_damages(damages)




# write your construct hurricane dictionary function here:
def hurricane_dictionary(names,months,years,winds,areas,damages,deaths):
  new_dict ={}

  for index in range(len(names)):
    new_dict[names[index]] = {"Name": names[index],"Month": months[index],"Year": years[index],"Max Sustained Wind": winds[index],"Areas Affected": areas[index],"Damage": damages[index],"Deaths": deaths[index]}

  return new_dict

  


hurricanes = hurricane_dictionary(names,months,years,max_sustained_winds,areas_affected,damages,deaths)





# write your construct hurricane by year dictionary function here:
def hurricane_by_year(dictionary):
  new_dict = {}
  
  for item in dictionary:
   # print(item)
    current_year = dictionary[item].get('Year')
    #print(current_year)
    #print(new_dict.keys())
    if current_year in new_dict.keys():
      #print('year exists as key')
      my_list = new_dict[current_year]
      my_list.append(dictionary[item])

    else:
      new_dict[current_year]= [dictionary[item]]
  return new_dict
  #print(new_dict)  


dict_by_year = hurricane_by_year(hurricanes)

#print(dict_by_year[1932])

# write your count affected areas function here:
def affected_areas(affected_areas):
  new_dict = collections.defaultdict(int)

  for items in affected_areas:
    for city in items:
      new_dict[city] +=1
  #print(new_dict)
  return new_dict


affected_areas = affected_areas(areas_affected)


# write your find most affected area function here:

def most_affected_area(dictionary):
  sorted_dict =sorted(dictionary.items(), key=lambda x:x[1], reverse=True)

  return sorted_dict

most_aff = most_affected_area(affected_areas)[0]
#print(most_aff)



# write your greatest number of deaths function here:

def find_max_deaths(dict):
  
  deaths = [int(d['Deaths']) for d in dict.values()]
  index = deaths.index(max(deaths))
  list_items = list(dict.values())
  print(index)
  return list_items[index]

max_death =find_max_deaths(hurricanes)

print(max_death["Name"])
print(max_death["Deaths"])



# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def add_mortality_scale(dictionary):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for item in dictionary:
    if dictionary[item]['Deaths'] == 0:
      hurricanes_by_mortality[0].append(dictionary[item]['Deaths'])
    elif dictionary[item]['Deaths'] > 0 and dictionary[item]['Deaths'] <= 100:
      hurricanes_by_mortality[1].append(dictionary[item])
    elif dictionary[item]['Deaths'] > 100 and dictionary[item]['Deaths'] <= 500:
      hurricanes_by_mortality[2].append(dictionary[item])
    elif dictionary[item]['Deaths'] > 500 and dictionary[item]['Deaths'] <= 1000:
      hurricanes_by_mortality[3].append(dictionary[item])
    elif dictionary[item]['Deaths'] > 1000 and dictionary[item]['Deaths'] <= 10000:
      hurricanes_by_mortality[4].append(dictionary[item])
    else:
      hurricanes_by_mortality[5].append(dictionary[item])

    
  
  return hurricanes_by_mortality

test = add_mortality_scale(hurricanes)
#print(test)





# write your greatest damage function here:



def find_most_damages(dict):
  
  damages = [int(d['Damage']) for d in dict.values()]
  index = damages.index(max(deaths))
  list_items = list(dict.values())
  print(index)
  return list_items[index]

max_damages =find_max_deaths(hurricanes)

print(max_damages["Name"])
print(max_damages["Damage"])





# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def add_damage_scale(dictionary):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for item in dictionary:
    if dictionary[item]['Damage'] == 'Damages not recorded':
      hurricanes_by_damage[0].append(dictionary[item])
    elif dictionary[item]['Damage'] > 0 and dictionary[item]['Damage'] <= 100000000:
      hurricanes_by_damage[1].append(dictionary[item])
    elif dictionary[item]['Damage'] > 100000000 and dictionary[item]['Damage'] <= 1000000000:
      hurricanes_by_damage[2].append(dictionary[item])
    elif dictionary[item]['Damage'] > 1000000000 and dictionary[item]['Damage'] <= 10000000000:
      hurricanes_by_damage[3].append(dictionary[item])
    elif dictionary[item]['Damage'] > 10000000000 and dictionary[item]['Damage'] <= 50000000000:
      hurricanes_by_damage[4].append(dictionary[item])
    else:
      hurricanes_by_damage[5].append(dictionary[item])
  return hurricanes_by_damage

#print(add_damage_scale(hurricanes))