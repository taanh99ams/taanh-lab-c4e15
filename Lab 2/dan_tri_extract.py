url = "http://dantri.com.vn/"

output_file_name = "news.xlsx"

#Step 1: Download information on the Dantri website
from urllib.request import urlopen
from bs4 import BeautifulSoup


#1.1: Open a connection
conn = urlopen(url)

#1.2: read
raw_data = conn.read()   #byte

#1.3: Decode
html_content = raw_data.decode('utf-8')

# Faster way
# from urllib.request import urlopen
# html_content = urlopen(url).read().decode('utf-8')
# print(html_content)
# print(html_content)

#How to save html_content as a file (in case internet is weak)
# html_file = open("dantri.html","wb")            #write: byte
# html_file.write(raw_data)
# html_file.close()

#Step 2: Extract ROI (Region of interest)

#Create a soup
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify)
ul = soup.find("ul", "ul1 ulnew")
# find chi dung cho tim 1 cai
# print(ul.prettify())
li_list = ul.find_all("li")
#find_all dung cho tim tat ca
# for li in li_list:
#     print(li)
#     print("***" * 10)

#Step 3: Extract News
news_list = []

for li in li_list:
# li = li_list[0]
# h4 = li.h4      #h4 = li.find("h4")
# a = h4.a

#better way:
# a = li.h4.a   (or li.a)
    a = li.h4.a
    href = url + a["href"]
    title = a.string
    news = {
        "title": title,
        "link": href
    }
    news_list.append(news)

print(news_list)
