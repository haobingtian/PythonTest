# import requests
# from bs4 import BeautifulSoup
# content=requests.get('http://www.qiushibaike.com').content
# soup=BeautifulSoup(content,'html.parser')
# for div in soup.find_all('div',{'class':'content'}):
#     print (div.text.strip())
#
# if __name__=='__main__':
#         print("Hello world")
import  re
t1="someone@gmail.com"
t2="bill.gates@microsoft.com"
t3="<Tom Paris>tom@voyager.com"
m1= re.match(r'^[0-9a-zA-Z]*[.]*[0-9a-zA-Z]+@[0-9a-zA-Z]+.com$',t2)
print(m1)
m2=re.match(r'^<([a-zA-Z.\s]+)>[a-zA-Z]+@[a-zA-Z]+[".org"|".com"]{4}$',t3)
print(m2)
print("啦啦啦")

