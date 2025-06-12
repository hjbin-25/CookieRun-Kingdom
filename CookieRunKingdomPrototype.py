import random
import time

# 쿠키 정보 저장
allCookiesInfo = {}

# 시나리오 저장
allScenario = {}

# 희귀도가 일반인 쿠키들
commonCookiesList = ["용감한 쿠키", "딸기맛 쿠키", "마법사맛 쿠키", "닌자맛 쿠키", "근육맛 쿠키"]
# 희귀도가 희귀인 쿠키들
rareCookiesList = ["클로버맛 쿠키", "커스터드 3세맛 쿠키"]
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

        # 다양한 변수들

        print("-" * 50)
        print("[ 종료버튼: -1 ]")
        print("-" * 50)



    # 가이드북 부분

    # 설정 부분 가이드북
    def getSettingGuideBook(self):
        pass

    # 상점 부분 가이드북
    def getStoreGuideBook(self):
        pass
    
    # 플레이 부분 가이드북
    def getPlayGuideBook(self):
        pass

    # 왕국 부분 가이드북
    def getKingdomGuideBook(self):
        pass

    # 내 쿠키 부분 가이드북
    def getMyCookiesGuideBook(self):
        pass

    # 기본 가이드북
    def getMethodGuideBook(self):
        pass



    # 설정 구현

    # 닉네임 변경
    def setUserNickName(self):
        pass
    
    # 닉네임 출력
    def getUserNickName(self):
        pass

    # 설정 부분 담당
    def setting(self):
        pass



    # 상점 부분
    
    # 뽑기 최적화
    def cookieByLot(self):
        pass
    
    # 쿠키틀 뽑기 최적화
    def cookieFrameByLotInner(self):
        pass

    # 쿠키틀 뽑기
    def cookieFrameByLot(self):
        pass

    # 다이아몬드 뽑기 최적화
    def diamondByLotInner(self):
        pass

    # 다이아몬드 뽑기
    def diamondByLot(self):
        pass

    # 유저 재화 출력
    def getUserGoods(self):
        pass
    
    # 개발자 지원하기
    def supportDeveloper(self):
        pass
    
    # 상점 부분 담당
    def store(self):
        pass



    # 플레이 부분
    
    # 시나리오 부분 담당
    def scenario(self):
        pass

    # 플레이 부분 담당
    def play(self):
        pass



    # 왕국 부분
    
    # 보유중인 쿠키 출력
    def getCurrentOwnCookies(self):
        pass

    # 쿠키 확인 부분 담당
    def currentCookies(self):
        pass
    
    # 강화 조건 최적화
    def cookieStrengthenInner(self, usingCookie, currentLevel):
        pass
    
    # 쿠키 강화
    def cookieStrengthen(self, usingCookie):
        pass

    # 내 전투력 보기
    def getUserDeckTotalCombatPower(self):
        pass
    
    # 내 덱 출력
    def getUserCurrentDeck(self):
        pass
    
    # 내 덱 변경
    def changeUserDeck(self):
        pass

    # 내 덱
    def userDeck(self):
        pass

    # 왕국 부분 담당
    def kingdom(self):
        pass



    # 메인 플레이

    # 메인 플레이를 진행할 플레이 함수
    def playCookieRunKingdom(self):
        pass


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