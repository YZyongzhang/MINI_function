import urllib.request as url
from bs4 import BeautifulSoup
import html2text as ht

# 从目标网页获取内容
request = url.Request(url='https://blog.csdn.net/clover661/article/details/119607419')
html = url.urlopen(request).read().decode('utf-8')
html = BeautifulSoup(html, 'lxml')

# 提取目标 div 内容
div_content = html.find("div", id="content_views")

# 读取本地 HTML 文件
with open("myhtml.html", 'r+', encoding='utf-8') as origin_html:
    origin_page = BeautifulSoup(origin_html, 'lxml')

    # 找到目标 div 在本地文件中的位置
    target_div = origin_page.find('div', class_="content")
    
    # 将获取的 div 内容插入目标 div
    if target_div:
        target_div.append(div_content)
    text_maker = ht.HTML2Text()
    # 将修改后的内容写入新的文件
    with open("csdn_blog.md", "w+", encoding='utf-8') as file:
        file.write(text_maker.handle(origin_page.prettify()))