import requests
import apiKey

# Riot Games API Key
api_key = apiKey.key

# 소환사 이름
summoner_name = "지송구"

# Summoner API 호출을 위한 URL
summoner_url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}"

# Summoner API 호출
response = requests.get(summoner_url)

# 소환사 정보 가져오기
if response.status_code == 200:
    summoner_info = response.json()
    summoner_id = summoner_info['id']
    
    # League API 호출을 위한 URL
    league_url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}"

    # League API 호출
    response = requests.get(league_url)

    # 랭크 정보 가져오기
    if response.status_code == 200:
        rank_info = response.json()
        if rank_info:
            print(f"소환사 {summoner_name}의 현재 랭크 정보:")
            for entry in rank_info:
                print(f"큐 타입: {entry['queueType']}, 티어: {entry['tier']} {entry['rank']}, LP: {entry['leaguePoints']}, 승리/패배: {entry['wins']}/{entry['losses']}")
        else:
            print(f"소환사 {summoner_name}은(는) 현재 랭크 정보가 없습니다.")
    else:
        print("League API 호출에 실패했습니다.")
else:
    print("Summoner API 호출에 실패했습니다.")
