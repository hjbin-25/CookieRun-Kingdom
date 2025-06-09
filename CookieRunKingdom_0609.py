import random
import time

# 쿠키 정보 저장
allCookiesInfo = {"용감한 쿠키": "당신은 자신감 폭발~ 나를 따르라! 용감한 쿠키입니다.\n\
자신감 폭발 나를 따르라 형 용감한 쿠키군은 자신이 원하는 것을 잘 알고 있고, 그것을 성취하기 위해 실행으로 옮기는 편입니다.\n\
자신감이 넘치며, 자신에게 이목이 쏠리는 것을 부담스러워 하지 않기도 합니다.\n\
논리적인 사고나 계획에 의해서 움직이는 것은 아니지만, 목표가 생기면 거침없이 돌진합니다. 가치가 있다고 여겨지는 일을 하는 것을 좋아하며,\n\
남에게 통제를 받는 것보다는 스스로 결정하고 주위에 영향력을 끼치곤 합니다.\n\
분위기를 주도하는 능력이 뛰어나 친구들이 많고 주위 사람들과도 두루 잘 지내는 성격입니다. 평소에는 당신이 하고 싶은 대로 내버려 두지만\n\
아주 중요한 순간에 큰 힘을 실어줄 수 있는 이성을 만나는 것이 좋습니다."}

# 희귀도가 일반인 쿠키들
commonCookiesList = ["용감한 쿠키", "딸기맛 쿠키", "마법사맛 쿠키", "닌자맛 쿠키", "근육맛 쿠키"]
# 희귀도가 희귀인 쿠키들
rareCookiesList = ["클로버맛 쿠키", "커스터드 3세맛 쿠카"]
# 희귀도가 에픽인 쿠키들
epicCookiesList = ["웨어울프맛 쿠키", "다크초코 쿠키", "자색고구마맛 쿠키", "구미호맛 쿠키", "벨벳케이크맛 쿠키", "라즈베리맛 쿠키"]
# 희귀도가 전설인 쿠키들
legendaryCookiesList = ["바다요정 쿠키", "블랙펄 쿠키"]
# 희귀도가 고대인 쿠키들
ancientCookiesList = ["다크카카오 쿠키", "홀리베리 쿠키", "퓨어바닐라 쿠키"]
# 희귀도가 비스트인 쿠키들
beastCookiesList = ["이터널슈가 쿠키", "쉐도우밀크 쿠키"]

# 메인 플레이를 진행할 클래스, 모든 기능은 이 클래스에서 구현함
class CookieRunKingdom:
    # 기본적인 정보를 할당 및 호출할 생성자
    def __init__(self):
        tempUserName = None

        while True:
            tempUserName = input("닉네임: ")

            isUserAgree = input(f"{tempUserName}으로 하시겠습니까? (y, n): ")

            if isUserAgree == 'y':
                break
            
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
        print("\n\n")

        self.userNickName = tempUserName    # 이름
        self.userLevel = 0                  # 레벨
        self.userOwnCookies = ["용감한 쿠키"]  # 보유 쿠키
        self.userCookiesCounter = 1         # 보유 쿠키 수 저장
        self.userGold = 0                   # 골드
        self.userDiamond = 0                # 다이아몬드
        self.currentStage = 1               # 현재 스테이지 저장
        self.frame = 1                      # 현재 남아있는 뽑기 틀의 개수 저장
        self.cookiePiece = 0                # 강화에 쓸 쿠키 조각 개수 저장

        # 쿠폰 코드 저장 (리스트 형태로 보상이 저장 [골드, 다이아몬드, 쿠키틀])
        self.couponCode = {"암소의 과학 공부": [10000, 3000, 100], "암소의 포트폴리오": [3000, 4500, 125]}

        print("-" * 50)
        print("[ 종료버튼: -1 ]")
        print("-" * 50)

    # 닉네임 변경
    def setUserNickName(self):
        while True:
            newUserNickName = input("새 닉네임: ")

            isUserAgree = input(f"{newUserNickName}으로 변경하시겠습니까? (y, n): ")

            if isUserAgree == '-1':
                print("게임 종료")
                exit()

            if isUserAgree == 'y':
                self.userNickName = newUserNickName
                print("닉네임이 성공적으로 변경되었습니다.")
                return
            else:
                print("닉네임 변경을 취소합니다.")
                return
    
    # 닉네임 출력
    def getUserNickName(self):
        print("-" * 50)
        print(f"닉네임: {self.userNickName}")
        print("-" * 50)

        print()

    # 보유중인 쿠키 출력
    def getCurrentOwnCookies(self):
        print("-" * 50)
        for cookieIndex in range(len(self.userOwnCookies)):
            if (cookieIndex + 1) % 5 == 0:
                print()
            
            print(f"[ {self.userOwnCookies[cookieIndex]} ]")
            if cookieIndex + 1 < len(self.userOwnCookies):
                print(", ", end='')
        
        print()

        print("상호작용 할려면 이름으로 접근하세요.")
        
        print("-" * 50)

    # 쿠키틀 뽑기 최적화
    def cookieFrameByLotInner(self):
        if self.frame >= 1:
            self.frame -= 1
            chosenResult = random.randint(1, 100)

            if chosenResult <= 50:
                appendCookie = commonCookiesList[random.randint(0, len(commonCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 5개\n")
                    self.cookiePiece += 5

            elif chosenResult <= 75:
                appendCookie = rareCookiesList[random.randint(0, len(rareCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 10개\n")
                    self.cookiePiece += 10

            elif chosenResult <= 85:
                appendCookie = epicCookiesList[random.randint(0, len(epicCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 25개\n")
                    self.cookiePiece += 25
            
            elif chosenResult <= 91:
                appendCookie = legendaryCookiesList[random.randint(0, len(legendaryCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 75개\n")
                    self.cookiePiece += 75
            
            elif chosenResult <= 99:
                appendCookie = ancientCookiesList[random.randint(0, len(ancientCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 50개\n")
                    self.cookiePiece += 50
            
            else:
                appendCookie = beastCookiesList[random.randint(0, len(beastCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 100개\n")
                    self.cookiePiece += 100
            
            if appendCookie not in allCookiesInfo.keys():
                print("-" * 50)
                print(f"얻은 쿠키: {appendCookie}")
                print("-" * 50)
                time.sleep(3)

                self.userOwnCookies.append(appendCookie)
                print("\n\n\n\n\n\n\n\n\n\n")
            
        else:
            print("재화가 부족해서 뽑기가 중단되었습니다.")
            time.sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n")

    # 쿠키틀 뽑기
    def cookieFrameByLot(self):
        while True:
            # 입력값 저장
            userInput = None

            while True:
                # 명령어 보여줌
                print("-" * 50)
                print("1. 1회 뽑기")
                print("2. 3회 연속 뽑기")
                print("-" * 50)

                print("\n\n\n\n")
        
                print("[ 뽑기 ]")
                try:
                    userInput = int(input("단축키를 입력하세요(숫자만 가능): "))
                # 이상값 확인
                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해주세요.")
                    continue
                else:
                    # 게임종료
                    if userInput == -1:
                        print("게임 종료")
                        exit()
                    # 돌아가기
                    if userInput == 0:
                        return
                    # 1회 뽑기
                    if userInput == 1:
                        self.cookieFrameByLotInner()
                        return
                    
                    # 3회 연속 뽑기
                    if userInput == 2:
                        for _ in range(3):
                            self.cookieFrameByLotInner()
                        return

    # 다이아몬드 뽑기 최적화
    def diamondByLotInner(self):
        if self.userDiamond >= 300:
            self.frame -= 300
            chosenResult = random.randint(1, 100)

            if chosenResult <= 50:
                appendCookie = commonCookiesList[random.randint(0, len(commonCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 5개\n")
                    self.cookiePiece += 5

            elif chosenResult <= 75:
                appendCookie = rareCookiesList[random.randint(0, len(rareCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 10개\n")
                    self.cookiePiece += 10

            elif chosenResult <= 85:
                appendCookie = epicCookiesList[random.randint(0, len(epicCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 25개\n")
                    self.cookiePiece += 25
            
            elif chosenResult <= 91:
                appendCookie = legendaryCookiesList[random.randint(0, len(legendaryCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 75개\n")
                    self.cookiePiece += 75
            
            elif chosenResult <= 99:
                appendCookie = ancientCookiesList[random.randint(0, len(ancientCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 50개\n")
                    self.cookiePiece += 50
            
            else:
                appendCookie = beastCookiesList[random.randint(0, len(beastCookiesList) - 1)]

                if appendCookie in self.userOwnCookies:
                    print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                    print("쿠키 조각 100개\n")
                    self.cookiePiece += 100
            
            if appendCookie not in allCookiesInfo.keys():
                print("-" * 50)
                print(f"얻은 쿠키: {appendCookie}")
                print("-" * 50)
                time.sleep(3)

                self.userOwnCookies.append(appendCookie)
                print("\n\n\n\n\n\n\n\n\n\n")
        else:
            print("재화가 부족해서 뽑기가 중단되었습니다.")
            time.sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n")

    # 다이아몬드 뽑기
    def diamondByLot(self):
        while True:
            # 입력값 저장
            userInput = None

            while True:
                # 명령어 보여줌
                print("-" * 50)
                print("1. 1회 뽑기")
                print("2. 3회 연속 뽑기")
                print("-" * 50)

                print("\n\n\n\n")
        
                print("[ 뽑기 ]")
                try:
                    userInput = int(input("단축키를 입력하세요(숫자만 가능): "))
                # 이상값 확인
                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해주세요.")
                    continue
                else:
                    # 게임종료
                    if userInput == -1:
                        print("게임 종료")
                        exit()
                    # 돌아가기
                    if userInput == 0:
                        return
                    # 1회 뽑기
                    if userInput == 1:
                        self.diamondByLotInner()
                        return
                    
                    # 3회 연속 뽑기
                    if userInput == 2:
                        for _ in range(3):
                            self.diamondByLotInner()
                        return

    # 유저 재화 출력
    def getUserGoods(self):
        print("\n\n\n\n\n\n\n\n\n")
        print("-" * 50)
        print(f"골드: {self.userGold}")
        print(f"다이아몬드: {self.userDiamond}")
        print(f"쿠키틀: {self.frame}")
        print("-" * 50)

        time.sleep(3)

        print("\n\n\n")
    
    # 개발자 지원하기
    def supportDeveloper(self):
        print("\n\n\n\n\n\n\n\n\n")
        print("-" * 50)
        print("대구은행 281-13-082351")
        print("-" * 50)

        time.sleep(10)

        print("\n\n\n\n\n")

    # 설정 부분 가이드북
    def getSettingGuideBook(self):
        print("-" * 50)
        print("1. 닉네임 변경")
        print("2. 닉네임 확인")
        print("3. 회원 탈퇴")
        print("4. 쿠폰 입력")
        print("-" * 50)

        print("\n\n")

    # 상점 부분 가이드북
    def getStoreGuideBook(self):
        print("-" * 50)
        print("1. 쿠키틀 뽑기")
        print("2. 다이아몬드 뽑기")
        print("3. 현재 재화 확인")
        print("4. 개발자 지원하기")
        print("-" * 50)

        print("\n\n")

    # 왕국 부분 가이드북
    def getKingdomGuideBook(self):
        print("-" * 50)
        print("1. 내 쿠키 보기")
        print("2. 왕국 꾸미기")
        print("-" * 50)

        print("\n\n\n\n")

    # 내 쿠키 부분 가이드북
    def getMyCookiesGuideBook(self):
        print("-" * 50)
        print("0. 돌아가기")
        print("1. 쿠키 정보")
        print("2. 쿠키 버리기")
        print("3. 쿠키 강화")
        print("-" * 50)

        print("\n")

    # 기본 가이드북
    def getMethodGuideBook(self):
        print("-" * 50)
        print("0. 돌아가기")
        print("1. 설정")
        print("2. 상점")
        print("3. 플레이")
        print("4. 내 왕국")
        print("-" * 50)

        print()
    
    # 설정 부분 담당
    def setting(self):
        while True:
            # 입력값 저장
            userInput = None

            # 명령어 보여줌
            self.getSettingGuideBook()

            while True:
                print("[ 설정 ]")
                try:
                    userInput = int(input("단축키를 입력하세요(숫자만 가능): "))
                # 이상값 확인
                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해주세요.")
                    continue
                else:
                    # 게임종료
                    if userInput == -1:
                        print("게임 종료")
                        exit()
                    # 돌아가기
                    if userInput == 0:
                        return
                    # 닉네임 변경
                    if userInput == 1:
                        self.setUserNickName()
                        print("\n\n\n\n")
                        return
                    # 닉네임 확인
                    if userInput == 2:
                        self.getUserNickName()
                        return
                    # 계정 삭제
                    if userInput == 3:
                        print("계정 삭제 완료")
                        exit()
                    # 쿠폰 입력
                    if userInput == 4:
                        while True:
                            userInputCode = input("쿠폰 코드 입력: ")

                            if userInputCode == '0':
                                return
                            if userInputCode == '-1':
                                print("게임 종료")
                                exit()
                            
                            if userInputCode in self.couponCode.keys():
                                print("입력 성공")

                                self.userGold += self.couponCode[userInputCode][0]
                                self.userDiamond += self.couponCode[userInputCode][1]
                                self.frame += self.couponCode[userInputCode][2]

                                del self.couponCode[userInputCode]
                                
                                time.sleep(3)

                                print("\n\n\n")

                                return

                    else:
                        print("올바른 번호를 입력해주세요.")
                        continue

    # 상점 부분 담당
    def store(self):
        while True:
            # 입력값 저장
            userInput = None

            while True:
                # 명령어 보여줌
                self.getStoreGuideBook()
    
                print("[ 상점 ]")
                try:
                    userInput = int(input("단축키를 입력하세요(숫자만 가능): "))
                # 이상값 확인
                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해주세요.")
                    continue
                else:
                    print("\n\n\n")
                    # 프로그램 종료
                    if userInput == -1:
                        print("게임 종료")
                        exit()
                    # 돌아가기
                    if userInput == 0:
                        return
                    # 쿠키틀 뽑기
                    if userInput == 1:
                        self.cookieFrameByLot()
                        return
                    # 다이아몬드 뽑기
                    if userInput == 2:
                        self.diamondByLot()
                        return
                    # 현재 재화 확인
                    if userInput == 3:
                        self.getUserGoods()
                        return
                    # 개발자 지원하기
                    if userInput == 4:
                        self.supportDeveloper()
                        return
                    else:
                        print("올바른 번호를 입력해주세요.")
                        continue

    # 쿠키 확인 부분 담당
    def currentCookies(self):
        interactCookie = None
        while True:
            self.getMyCookiesGuideBook()

            self.getCurrentOwnCookies()
            interactCookie = input("접근할 쿠키의 이름을 입력해주세요: ")

            if interactCookie == '-1':
                print("게임 종료")
                exit()
            if interactCookie == '0':
                return

            print()
            if interactCookie in self.userOwnCookies:
                break
            else:
                print("\n\n\n\n")
                print("보유하지 않거나 존재하지 않는 쿠키입니다.")
        
        print("\n\n\n\n\n")

        self.getMyCookiesGuideBook()

        while True:
            print("[ 내 쿠키 ]")
            try:
                userInput = int(input("단축키를 입력하세요(숫자만 가능): "))
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            else:
                print("\n\n\n")
                # 돌아가기
                if userInput == 0:
                    return
                # 해당 쿠키 정보 출력
                if userInput == 1:
                    print("-" * 50)
                    print(f"[ {interactCookie} ]")
                    print(allCookiesInfo[interactCookie])
                    print("-" * 50)
                    time.sleep(5)

                    print("\n\n\n\n\n")
                    return
                # 해당 쿠키 삭제
                if userInput == 2:
                    print("\n\n\n\n\n\n\n\n\n\n")
                    self.userOwnCookies.remove(interactCookie)
                    print(f"{interactCookie} 삭제 완료")
                    time.sleep(1)
                    print("\n\n\n")
                    return
                # 해당 쿠키 강화
                if userInput == 3:
                    print("\n\n\n\n\n\n\n\n\n\n")
                    raise KeyboardInterrupt
                    return
                else:
                    print("올바른 번호를 입력해주세요.")
                    continue

    # 왕국 부분 담당
    def kingdom(self):
        while True:
            # 입력값 저장
            userInput = None

            # 명령어 보여줌
            self.getKingdomGuideBook()

            while True:
                print("[ 왕국 ]")
                try:
                    userInput = int(input("단축키를 입력하세요(숫자만 가능): "))
                # 이상값 확인
                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해주세요.")
                    continue
                else:
                    print()
                    # 개임 종료
                    if userInput == -1:
                        print("게임 종료")
                        exit()
                    # 돌아가기
                    if userInput == 0:
                        return
                    # 내 쿠키
                    if userInput == 1:
                        self.currentCookies()
                        return
                    # 왕국 꾸미기
                    if userInput == 2:
                        print("미완성")
                        raise RuntimeError
                        return
                    else:
                        print("올바른 번호를 입력해주세요.")
                        continue

    # 메인 플레이를 진행할 플레이 함수
    def playCookieRunKingdom(self):
        while True:
            # 입력값 저장
            userInput = None

            while True:
                # 명령어 보여줌
                self.getMethodGuideBook()
                print()
                print("[ 메뉴 ]")
                try:
                    userInput = int(input("단축키를 입력하세요(숫자만 가능): "))
                # 이상값 확인
                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해주세요.")
                    continue
                else:
                    print("\n\n\n")
                    if userInput == -1:
                        print("게임 종료")
                        exit()
                    # 설정
                    if userInput == 1:
                        self.setting()
                        continue
                    if userInput == 2:
                        self.store()
                        continue
                    if userInput == 3:
                        print("미완성")
                        raise RuntimeError
                        continue
                    if userInput == 4:
                        self.kingdom()
                        continue
                    else:
                        print("올바른 번호를 입력해주세요.")
                        continue


# 메인 함수 부분
print("\n\n\n\n\n\n\n\n\n\n\n")
print("쿠키런: 킹덤 (Cookie Run: Kingdom)\n\n\n")
print("다양한 쿠키를 수집하고 육성해 전투를 펼치며, 나만의 왕국을 건설하는 전략 RPG입니다.\n\
실시간 자동 전투와 PvP, 보스전 등 다채로운 전투 콘텐츠가 기다리고 있습니다.\n\
자원을 모아 왕국을 성장시키고, 개성 넘치는 꾸미기로 나만의 세상을 만들어보세요.\n\
매일 새로워지는 이벤트와 스토리로 끝없는 재미를 즐기실 수 있습니다.")

print("-" * 50 + '\n')

callingVar = CookieRunKingdom()
callingVar.playCookieRunKingdom()