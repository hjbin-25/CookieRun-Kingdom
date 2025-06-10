import random
import time

# 쿠키 정보 저장
allCookiesInfo = {"용감한 쿠키": """당신은 자신감 폭발~ 나를 따르라! 용감한 쿠키입니다.
자신감 폭발 나를 따르라 형 용감한 쿠키군은 자신이 원하는 것을 잘 알고 있고, 그것을 성취하기 위해 실행으로 옮기는 편입니다.
자신감이 넘치며, 자신에게 이목이 쏠리는 것을 부담스러워 하지 않기도 합니다.
논리적인 사고나 계획에 의해서 움직이는 것은 아니지만, 목표가 생기면 거침없이 돌진합니다. 가치가 있다고 여겨지는 일을 하는 것을 좋아하며,
남에게 통제를 받는 것보다는 스스로 결정하고 주위에 영향력을 끼치곤 합니다.
분위기를 주도하는 능력이 뛰어나 친구들이 많고 주위 사람들과도 두루 잘 지내는 성격입니다. 평소에는 당신이 하고 싶은 대로 내버려 두지만
아주 중요한 순간에 큰 힘을 실어줄 수 있는 이성을 만나는 것이 좋습니다.""",

"딸기맛 쿠키": """딸기의 상큼하고 달콤한 향기를 가득 담은 딸기맛 쿠키는 사랑스러운 외모만큼이나 부드럽고 친근한 매력을 지녔다.
겉보기엔 수줍음이 많아 보이지만, 소중한 친구를 위해서라면 망설임 없이 용기를 내는 따뜻한 마음의 소유자다.
딸기 시럽이 흐르는 망토와 함께 달콤한 향기를 퍼뜨리며, 주변 모두를 기분 좋게 만드는 사랑받는 존재다.""",

"마법사맛 쿠키": """화려한 별가루와 신비한 마법의 힘을 지닌 마법사맛 쿠키는 밤하늘처럼 깊고 오묘한 매력을 뽐낸다.
긴 모자와 반짝이는 망토는 그의 마법 실력을 상징하며, 호기심 많은 성격으로 항상 새로운 주문을 연구 중이다.
때로는 덤벙대지만, 필요할 때는 믿음직한 힘이 되어 주는 든든한 존재다.""",

"닌자맛 쿠키": """그림자처럼 빠르고 조용하게 움직이는 닌자맛 쿠키는 날렵한 몸놀림과 침착한 판단력이 돋보인다.
간결한 말투와 쿨한 태도를 지녔지만, 은근히 동료들을 챙기는 따뜻한 마음을 숨기고 있다.
전투에서는 손에 든 수리검보다 더 날카로운 집중력으로 눈 깜짝할 새 적을 제압한다.""",

"근육맛 쿠키": """단단한 반죽 위에 뿜어져 나오는 힘과 열정, 근육맛 쿠키는 언제나 에너지 넘치고 활기찬 분위기를 만든다.
운동과 친구를 좋아하는 그는 사소한 일에도 큰 웃음을 터뜨리는 명랑한 분위기 메이커다.
무슨 일이든 정면 돌파하는 스타일로, 어려움 앞에서도 절대 포기하지 않는 강한 의지를 지녔다.""",

"클로버맛 쿠키": """작은 풀잎 하프를 연주하며 자연과 교감하는 순수한 마음의 소유자.
불운한 상황에서도 희망의 노래를 잃지 않고, 동료들에게 위로와 용기를 전한다.
잔잔한 미소와 부드러운 음악은 언제나 평화를 불러온다.""",

"커스터드 3세맛 쿠키": """스스로를 위대한 왕이라 칭하지만, 아직은 호기심 가득한 꼬마 쿠키.
작은 왕관을 쓰고 마법지팡이를 휘두르며 진짜 왕이 되기 위한 모험을 떠난다.
엉뚱하지만 귀엽고 정의로운 마음으로 모두의 미소를 이끌어낸다.""",

"웨어울프맛 쿠키": """두 개의 모습, 쿠키와 야수 사이를 오가는 슬픔을 품은 전사.
분노의 밤에는 강력한 힘으로 전장을 지배하지만, 그 안엔 외로움이 깃들어 있다.
거칠지만 누구보다 진심 어린 마음으로 동료를 지키려 한다.""",

"다크초코 쿠키": """깊은 죄책감과 어두운 힘을 지닌 검은 검사의 전설.
강력한 힘을 가졌지만, 그 힘으로 상처를 준 과거를 스스로 짊어진다.
차가운 외면 너머에 숨겨진 따뜻한 마음은 그 누구보다 깊다.""",

"자색고구마맛 쿠키": """외모는 무섭지만 속은 누구보다 순한 심성의 쿠키.
힘을 쓰는 일을 좋아하며, 도움이 필요하면 언제든 달려온다.
울컥하는 감정 표현이 많지만, 진심은 진실하다.""",

"구미호맛 쿠키": """아름다운 외모와 신비로운 분위기를 지닌 전설 속 존재.
낮에는 쿠키, 밤에는 여우의 모습으로 변하며 외로움을 안고 살아간다.
속삭이듯 부드러운 말투 속에는 수백 년의 기억이 담겨 있다.""",

"벨벳케이크맛 쿠키": """고귀한 자태와 예술적인 전투 스타일로 적을 유혹하는 전장 위의 퍼포머.
부드러움 속에 감춰진 날카로운 칼날은 적에게 치명적이다.
그 누구보다 우아하고 치명적인 무대를 선보인다.""",

"라즈베리맛 쿠키": """귀족 명문 가문의 후계자로, 검술과 자부심 모두를 갖춘 완벽주의자.
명예를 중시하며, 무사로서의 자존심에 흠이 나는 것을 용납하지 않는다.
치밀한 검격 속에 뜨거운 열정과 집념이 숨겨져 있다.""",

"바다요정 쿠키": """심해의 고요와 분노를 함께 지닌 바다의 정령.
과거의 상처로 얼어붙은 마음을 지녔지만, 그 안엔 깊은 슬픔이 흐른다.
파도처럼 아름답고, 폭풍처럼 강력한 힘을 자유자재로 다룬다.""",

"블랙펄 쿠키": """어둠이 깃든 심해의 왕좌에 앉은 검은 진주의 주인.
침묵 속에서 깊은 심연을 지배하며, 누구도 감히 다가설 수 없는 위엄을 품었다.
그 존재만으로도 모든 것을 압도하는 절대적인 카리스마의 소유자.""",

"다크카카오 쿠키": """엄혹한 검은 산맥을 다스리는 강철 같은 지도자.
무거운 침묵과 단호한 의지로 자신과 나라를 지켜온 전사의 상징.
한 자루의 검에 역사를 담아, 정의를 위해 휘두른다.""",

"홀리베리 쿠키": """언제나 앞장서서 싸우는 명랑한 수호자의 표본.
힘이 넘치고 활기차며, 웃음 속에서도 강인한 책임감을 잃지 않는다.
우정과 용기를 중시하는 그녀는 모두의 든든한 언니 같은 존재.""",

"퓨어바닐라 쿠키": """치유의 마법과 지혜를 겸비한 고대의 대마법사.
언제나 부드러운 미소로 모두를 감싸며, 어둠 속에서도 희망을 잃지 않는다.
진심 어린 마음이 모든 상처를 치유하는 기적을 이룬다.""",

"이터널슈가 쿠키": """끝없는 단맛의 저편에서 태어난 미지의 존재.
은은하게 반짝이는 눈동자와 무형의 실루엣은 현실과 환상을 넘나든다.
시간조차도 느끼지 못할 만큼 부드럽고, 동시에 날카로운 단맛을 지닌 전설의 수호자.""",

"쉐도우밀크 쿠키": """어둠의 안개처럼 나타났다 사라지는 정체불명의 야수 쿠키.
새하얀 피부에 스며든 그림자들은 조용하지만 위협적인 존재감을 발산한다.
달빛 아래서 본 모습은 순식간에 사라지며, 흔적조차 남기지 않는다."""}

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

        self.userNickName = tempUserName                 # 이름
        self.userLevel = 0                               # 레벨
        # 보유 쿠키 이름-레벨 딕셔너리
        self.userOwnCookieNameToLevel = {"용감한 쿠키": 1, "딸기맛 쿠키": 1, "마법사맛 쿠키": 1, "닌자맛 쿠키": 1, "근육맛 쿠키": 1}
        # 보유 쿠키 이름-전투력 딕셔너리
        self.userOwnCookieNameToCombatPower = {"용감한 쿠키": 1000, "딸기맛 쿠키": 1000, "마법사맛 쿠키": 1000, "닌자맛 쿠키": 1000, "근육맛 쿠키": 1000}
        self.userCookiesCounter = 1                      # 보유 쿠키 수 저장
        self.userGold = 0                                # 골드
        self.userDiamond = 1000                          # 다이아몬드
        self.currentStage = 1                            # 현재 스테이지 저장
        self.frame = 1                                   # 현재 남아있는 뽑기 틀의 개수 저장
        self.cookiePiece = 0                             # 강화에 쓸 쿠키 조각 개수 저장
        # 유저의 현제 덱 저장
        self.userCurrentDeck = ["용감한 쿠키", "딸기맛 쿠키", "마법사맛 쿠키", "닌자맛 쿠키", "근육맛 쿠키"]
        self.userCombatPower = 5000                      # 유저의 전투력 저장

        # 쿠폰 코드 저장 (리스트 형태로 보상이 저장 [골드, 다이아몬드, 쿠키틀, 쿠키 조각])
        self.couponCode = {"암소의 과학 공부": [10000, 3000, 100, 100], "암소의 포트폴리오": [3000, 4500, 125, 200]}

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

        cnt = 1
        for key in self.userOwnCookieNameToLevel.keys():
            if cnt % 5 == 0:
                print()

            cnt += 1

            print(f"[ {key} ]", end='')
            if cnt < len(self.userOwnCookieNameToLevel):
                print(", ", end='')
        
        print()

        print("상호작용 할려면 이름으로 접근하세요.")
        
        print("-" * 50)
    
    # 뽑기 최적화
    def cookieByLot(self):
        chosenResult = random.randint(1, 100)

        additionalCombatPower = 0

        if chosenResult <= 50:
            appendCookie = commonCookiesList[random.randint(0, len(commonCookiesList) - 1)]

            additionalCombatPower = 1000

            if appendCookie in self.userOwnCookieNameToLevel.keys():
                print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                print("쿠키 조각 5개\n")
                self.cookiePiece += 5

        elif chosenResult <= 75:
            appendCookie = rareCookiesList[random.randint(0, len(rareCookiesList) - 1)]

            additionalCombatPower = 2000

            if appendCookie in self.userOwnCookieNameToLevel.keys():
                print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                print("쿠키 조각 10개\n")
                self.cookiePiece += 10

        elif chosenResult <= 85:
            appendCookie = epicCookiesList[random.randint(0, len(epicCookiesList) - 1)]
            
            additionalCombatPower = 2500

            if appendCookie in self.userOwnCookieNameToLevel.keys():
                print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                print("쿠키 조각 25개\n")
                self.cookiePiece += 25
        
        elif chosenResult <= 91:
            appendCookie = legendaryCookiesList[random.randint(0, len(legendaryCookiesList) - 1)]

            additionalCombatPower = 3000

            if appendCookie in self.userOwnCookieNameToLevel.keys():
                print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                print("쿠키 조각 75개\n")
                self.cookiePiece += 75
        
        elif chosenResult <= 99:
            appendCookie = ancientCookiesList[random.randint(0, len(ancientCookiesList) - 1)]

            additionalCombatPower = 3500

            if appendCookie in self.userOwnCookieNameToLevel.keys():
                print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                print("쿠키 조각 50개\n")
                self.cookiePiece += 50
        
        else:
            appendCookie = beastCookiesList[random.randint(0, len(beastCookiesList) - 1)]

            additionalCombatPower = 4000

            if appendCookie in self.userOwnCookieNameToLevel.keys():
                print("이미 있는 쿠키가 나와서 아래 보상으로 대체됩니다.")
                print("쿠키 조각 100개\n")
                self.cookiePiece += 100
        
        if appendCookie not in allCookiesInfo.keys():
            print("-" * 50)
            print(f"얻은 쿠키: {appendCookie}")
            print("-" * 50)
            time.sleep(3)

            self.userOwnCookieNameToLevel[appendCookie] = 1
            self.userOwnCookieNameToCombatPower[appendCookie] = additionalCombatPower
            print("\n\n\n\n\n\n\n\n\n\n")
    
    # 쿠키틀 뽑기 최적화
    def cookieFrameByLotInner(self):
        if self.frame >= 1:
            self.frame -= 1
            self.cookieByLot()
            return
            
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
            self.userDiamond -= 300
            self.cookieByLot()
            return

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
    
    # 강화 조건 최적화
    def cookieStrengthenInner(self, usingCookie, currentLevel):
        requiredCookiePiece = 0

        additionalCombatPower = 0
        
        if currentLevel <= 10:
            requiredCookiePiece = 1
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie] * 0.25)
        elif currentLevel <= 20:
            requiredCookiePiece = 3
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie] * 0.55)
        elif currentLevel <= 30:
            requiredCookiePiece = 5
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie] * 0.75)
        elif currentLevel <= 40:
            requiredCookiePiece = 10
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie] * 0.9)
        elif currentLevel <= 50:
            requiredCookiePiece = 15
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie])
        elif currentLevel <= 60:
            requiredCookiePiece = 20
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie] * 1.15)
        elif currentLevel <= 70:
            requiredCookiePiece = 45
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie] * 1.25)
        elif currentLevel <= 80:
            requiredCookiePiece = 65
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie] * 1.5)
        elif currentLevel < 90:
            requiredCookiePiece = 85
            additionalCombatPower = int(self.userOwnCookieNameToCombatPower[usingCookie] * 2)
        else:
            print("이미 최대 레벨입니다.")
            time.sleep(2)

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return

        if self.cookiePiece >= requiredCookiePiece:
            self.userOwnCookieNameToLevel[usingCookie] += 1
            self.cookiePiece -= requiredCookiePiece
            self.userOwnCookieNameToCombatPower[usingCookie] += additionalCombatPower

            print("강화완료")
            print(f"{usingCookie}의 레벨: {self.userOwnCookieNameToLevel[usingCookie]} lv")
            time.sleep(2)

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return
        else:
            print("쿠키조각이 부족합니다.")
            time.sleep(2)

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return
    
    # 쿠키 강화
    def cookieStrengthen(self, usingCookie):
        while True:

            print("-" * 50)
            print(f"{usingCookie}의 레벨: {self.userOwnCookieNameToLevel[usingCookie]} lv")
            print("-" * 50)

            print()

            print("-" * 50)
            print("2-10 lv: 1개, 11-20 lv: 3개, 21-30 lv: 5개")
            print("31-40 lv: 10개, 41-50 lv: 15개, 51-60 lv: 20개")
            print("61-70 lv: 40개, 71-80 lv: 65개, 81-90 lv: 85개")
            print("-" * 50)

            print("\n\n")

            print(" [ 쿠키 강화 ] ")
            userInput = input(f"{usingCookie}를 강화하시겠습니까? (y/n): ")
            
            # 게임 종료
            if userInput == '-1':
                print("게임 종료")
                exit()
            # 돌아가기
            if userInput == '0':
                print("\n\n\n\n\n\n\n\n\n\n\n")
                return

            if userInput == 'y':
                self.cookieStrengthenInner(usingCookie, self.userOwnCookieNameToLevel[usingCookie])
            elif userInput == 'n':
                print("\n\n\n\n\n\n\n\n\n")
                return
            else:
                print("올바른 값을 입력하세요")
                time.sleep(2)

                print("\n\n\n\n\n\n\n")
                continue

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
        print(" [ 개발자 지원하기 ]")
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
        print("2. 내 덱 보기")
        print("3. 왕국 꾸미기")
        print("-" * 50)

        print("\n\n\n")

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
                                self.cookiePiece += self.couponCode[userInputCode][3]

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
            if interactCookie in self.userOwnCookieNameToLevel.keys():
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
                # 종료하기
                if userInput == -1:
                    print("게임 종료")
                    exit()
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
                    del self.userOwnCookieNameToLevel[interactCookie]
                    print(f"{interactCookie} 삭제 완료")
                    time.sleep(1)
                    print("\n\n\n")
                    return
                # 해당 쿠키 강화
                if userInput == 3:
                    print("\n\n\n\n\n\n\n\n\n\n")
                    self.cookieStrengthen(interactCookie)
                    return
                else:
                    print("올바른 번호를 입력해주세요.")
                    continue
    
    # 내 전투력 보기
    def getUserDeckTotalCombatPower(self):
        print("[ 내 덱 ]")
        print("-" * 50)
        print(f"현재 덱 전투력: {self.userCombatPower}")
        print("-" * 50)

        time.sleep(3)

        print("\n\n\n\n\n\n\n\n\n")
        return
    
    # 내 덱 변경
    def changeUserDeck(self):
        print("[ 내 덱 ]")
        print("-" * 50)
        cnt = 1
        for key in self.userOwnCookieNameToLevel.keys():
            if key not in self.userDeck:
                if cnt % 5 == 0:
                    print()

                cnt += 1
                
                print(f"[ {key} ]", end='')
                if cnt < len(self.userOwnCookieNameToLevel):
                    print(", ", end='')
        
        print()

        print("상호작용 할려면 이름으로 접근하세요.")
        
        print("-" * 50)
        print("-" * 50)

        time.sleep(3)

        print("\n\n\n\n\n\n\n\n\n")
        return

    # 내 덱
    def userDeck(self):
        while True:
            print("[ 내 덱 ]")
            
            print("-" * 50)
            for cookieIndex in range(5):
                print(f"{self.userCurrentDeck[cookieIndex]}", end='')

                if cookieIndex + 1 < 5:
                    print(", ", end='')
                else:
                    print()
            print("-" * 50)

            print()

            print("-" * 50)
            print("1. 전투력 확인")
            print("2. 내 덱 변경")
            print("-" * 50)

            print("\n")

            try:
                userInput = int(input("단축키를 입력하세요(숫자만 가능): "))
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            else:
                print("\n\n\n")
                # 종료하기
                if userInput == -1:
                    print("게임 종료")
                    exit()
                # 돌아가기
                if userInput == 0:
                    return
                # 전투력 확인
                if userInput == 1:
                    self.getUserDeckTotalCombatPower()
                    return
                # 덱 교체
                if userInput == 2:
                    self.changeUserDeck()
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
                    # 내 덱
                    if userInput == 2:
                        self.userDeck()
                        return
                    # 왕국 꾸미기
                    if userInput == 3:
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
print("""다양한 쿠키를 수집하고 육성해 전투를 펼치며, 나만의 왕국을 건설하는 전략 RPG입니다.
실시간 자동 전투와 PvP, 보스전 등 다채로운 전투 콘텐츠가 기다리고 있습니다.
자원을 모아 왕국을 성장시키고, 개성 넘치는 꾸미기로 나만의 세상을 만들어보세요.
매일 새로워지는 이벤트와 스토리로 끝없는 재미를 즐기실 수 있습니다.""")

print("-" * 50 + '\n')

callingVar = CookieRunKingdom()
callingVar.playCookieRunKingdom()