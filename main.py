import findUser

while True:
    processNumber = input("실행할 프로세스를 선택하세요.\n 1. 유저 저장 \n 2. 매치 생성\n 3. 프로그램 종료 \n -->  ")

    if processNumber == '1':
        findUser.search()  # findUser 함수를 호출
    elif processNumber == '2':
        print('구현 중')
        break
    elif processNumber == '3':
        break
    else:
        print('다시 입력하세요. \n')
