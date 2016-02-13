from bs4 import BeautifulSoup
import csv
import os
import re
import urllib

directory_name = raw_input('Directory: ')
domain = raw_input('Domain string to exclude: ').lower()
finished = 'n'

if not os.path.exists(directory_name):
   os.mkdir(directory_name)

while 'n' == finished:
   url = raw_input('URL to mine: ')
   directory_cat = raw_input('Name of category: ')
   code = raw_input('Code for this category: ')

   listing_filename = directory_name + '/' + directory_cat
   urllib.urlretrieve(url, filename=listing_filename)
   csv_filename = 'all_links.csv'

   with open(csv_filename, 'a') as csvfile:
      csv_writer = csv.writer(csvfile, delimiter='\t')
      listing = BeautifulSoup(open(listing_filename, 'r'), 'html.parser')
      for link in listing.find_all('a'):
         href = link.get('href').lower()
         if 'mailto' not in href and domain not in href and 'http' in href:
            clean_link = re.search(r'(http.*)$', link.get('href')).group(0)
            csv_writer.writerow([clean_link, directory_name, directory_cat, code])
   finished = raw_input('Finished? y/n: ')
