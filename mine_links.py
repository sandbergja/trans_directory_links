from bs4 import BeautifulSoup
import csv
import re

listing_filename = 'abg/articles.shtml'
csv_filename = 'all_links.csv'
directory_name = 'ABGender'
directory_cat = 'articles'
code = ''

with open(csv_filename, 'a') as csvfile:
   csv_writer = csv.writer(csvfile, delimiter='\t')
   listing = BeautifulSoup(open(listing_filename, 'r'), 'html.parser')
   for link in listing.find_all('a'):
      href = link.get('href')
      if 'mailto' not in href and 'http' in href:
         clean_link = re.search(r'(http.*)$', link.get('href')).group(0)
         csv_writer.writerow([clean_link, directory_name, directory_cat, code])

