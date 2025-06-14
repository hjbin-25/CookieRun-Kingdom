import random
import time

# 쿠키 정보 저장
allCookiesInfo = {}

# 시나리오 저장
allScenario = {}

# 쿠키 저장

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

    # 보스전 부분 담당
    def bossBattke(self):
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
# 설명

callingVar = CookieRunKingdom()
callingVar.playCookieRunKingdom()