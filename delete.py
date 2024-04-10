def userInfo():
    # 'profiles.txt' 파일을 열고 내용을 모두 지우기
    with open('profiles.txt', 'w') as file:
        file.truncate(0)

    print("삭제가 완료되었습니다.")