from Page.BasePage import BasePage

class MemberPage(BasePage):
    url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    def addMember(self,name,account,phone):
        #点击【添加成员】
        self.driver.find_element_by_xpath('//*[@id="js_contacts41"]/div/div[2]/div/div[2]/div[3]/div[9]/a[1]').click()
        #姓名输入name
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(name)
        #账号输入account
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys(account)
        #手机输入phone
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys(phone)
        #点击【保存】按钮
        self.driver.find_element_by_xpath('//*[@id="js_contacts41"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()


