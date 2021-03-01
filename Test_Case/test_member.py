from time import sleep

from Page.MemberPage import MemberPage


class TestLogin:
    def teardown(self):
        self.member.close()

    def test_addMember(self):
        self.member = MemberPage()
        sleep(3)
        self.member.addMember("test","123456",'13424405193')
        sleep(3)
        self.member.close()
