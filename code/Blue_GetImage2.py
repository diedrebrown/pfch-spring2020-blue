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



# images to download
MeissenerblueMacaw = 'https://lh3.ggpht.com/5sc-SGzzgobkHnmnykUi4B1PqMtadoFqXOhYLQmsAI0Mcs_FeCoXT6loaiAUhr_zKvp2iyXntDxVhCzeVwjFulsjzRE=s0'
VerspronckportGirLDressed = 'https://lh3.googleusercontent.com/hpl3FiKJycePxIROjWZLZXbodT5uV-EsBw9dlux7NFmhbWAX2xtHQZmlIqb9yxhu-yvs28KQsw1ulzjL8qdiRhPmDgc=s0'
VermeerWomanLet = 'https://lh3.googleusercontent.com/n7X03-aBMaHLQmd9UZXy0WSO81bLI376BMv8tjXfah_-BqdJURY-FoyX_YJKj5WuV5j3P8rLNEHM-T8jJztag9FQZkD3=s0'
VermeerMilkmaid = 'https://lh3.googleusercontent.com/cRtF3WdYfRQEraAcQz8dWDJOq3XsRX-h244rOw6zwkHtxy7NHjJOany7u4I2EG_uMAfNwBLHkFyLMENzpmfBTSYXIH_F=s0'
deHoochDelousing = 'https://lh3.googleusercontent.com/6Vm9nYrTeeYe5wl7lOafEHUnbzNF8KJw3ZbV_cNBr_wQTyHyp1DJxEWEEK3OSuji9XGYx04r15HTVPu850WeFcOd0ZVv=s0'
SintJansHolyKin = 'https://lh3.googleusercontent.com/qjkiSAC89H2lvsgogjCe6WGLzMFNgdoCLHwRngvUX6BACTFTggkzIXE99tz9Em-hTf44MS9YeRsxCjDkW7tfC9lprw=s0'
BlueWashOntwerp = 'https://lh3.googleusercontent.com/Hbux_YN-tRlv9oeRcT1nMyMMaiwLi-22BcHzyE3Go_SNKAWKRI5J5I-GRsMmlwsdCDgSO3zdvaMVtUiXlbm-w526l8U=s0'
MeissnerblueParrot = 'https://lh3.googleusercontent.com/jPW2iKGONNfvfNrCmHHEICcwPontfBXgtchCrMwx7UEnPvaxC58z1V-i1PCmeeF9qsuil8plDBbDBtPgMWXeXZbYTgS_=s0'

imgloc = [MeissenerblueMacaw,VerspronckportGirLDressed, VermeerWomanLet, VermeerMilkmaid, deHoochDelousing, SintJansHolyKin, BlueWashOntwerp, MeissnerblueParrot]
filepath = '/Users/diedrebrown/Desktop/Brown-PCH-Final-Sp20-Blue/images/' 

imgloccount = 0
for img in imgloc:
	filename=str(imgloccount)
	imgpath = filepath + filename +'.jpg'
	urllib.request.urlretrieve(imgloc[imgloccount], imgpath)
	imgloccount +=1
