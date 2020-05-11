# Blue at the Rijksmuseum - Get Images

# Objectives:
#   1. Import blueitemsfinal.csv as a df
#	2. Create two columns--one to store the image url, and one to store the image file name
#	3. Find which images can be downloaded from web
#		a. loop through df
#		b. if value in permitDownload == TRUE, use webImage['url'] to download image, else skip
#	4. Access url to save image to desktop
#	5. Save image name to df column

import pandas as pd
import csv
import requests
import urllib.request
import numpy as np

# make the df
blueitemsdf = pd.read_csv('blueitemsfinal.csv')
# print(blueitemsdf)

# append two new columns to df
blueitemsdf["imgURL"] = ""
blueitemsdf["imgFileName"] = ""
# print(blueitemsdf)


# select rows where df['permitDownload'] == 'True' to find images that can be downloaded
# print(type(blueitemsdf['permitDownload'])) # type is Series
print(blueitemsdf[0])
