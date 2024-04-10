def update_or_add_profile(name, id, accountId, puuid, profileIconId, summonerLevel):
        with open('profiles.txt', 'r') as file:
            lines = file.readlines()
        updated = False
        with open('profiles.txt', 'w') as file:
            for line in lines:
                # puuid 값이 일치하는 항목을 찾아서 업데이트
                if line.split(',')[3].strip() == puuid:
                    file.write(f"{name}, {id}, {accountId}, {puuid}, {profileIconId}, {summonerLevel}\n")
                    updated = True
                else:
                    file.write(line)
            # puuid 값이 일치하는 항목이 없으면 새로운 항목 추가
            if not updated:
                file.write(f"{name}, {id}, {accountId}, {puuid}, {profileIconId}, {summonerLevel}\n")
        print("프로필 저장 완료")