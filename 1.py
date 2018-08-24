import requests
from bs4 import BeautifulSoup
import csv


def html_parser(url_start):
    # 获取html
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  # 模拟浏览器登入
        r = requests.get(url_start, headers=headers, timeout=10)  # 获取网页
    except:
        pass
        # print(r.status_code)
    else:
        html = r.content.decode('gb2312', 'ignore')  # 解码gb2312，忽略其中有异常的编码，仅显示有效的编码

        # print(len(html))

# 解析网页
    soup = BeautifulSoup(html, 'lxml')
    for li in soup.select('.co_area2 li'):  # 选择所有class=co_area2 下的所有的 li 节点
      for a in li.select('a'):  # 选择 li 节点下的 a 节点
          link = url_start + a['href']  # 构造每个电影的网页链接
          item = {  # 将获取的结果存储为字典
              "name": a.string,
              "link": link
          }
          save_result(item)  # 每次获取一个结果后，存储一次
          item.clear()  # 存储后清空字典，为下次存储做准备

def save_result(item):  # 存储结果

    with open('dy.csv', 'a', newline='', encoding='utf-8') as csvfile:  # 打开一个csv文件，用于存储
        fieldnames = ['name', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(item)

def main():  # 主程序
    with open('dy.csv', 'a', newline='') as csvfile:  # 写入表头
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'link'])

    url_start = "https://www.dy2018.com/"
    html_parser(url_start)

if __name__ == '__main__':  # 运行主程序
    main()