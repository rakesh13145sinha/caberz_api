






import http.client
conn=http.client.HTTPConnection("2factor.in/API/V1")
payload={ "Status": "Success", "Details": "5D6EBEE6-EC04-4776-846D"}
headers={
    'authkey':"e2620bdd-53bb-11ea-9fa5-0200cd936042",
    'content-type':"application/json"
}
conn.request("POST","/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/+91{user's_phone_no}/AUTOGEN",payload,headers)
res=conn.getresponse()
data=res.read()
print (data.decode("utf-8"))


