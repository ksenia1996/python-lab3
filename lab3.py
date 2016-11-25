import requests
import datetime as dt
f=open('result.html', 'w', encoding='utf-8')
f.write('<!DOCTYPE html><html><head><meta charset=UTF-8"></head><body><ul>')
f.write("<h3 style='text-align:center;'>"+"Events in New York"+"</h3>")
f.write("<h3 style='text-align:center;'>"+str(dt.date.today())+" - "+str(dt.date.today()+dt.timedelta(days=7))+"</h3>")
r=requests.get('https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=48.836452&topic=php&city=Paris&category=34&lon=2.413619&radius=10&page=20&time=,1w&key=2d44d7d3062672b7d28101c73774f2d')
data_all = r.json()
dat=[]
for item in data_all['results']:
	time=dt.datetime.fromtimestamp(int(str(item['time'])[0:10]))
	dat.append(dt.datetime.date(time))
i=0
for item in data_all['results']:
	time=dt.datetime.fromtimestamp(int(str(item['time'])[0:10]))
	newdat=str(dt.datetime.date(time))
	if newdat==dat[i]:
		f.write("<div>"+"<h3>" +str(i+1)+ " " + "Date:" + "</h3>" + str(newdat) +"</div>")
		f.write("<div>" + "<h3>Name: " + "</h3>" + str((item['group'])['name'])+"</div>")
		f.write("<div>" + "<h3>" + "Address: " + "</h3>" + str((item['venue'])['address_1'])+"</div>")
		try:
    		  f.write("<div>" + "<h3>" + "Discription : " + "</h3>" + str(item['description'])+"</div>" )
		except:pass
	else:
		
		f.write("<div>"+"<h3>" +str(i+1)+ " " + "Date:" + "</h3>" + str(newdat) +"</div>")
		f.write("<div>" + "<h3>Name: " + "</h3>" + str((item['group'])['name'])+"</div>")
		f.write("<div>" + "<h3>" + "Address: " + "</h3>" + str((item['venue'])['address_1'])+"</div>")
		try:
    		  f.write("<div>" + "<h3>" + "Discription : " + "</h3>" + str(item['description'])+"</div>" )
		except:pass
	i=i+1
f.close()