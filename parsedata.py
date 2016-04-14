#coding = UTF-8

import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cwb.gov.tw/V7/observe/real/windAll.htm")
soup = BeautifulSoup(response.content.decode("utf-8"),"lxml")

station_N = soup.find_all("tr",{"class":"TypeN"})
for i in range(25):
	name=station_N[i].find_all("td")
	yellow=station_N[i].find_all("td",{"class":"yellow"})
	orange=station_N[i].find_all("td",{"class":"orange"})
	for td in yellow:	
		print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:5])
		payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
		req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
		print(req)
	for td in orange:
		if td.text[3]!='.':
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0:2]+" 公尺每秒:"+td.text[2:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)
		else:	
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)	


station_C = soup.find_all("tr",{"class":"TypeC"})
for i in range(25):
	name=station_C[i].find_all("td")
	yellow=station_C[i].find_all("td",{"class":"yellow"})
	orange=station_C[i].find_all("td",{"class":"orange"})
	for td in yellow:	
		print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
		payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
		req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
		print(req)
	for td in orange:
		if td.text[3]!='.':
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0:2]+" 公尺每秒:"+td.text[2:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)
		else:	
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)	


station_S = soup.find_all("tr",{"class":"TypeS"})
for i in range(18):
	name=station_S[i].find_all("td")
	yellow=station_S[i].find_all("td",{"class":"yellow"})
	orange=station_S[i].find_all("td",{"class":"orange"})
	for td in yellow:	
		print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
		payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
		req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
		print(req)
	for td in orange:
		if td.text[3]!='.':
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0:2]+" 公尺每秒:"+td.text[2:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)
		else:	
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)	


station_E = soup.find_all("tr",{"class":"TypeE"})
for i in range(18):
	name=station_E[i].find_all("td")
	yellow=station_E[i].find_all("td",{"class":"yellow"})
	orange=station_E[i].find_all("td",{"class":"orange"})	
	for td in yellow:	
		print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
		payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
		req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
		print(req)
	for td in orange:
		if td.text[3]!='.':
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0:2]+" 公尺每秒:"+td.text[2:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)
		else:	
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)	


station_I = soup.find_all("tr",{"class":"TypeI"})
for i in range(6):
	name=station_I[i].find_all("td")
	yellow=station_I[i].find_all("td",{"class":"yellow"})
	orange=station_I[i].find_all("td",{"class":"orange"})
	for td in yellow:	
		print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
		payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
		req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
		print(req)
	for td in orange:
		if td.text[3]!='.':
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0:2]+" 公尺每秒:"+td.text[2:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)
		else:	
			print(name[0].text+" "+name[1].text+" "+td['title']+" 蒲福風級:"+td.text[0]+" 公尺每秒:"+td.text[1:])
			payload = {"robot_id":"108143422899450","content":td,"lng":"120","lat":"218"}
			req=requests.post("http://52.192.20.250/chat/create/robot/",data=payload)
			print(req)	



