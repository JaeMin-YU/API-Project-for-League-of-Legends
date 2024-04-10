import findUser
import delete

while True:
    processNumber = input("실행할 프로세스를 선택하세요.\n 1. 유저 저장 \n 2. 매치 생성\n 3. 프로그램 종료\n 4. 데이터 삭제 \n -->  ")

    # 1번 유저 저장
    if processNumber == '1':
        findUser.search()  # findUser 함수를 호출
    # 2번 밸런스 계산하여 자동 배치
    elif processNumber == '2':
        print('구현 중')
        break
    # 3번 프로그램 종료
    elif processNumber == '3':
        break
    # 4번 데이터 삭제
    elif processNumber == '4':
        delete.userInfo()
        break
    # 5번 잘못 입력한 경우 
    else:
        print('다시 입력하세요. \n')
