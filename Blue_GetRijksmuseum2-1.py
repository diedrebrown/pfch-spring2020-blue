# Blue at the Rijksmuseum - Get Data
# This code is based on lessons from Matt Miller's INFO 644 Programming for Cultural Heritage Course at Pratt Institute
# Objectives:
#   1. Get information about blue objects at the Rijksmuseum using the Rijksmuseum API.
#   2. Store information as text dictionary.
#   3. Access the individual artObjects from the dictionary and store to a CSV.

import requests, json
import csv
import pandas as pd

# get information from the rijksmuseum api and use to get works that are/mention blue and have images 
bluerijks = requests.get("https://www.rijksmuseum.nl/api/en/collection?key=????????&q=blue&imgonly")
# print(bluerijks.text)

# store retreived api info as a dictionary
bluerijksdata = json.loads(bluerijks.text)

# write retrived data to a json file backup
with open('bluerijksinfo.json', 'w') as outfile:
    json.dump(bluerijksdata, outfile) 

# print the dictionary keys
print(bluerijksdata.keys())
# print(len(bluerijksdata))
# keys include 'elapsedMilliseconds', 'count', 'countFacets', 'artObjects', 'facets'
# 'count' is the number of records/items that match my search = 452 
# 'countFacets' gives specifics on those items:
#   how many have an image? 370
#   how many are on display in the museum? 66
# 'artObjects' contains the information on the items as lists of dictionaries
# 'facets' contains nested dictionaries of a key-value pairs of counts of information, such as:
#    artist:number of their works 
#    country: number of items from country
#    hex code: number of images with hex code
#    ...and more 
# store artObects into a variable as a list of dictionaries which we may use later
bluerijksObjects = bluerijksdata.get('artObjects')
# print(type(bluerijksObjects), len(bluerijksObjects))
# bluerijksObjects is a list of 10 items/dictionaries
# print(bluerijksObjects[0])
# print(bluerijksObjects[2])

# create a csv file with the information of the object
with open('blueitem3.csv', mode='w') as blueitems_file:
    blueitemswriter = csv.writer(blueitems_file, delimiter=',')
    writecount = 0
    for item in bluerijksObjects:
        if writecount == 0:
            header = item.keys()
            blueitemswriter.writerow(header)
            writecount += 1
        blueitemswriter.writerow(item.values())

# let's modify the csv for only the information we need
# objectNumber [item 2], title [item 3], principleOrFirstMaker [item 5], permitDownload [item 8], webImage[item 9] (url from webImage [item 5])
readdf = pd.read_csv('blueitem3.csv')
moddf = readdf.drop(columns=['links','id','headerImage','productionPlaces'], axis=1)
# print(moddf)
# store moddf as a csv
moddf.to_csv('blueitemsfinal.csv', index=False)

