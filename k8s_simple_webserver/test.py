from requests_html import HTMLSession
from datetime import datetime as dt
 
session = HTMLSession()
resp = session.get("http://10.1.181.100/")
print(resp.status_code)

resp.html.render()
tags = resp.html.find("p")
podDate = tags[0]

testDate = dt.now().strftime("%d/%m/%Y")

podDate = dt.strptime(podDate.text, "%d/%m/%Y")
testDate = dt.strptime(testDate, "%d/%m/%Y")

print(podDate==testDate)