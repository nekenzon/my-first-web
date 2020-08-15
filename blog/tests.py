# -*- coding:utf-8 -*-
__version__ = '1.0.0.0'
from selenium import webdriver
import unittest
from django.test import TestCase
from django.test import Client
from bs4 import BeautifulSoup
from .models import Graduation, Experience
from selenium.webdriver.common.keys import Keys
import time

class Myunittest(TestCase):

    def setUp(self):
        response = self.client.get('/cv')
        self.assertEqual(response.status_code, 200)
        self.bs = BeautifulSoup(response.content.decode(), "html.parser")

    def test_tr2(self):
        temp = self.bs.select("table > tr ")[2].select("td")[0]
        self.assertEqual("Name", temp.text)
        temp = self.bs.select("table > tr ")[2].select("td")[1]
        self.assertEqual("QIHONGLIANG", temp.text)
        temp = self.bs.select("table > tr ")[2].select("td")[2]
        self.assertEqual("Sex", temp.text)
        temp = self.bs.select("table > tr ")[2].select("td")[3]
        self.assertEqual("Male", temp.text)
        temp = self.bs.select("table > tr ")[2].select("td")[4]
        self.assertEqual("Nation", temp.text)
        temp = self.bs.select("table > tr ")[2].select("td")[5]
        self.assertEqual("Chinese", temp.text)

    def test_tr3(self):
        temp = self.bs.select("table > tr ")[3].select("td")[0]
        self.assertEqual("Date-Of-Birth", temp.text)
        temp = self.bs.select("table > tr ")[3].select("td")[1]
        self.assertEqual("1998-11-29", temp.text)
        temp = self.bs.select("table > tr ")[3].select("td")[2]
        self.assertEqual("Religion", temp.text)
        temp = self.bs.select("table > tr ")[3].select("td")[3]
        self.assertEqual("No-Religion", temp.text)
        temp = self.bs.select("table > tr ")[3].select("td")[4]
        self.assertEqual("Marriage", temp.text)
        temp = self.bs.select("table > tr ")[3].select("td")[5]
        self.assertEqual("Married", temp.text)

    def test_tr4(self):
        temp = self.bs.select("table > tr ")[4].select("td")[0]
        self.assertEqual("Hometown", temp.text)
        temp = self.bs.select("table > tr ")[4].select("td")[1]
        self.assertEqual("GuangDong", temp.text)
        temp = self.bs.select("table > tr ")[4].select("td")[2]
        self.assertEqual("Current-address", temp.text)
        temp = self.bs.select("table > tr ")[4].select("td")[3]
        self.assertEqual("Birmingham", temp.text)
        temp = self.bs.select("table > tr ")[4].select("td")[4]
        self.assertEqual("Education", temp.text)
        temp = self.bs.select("table > tr ")[4].select("td")[5]
        self.assertEqual("Undergraduate", temp.text)

    def test_tr5(self):
        temp = self.bs.select("table > tr ")[5].select("td")[0]
        self.assertEqual("Graduated-school", temp.text)
        temp = self.bs.select("table > tr ")[5].select("td")[1]
        self.assertEqual("University-Of-Birmingham", temp.text)
        temp = self.bs.select("table > tr ")[5].select("td")[2]
        self.assertEqual("Major", temp.text)
        temp = self.bs.select("table > tr ")[5].select("td")[3]
        self.assertEqual("Meng-SoftwareEnginnering/Computer-Science", temp.text)

    def test_tr6(self):
        temp = self.bs.select("table > tr ")[6].select("td")[0]
        self.assertEqual("Email", temp.text)
        temp = self.bs.select("table > tr ")[6].select("td")[1]
        self.assertEqual("nekenzon@gmail.com/qxl749@student.bham.ac.uk", temp.text)
        temp = self.bs.select("table > tr ")[6].select("td")[2]
        self.assertEqual("Contacted-Number", temp.text)
        temp = self.bs.select("table > tr ")[6].select("td")[3]
        self.assertEqual("07465644363", temp.text)

    def test_experience_model(self):
        experience_list = Experience.objects.all()
        temp_list = self.bs.select("table > tr.experience ")
        for index,item in enumerate(temp_list):
            td_list = item.select("td")
            self.assertEqual(experience_list[index].start_time, td_list[0].text)
            self.assertEqual(experience_list[index].company, td_list[1].text)
            self.assertEqual(experience_list[index].work_content, td_list[2].text)

    def test_graduation_model(self):
        graduation_list = Graduation.objects.all()
        temp_list = self.bs.select("table > tr.graduation ")
        for index, item in enumerate(temp_list):
            td_list = item.select("td")
            self.assertEqual(graduation_list[index].start_time, td_list[0].text)
            self.assertEqual(graduation_list[index].school, td_list[1].text)
            self.assertEqual(graduation_list[index].professional, td_list[2].text)

    def test_aihao(self):
        temp = self.bs.select("table > tr.aihao ")[0].select("td")[0]
        self.assertEqual("Skill-And-Hobbit", temp.text)
        temp = self.bs.select("table > tr.aihao ")[0].select("td")[1]
        self.assertEqual("#Stay Up All night for programming #Test Open-Source Game or App #Develop Game", temp.text)

    def test_pingjia(self):
        temp = self.bs.select("table > tr.pingjia ")[0].select("td")[0]
        self.assertEqual("Self-Evaluation", temp.text)
        temp = self.bs.select("table > tr.pingjia ")[0].select("td")[1]
        self.assertEqual("Postive and love to social", temp.text)

    def test_cv(self):
        temp = self.bs.select("table > tr ")[0].select("td")[1]
        self.assertEqual("Django Web Designer", temp.text)
        temp = self.bs.select("table > tr ")[1].select("td")[0]
        self.assertEqual("Basic Information", temp.text)

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_get_to_the_url_correct(self):

        #functional testing
        self.browser.get('http://localhost:8000/cv')

        #Title testing
        self.assertIn('QIHONGLIANG BLOG', self.browser.title)

        #head element testing
        head = self.browser.find_element_by_tag_name('td').text
        self.assertEqual('Objective Job',head)





if __name__ == '__main__':
    unittest.main(warnings='ignore')
