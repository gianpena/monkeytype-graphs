import requests,sys,json
from time import sleep
class StatsFetcher:
    def __init__(self, language='english', mode='time', mode2='60'):
        self.aggregated_data = []
        page=0
        r = requests.get(f'https://api.monkeytype.com/leaderboards?language={language}&mode={mode}&mode2={mode2}&page={page}&pageSize=200').json()
        while r['data']['entries'][-1]['rank'] != r['data']['count']:
            self.aggregated_data.extend(r['data']['entries'])
            page += 1
            sleep(8)
            r = requests.get(f'https://api.monkeytype.com/leaderboards?language={language}&mode={mode}&mode2={mode2}&page={page}&pageSize=200').json()

        self.aggregated_data.extend(r['data']['entries'])
        print(json.dumps(self.aggregated_data))




sf = StatsFetcher(mode2=sys.argv[1])