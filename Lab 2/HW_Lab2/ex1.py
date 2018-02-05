from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

#Part 1: Make an Excel file of USUK song chart
url = "https://www.apple.com/itunes/charts/songs/"
html_content = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul","")

li_list = ul.find_all("li")

hit_chart = []

for li in li_list:
    a_name = li.h3.a
    a_artist = li.h4.a
    name = a_name.string
    artist = a_artist.string
    hit_song = {
        "Song name": name,
        "Artist": artist
    }
    hit_chart.append(hit_song)

print(hit_chart)
pyexcel.save_as(records=hit_chart, dest_file_name="USUK_Song_Chart.xlsx")

#Part 2: Download those songs from Youtube
for song in hit_chart:
    options = {
        "default_search": "ytsearch",
        "max_downloads": 1
    }
    dl = YoutubeDL(options)
    dl.download(["{0} {1}".format(song["Song name"],song["Artist"])])
