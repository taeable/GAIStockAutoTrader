import urllib.request, json

f= open("price.txt","w+")
url = "https://api.nasdaq.com/api/quote/T/chart?assetclass=stocks&fromdate=2009-12-25&todate=2019-12-24"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read())
    for i in range(len(data['data']['chart'])):
        print(data['data']['chart'][i]['x'])
        print(data['data']['chart'][i]['y'])
        f.write("%d,%f\n" % (data['data']['chart'][i]['x'] , data['data']['chart'][i]['y']))
f.close()
