import math
import urllib
import urllib2
from StringIO import StringIO
import requests



def downloadImage(query_url, filename, root_dir="/Users/jiazhang/Documents/SocialComputing/streetview_download/"):
    response = requests.get(query_url)
    localfile = open(root_dir + str(filename) + '.jpeg', 'w')
    localfile.write(response.content)
    localfile.close()




def createStreetViewURL(latitude, longitude,heading,pitch, fov, outputfilename , api_key='AIzaSyBZnvqy9HEpG-LAQwm_AxDOegMciI9jgP4'):
    url = 'http://maps.googleapis.com/maps/api/streetview?size=400x400&location='+str(latitude)+','+str(longitude)+'&fov='+str(fov)+'&heading='+str(heading)+'&pitch='+str(pitch)+'&sensor=false&key='+api_key
    filename = outputfilename + '_' + str(latitude) + '_' + str(longitude)
    downloadImage(url,filename)
 

#loop over coordinates x
#loop over coordinates y
#loop over angels
heading = 90
pitch = -300
fov = 90
latitude = 42.364128
longitude = -71.103187
name = "test1"

createStreetViewURL(latitude, longitude, heading, pitch, fov, name)