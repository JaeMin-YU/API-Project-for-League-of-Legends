import requests
import apiKey
import requestList
import profileSave

def search():

    # 유저 기본 정보 검색
    key = apiKey.key
    api_url = requestList.summoner

    findName = input("\n유저명 입력: ")

    api_url = api_url + findName + '?api_key=' + apiKey.key
    resp = requests.get(api_url)
    if resp.status_code == 200:
        summoner_info = resp.json()
        id = summoner_info['id']
        accountId = summoner_info['accountId']
        puuid = summoner_info['puuid']
        profileIconId = summoner_info['profileIconId']
        summonerLevel = summoner_info['summonerLevel']

        #저장
        profileSave.update_or_add_profile(findName, id, accountId, puuid, profileIconId, summonerLevel)

    # API 오류 발생 혹은 입력돈 소환사 정보가 잘못된 경우
    else:
        print("Summoner API 호출에 실패 했습니다.\n")
