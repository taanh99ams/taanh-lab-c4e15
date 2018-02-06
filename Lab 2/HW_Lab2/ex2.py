from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

raw_data = urlopen(url).read()
html_content = raw_data.decode("utf-8")

html_file = open("cafef.html", "wb")
html_file.write(raw_data)
html_file.close()

#Extract ROI:
soup = BeautifulSoup(html_content, "html.parser")
div = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
table = div.find("table", id="tableContent")
tr_list = table.find_all("tr")

report = []
for tr in tr_list:
    td_list = tr.find_all("td")
    for td in td_list:
        col1 = td_list[0].string
        col2 = td_list[1].string
        col3 = td_list[2].string
        col4 = td_list[3].string
        col5 = td_list[4].string

    data_list = {
        " ": col1,
        "Quý 4 - 2016": col2,
        "Quý 1 - 2017": col3,
        "Quý 2 - 2017": col4,
        "Quý 3 - 2017": col5
}
    report.append(data_list)

pyexcel.save_as(records=report,dest_file_name="Cafef_financial_report.xlsx")
