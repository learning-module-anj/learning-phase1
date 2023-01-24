from Web.PageObjects.LoginPage import LoginPage
import time
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class TestLoginPage:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)

    def test_valid_login(self, specialSetUp):
        self.lp.enter_login_email("demo@supplysail.com")
        self.lp.click_on_next_button()
        self.lp.enter_login_password("demo1234")
        self.lp.click_on_next_button()
        result = self.lp.verify_home_page()
        assert result == True