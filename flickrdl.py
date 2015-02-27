#!/usr/bin/env python2.7

##############################################################################
# FlickrDownloadr
# Download images from flickr.
#
# Copyright (C) 2015 Francesco Pira <francescopira.me@gmail.com> <fpira.com>
#
# This script is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this script.  If not, see <http://www.gnu.org/licenses/>.

##############################################################################


import sys
import urllib2
from bs4 import BeautifulSoup


########### make page URL compliant ##########
def compliant_url(page_url):
     page_url = page_url.strip() 
     if page_url[len(page_url)-1]=='/':
          page_url = page_url[:-1]
     #page_url = page_url+"/sizes/k"
     #print page_url
     return page_url

########### parse flickr html to get picture URL ##########
def get_img_url(page_url):
      print "Please wait..."
      try:
          f = urllib2.urlopen(page_url)
      except:
          print "Error: Cannot connect to flickr. Have you inserted the right URL?"
          sys.exit()
      try:
          html = f.read()
          soup = BeautifulSoup(html)
          soup = soup.find(id="allsizes-photo")
          img_url = soup.img['src']
      except:
        print "Error: Image not found"
        sys.exit()
      return img_url

########### saving picture to disk ##########
def save_to_disk(img_url):

      file_name = img_url.split('/')[-1]
      try:
          u = urllib2.urlopen(img_url)
      except :
          print "Error: Cannot connect to flickr"
          sys.exit()
      try:     
          f = open(file_name, 'wb')
          meta = u.info()
          file_size = int(meta.getheaders("Content-Length")[0])
          print "Downloading: %s \t Size: %s KB" % (file_name, file_size/1024)

          file_size_dl = 0
          block_sz = 8192
          while True:
              buffer = u.read(block_sz)
              if not buffer:
                  break

              file_size_dl += len(buffer)
              f.write(buffer)
              status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
              status = status + chr(8)*(len(status)+1)
              print status,

          f.close()
      except:
          print "Error: Cannot save image to disk"
          sys.exit()
      print ""


## Main Program ####

try:
     if sys.argv[1].startswith("http"):
          vars = sys.argv[1]
except:
     #print "Error: No Arguments"
     print "usage:\t flickrdl url1,url2,..."
     print "example: flickrdl https://www.flickr.com/photos/example/12345678910/sizes/o/,https://..."
     sys.exit()

if sys.argv[1].startswith("http"):
     try:
          vars.startswith("http")
          vars = vars.replace(" ","")
          var_list = vars.split(",") # split entries
          var_list = filter(None, var_list) # exclude empty entries
     except:
          print "Input Error"
          sys.exit()

     print "Start working..."
     for page_url in var_list:
       page_url = compliant_url(page_url)
       img_url = get_img_url(page_url)
       save_to_disk(img_url)
     print "Finished!"
     sys.exit()
else:
     print "usage:\t flickrdl url1,url2,..."
     print "example: flickrdl https://www.flickr.com/photos/example/12345678910/sizes/o/,https://..."
     print ""
     sys.exit()
     # Next version #print "usage: flickrdl [download path] url1,url2,..."



