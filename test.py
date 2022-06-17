from selenium import webdriver
import unittest

## 실습1. 기능 테스트(FT). 파이어폭스 브라우저를 실행하고 웹페이즐ㄹ 연 다음 타이틀에서 Django 문구가 있는지 확인
# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
# assert 'Django' in browser.title


## 실습2. AssertionError 문구를 수정하기 위한 코드
# 1. TestCase를 상속하여 테스트를 클래스 형태로 만든다.
class NewVisitorTest(unittest.TestCase):

    # 2,3. 테스트 시작 전, 후에 실행되며 try/except와 비슷하고 브라우저를 시작(setUp)하고 닫을(tearDown) 수 있음
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="/Users/hailey/Downloads/geckodriver")
        # 8. 암묵적 대기 -> 페이지 로딩이 끝난 뒤 실행되도록 해줌(셀레니움 테스트에서 기본적인 로직)
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    # 4. 메인코드 ->test로 시작하면 테스트 메소드이며, 테스트 실행자에 의해 실행된다. 클래스당 하나 이상의 테스트 메소드 작성 가능, 이름을 알아보기 쉽게 짓자.
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # 5. 테스트 어설션(개발시에 디버깅을 해주면서 프로그램 배포시에는 컴파일 되지 않게 할 수 있는 코드)
        # 여기서는 assertIn을 만들었다.
        self.assertIn('To-Do', self.browser.title)
        # 6. 테스트 실패를 발생시키고 에러 메세지를 출력한다.
        self.fail('Finish the test!')


# 7. 실행부분, 다른 스크립트에 임포트 된 것이 아니라 자체 실행된 것을 확인해주는 코드
# 자동으로 unittest.main을 호출해서 unittest 테스트 실행자를 가동한다.
if __name__ == '__main__':
    unittest.main(warnings='ignore')