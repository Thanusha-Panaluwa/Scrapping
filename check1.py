import mechanize  #pip install mechanize
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

req = br.open("https://www.allpartsstore.com/ItemDetl.htm?ResultsList=210308292783924&CategorySeq=&SelcBrand=&SelcMachn=&SelcModel=&SelcSectn=&SelcSubsc=&SearchCross=1&TextSearch=A-87730185&ItemNumber=84402652").read()

soup = BeautifulSoup(req)
#print (soup)
## check your code first

#image_tags = soup.find("img", alt='A-84402652')
#print(image_tags)

#image_tags = soup.find_all("img", alt="A-84402652")
#print ("\n image \n")
#print (image_tags)

####WORKING####
part_num = soup.find_all('span', class_="partNumber")
data=part_num.span.span.contents
print(part_num)
inside_num = part_num.find_all(itemprop="mpn")
print(inside_num)

######WORKING#####
print('detail')
detail= soup.find('div', id='partDescription')
print(detail)
detail1=detail.find('span', itemprop='name').text
print(detail1)

########WORKING######
print('weight')
weight= soup.find_all('div', class_='partPrice')
weight1= weight.get_text()
print(weight)


#print('Flighting Diameter')
##Fli_diameter= soup.find("div")
##print (Fli_diameter.text)
#for fl in Fli_diameter:
   # fli= BeautifulSoup(str(fl))
    #fli_d=fli.find("attContainer")
   # fli_d1= fli_d.find_all("span")
  #  print(fli_d1[0])

###########WORKING########    
dataset = [(x.text, y.text) for x,y in zip(part_num, detail)]

with open("output.csv", "w") as csvfile: #write your file name
    writer = csv.writer(csvfile)
    for data in dataset[:250]: #truncate to 250 rows
        writer.writerow(data)
