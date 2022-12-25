from itertools import count
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

###########################################################################


username = "" # حط رقمك الجامعي
password = "" # حط باسووردك

# CourseID ==== حط الرقم الخاص بالمادة (الايدي اللي بالرابط لما تخش على صفحتها فالبلاك بورد)
# (course ID)راح انزل تحديث للـ
# StartTime ===== حط متى يبدأ كلاسك ( بنظام ال24 ساعة)
# EndTime ===== حط متى ينتهي كلاسك ( بنظام ال24 ساعة)

#### ملاحظة : حط اللي تبي بين علامات التنصيص غير كذا ما بيضبط ####
#### ملاحظة : الوقت و الرقم حق المادة لازم نفس الصيغة اللي مكتوب فيه الرقم الحين ####

dict = {
    "course_1" : {"CourseID" : "_441676_1" , "StartTime" : "11:00", "EndTime" : "12:40"} ,
    "course_2" : {"CourseID" : "_427863_1" , "StartTime" : "20:53", "EndTime" : "21:50"} ,
    "course_3" : {"CourseID" : "" , "Time" : ""} ,
    "course_4" : {"CourseID" : "" , "Time" : ""} ,
    "course_5" : {"CourseID" : "" , "Time" : ""} ,
}

arr = {
"course_1" : {"CourseID" : "_441676_1" , "StartTime" : "11:00", "EndTime" : "12:40"} ,
}
e=0
file = open("courses.txt","r", encoding='utf-8')
for info in file:
    if info != "please write your course informations as follows :":
        continue
    e = info.split(",")
    arre = e + arr



print(arre)
print(e)




###########################################################################
## CODE >>>>> 





#
# boo = True
# while boo:
#     endpoint = requests.get("http://worldtimeapi.org/api/timezone/Asia/Riyadh")
#     curTime = endpoint.json()["datetime"]
#     curTime = curTime[curTime.index("T")+1:curTime.index("T")+6]
#     hourr = int(curTime[:2])
#     minn = int(curTime[3:])
#
#     ID = ""
#     for key in dict.values():
#         for value in key.values():
#             if value.find(":") != -1 :
#
#                 hour = int(value[:2])
#                 min =  int(value[3:])
#                 if hour == hourr and min ==minn:
#                     options = Options()
#                     # options.headless=True
#                     driver = webdriver.Chrome(service=Service(executable_path="C:\webdrivers\chromedriver.exe"), options=options)
#                     driver.get("https://lms.kau.edu.sa/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_101_1")
#                     time.sleep(1)
#
#                     #### BlackBoard login page URL ####
#                     loginUrl = "https://iam.kau.edu.sa/oamsso-bin/kaulogin-fed.pl?contextType=external&username=string&OverrideRetryLimit=0&password=secure_string&challenge_url=%2Foamsso-bin%2Fkaulogin-fed.pl&request_id=865223081718835052&authn_try_count=0&locale=ar&resource_url=%252Fuser%252Floginsso"
#                     loginUrlIndex = loginUrl.index("&request_id=")
#                     loginUrl = loginUrl[:loginUrl.index("&request_id=")]
#
#                     #### check if it is login page = ####
#                     if driver.current_url[:loginUrlIndex] == loginUrl:
#                         userId = driver.find_element_by_name("userid")
#                         userId.clear
#                         userId.send_keys(username)
#
#                         passw = driver.find_element_by_name("password")
#                         passw.clear
#                         passw.send_keys(password)
#
#                         driver.find_element_by_class_name("c-btn").click()
#                         time.sleep(3)
#
#                         driver.get("https://lms.kau.edu.sa/webapps/collab-ultra/tool/collabultra?course_id="+ID+"&mode=view")
#
#                         s1 = value
#                         s2 = key["EndTime"]
#                         td = datetime.strptime(s2, '%H:%M') - datetime.strptime(s1, '%H:%M')
#                         td = str(td)
#                         date_time = datetime.strptime(td, "%H:%M:%S")
#                         a_ = date_time - datetime(1900, 1, 1)
#                         seconds = a_.total_seconds()
#                         print(seconds/60) # test the difference in time between classes
#                         time.sleep(seconds)
#
#                         boo = False ################# figure the latest class
#
#
#
#
#             elif value.find("_") != -1 and value.isidentifier():
#                 ID = value
#
#
#
#
#

