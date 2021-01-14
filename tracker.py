import urllib.request, json 
with urllib.request.urlopen("https://hiveon.net/api/v1/stats/miner/a438abea8bfb8855adcb08d4a369f751148522ae/ETH/workers") as url:
    data = json.loads(url.read().decode())
    for workername,workerstats in data['workers'].items():
        print(workername, ",", workerstats['sharesStatusStats']['validCount'])