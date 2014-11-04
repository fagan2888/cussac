import pandas as pd
from datetime import datetime
import numpy as np
import time
import matplotlib.pyplot as plt
import math
import re
import yaml


print datetime.strftime(datetime.utcnow(), "%b_%d_%Y_%H_%M")

# print '------------------'
# print '15 mins run: '
# print '------------------'
# 
# 
# colTypes = {'Tweet ID':np.str,'Enabled':np.bool}
# 
# ids = set()
# for i in range(1):
#     df = pd.read_csv("csv_tweets"+str(i)+".csv", parse_dates = [3,4], dtype = colTypes)
#     
#     numGeo = df[(df["Geo"] != 'None')]["Tweeted_At"].count()
#     numNotGeo = df[(df["Geo"] == 'None')]["Tweeted_At"].count()
#     total = df["Tweeted_At"].count()
#     print 'Geo enabled: ' + str (numGeo) + ' (' + str(numGeo*100.00/total) + '%)'
#     print 'Geo disabled: ' + str (numNotGeo) + ' (' + str(numNotGeo*100.00/total) + '%)'
#     print 'Total: ' + str(total)
#     
#     for _, geo in df['Geo'].iteritems():
#         print geo
#         geoObj = yaml.load(geo)
#         print geoObj["u'coordinates'"]
#         
#         break
      # {u'type': u'Point', u'coordinates': [40.6903213, -73.9271644]}

    
#     for _, id in df['Tweet ID'].iteritems():
#         ids.add(id)
#     print ids
#     print 'file: ' + str(i)
#     print '\t len(df) - '+ str(len(df))
#     print '\t len(ids) - '+ str(len(ids))