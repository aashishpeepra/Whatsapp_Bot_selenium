# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:27:23 2018

@author: hp
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options
option=Options()
option.add_argument('user-data-dir=selenium')
print("WHATSAPP-JARVIS by AASHISH PEEPRA!!")
print("ENTER ANY KEY TO CONTINUE")
input("")

driver=webdriver.Chrome(chrome_options=option)
driver.get("https://web.whatsapp.com/")
input("After Scanning press any key to continue")
##ELEMENT CHATHEAD
def name_input():
    ##take name input
    user_name=input("WHOM DO YOU WANT TO SEND MESSAGE")
    # //*[@id="side"]/div[1]/div/label/div/div[2]
    chatInput=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    chatInput.click()
    chatInput.send_keys(user_name)
    ##pane-side > div:nth-child(1) > div > div > div:nth-child(4) > div > div > div._2kHpK > div._3dtfX > div._3CneP > div > span > span
    # //*[@id="pane-side"]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div[1]/span/span
    # elems= driver.find_element_by_class_name('matched-text _3Whw5')
    # child=driver.find_element_by_css_selector("span.matched-text")
    # child.click
    # child=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]')
    child = driver.find_elements_by_class_name('matched-text')
    print(child)
    print("Select by entering the index")
    if len(child)==0:
        print("No match found! Try again")
        name_input()
    for i in range(len(child)):
        print(str(i+1)+".",child[i].text)
    index=int(input("Enter Inidex : "))
    if index >=1 and index<=len(child):
        child[index-1].click() 
    else:
        print("Wrong Index Selected Try again")
        name_input()
    # print(elems)
    # elems.click()
    # chat.click()

##TEXT LANE
def texter():
    lane=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    i=1
    ranger=int(input("Enter how many times to send a message"))
    typo=input("Enter the message to send")
    while i<=ranger:
        lane.send_keys(typo)
        lane.send_keys(Keys.RETURN)
        i=i+1

def reader():
    args=driver.find_element_by_class_name('selectable-text invisible-space copyable-text')
    print(args.text)
## profile clicker
def profile_click():
    dp_click=driver.find_element_by_xpath('//*[@id="main"]/header/div[1]')
    dp_click()
##lasttext
def last_text():
    elem=driver.find_element_by_xpath('//*[@id="main"]//div[contains(@class, "message")]')
    print(elem.text)
##ATTACHMENT
def attachment():
    button_a=driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div')
    button_a.click()
##clicks on your own profile pic
def profile_self():
    try:
        dp_click=driver.find_element_by_xpath('//img[@class="Qgzj8 gqwaM"]')
        dp_click.click()
        actual_exe()
    except:
        print("ERROR IN PROFILE-SELF")
        actual_exe()
##-------------------------------------------------------------------------------Qgzj8 gqwaM
def status():
    profile_self()
    status_point=driver.find_elements_by_css_selector('div._2S1VP.copyable-text.selectable-text')
    status_point.textContent()
def status2():
    profile_self()
    status_elem=driver.find_element_by_xpath('//*[@class="IuYNx"]')
    status_elem.click()

def last_text1():
    lst=driver.find_element_by_css_selector('span.selectable-text.invisible-space.copyable-text')
    print(lst.text)
    timeview=driver.find_element_by_xpath('//span[@class="_3EFt_"]')
    print(timeview.text)


##FORMAT CHECKER  
def format_checker(str):
    try:
        errr=int(input(str))
        return errr
    except:
        print("USE INTEGER FORMAT INPUT")
        format_checker(str)
##FORWORDER
def forwarder():
    namelist=[]
    choicer=0
    iol=0
    while choicer!=1:
        namer=input("Enter the name of person:%d"%(iol))
        namelist.append(namer)
        iol+=1
        choicer=format_checker("press 1 to exit, press any other key to continue adding list")
    print("contacts name are :")
    def list_print():
            for x in range(iol):
                print("%d namelist[%d]"%(x,x))
    def ex_forwarder():
        c_1=format_checker("Press 1 to add more contact || press 2 to delete some contacts || press 3 to continue")
        if c_1==1:           
            namer_r=input("Enter the name of person")
            namelist.append(namer_r)
        elif c_1==2:
            print("CURRENT LIST IS:")
            list_print()
            namer_t=input("Enter the Name of the person to remove!! please be accurate")
            kr=0
            for y in range(iol):
                if namelist[y]==namer_t:
                    namelist.remove(namer_t)
                    kr=1
            if kr==0:
                print("NO such contact found recalling")
                ex_forwarder()
            else:
                execute_forwarder()
        elif c_1==3:
            execute_forwarder()
        else:
            print("woops!! wrong choice recalling")
            ex_forwarder()
    def execute_forwarder():
        izr=format_checker("how many times do u want to send message")
        izr_text=input("Enter the message")
        for xoz in range(iol):
            use_this=namelist[xoz]
            opener=driver.find_element_by_xpath('//span[text()="%s"]'%(use_this))
            opener.click()
            lane_rn=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            izp=0
            while izp!=izr:
                try:
                    lane_rn.send_keys(izr_text)
                    lane_rn.send_keys(Keys.RETURN)
                    izp+=1
                except:
                    print("ERROR IN MULTIFORWARDER")
                    actual_exe()
        actual_exe()
    list_print()
    ex_forwarder()
##---------------------------------------------------------------
##Actual starts here
def multiple_sender():
    try:
        choice=0
        while choice!=1:
            name_input()
            texter()
            choice=format_checker("press 1 to exit")
            if choice==1:
                actual_exe()
    except Exception as e:
        print(e)
        print("error in multiple sender")
        print("RECALLING")
        multiple_sender()
##-------------------------------------------------------------------------------------
def actual_exe():
        print("PRESS 1 FOR MULTIPLE SENDER || PRESS 2 FOR FORWARDER || PRESS 3 TO VIEW YOUR OWN PIC || PRESS 4 TO STATUS || PRESS 5 TO EXIT")
        c_4=format_checker(" ")
        if c_4==1:
            multiple_sender()
        elif c_4==2:
            forwarder()
        elif c_4==3:
            profile_self()
        elif c_4==4:
            status2()
        elif c_4==5: 
            print("----THANKS FOR USING WEBJARVIS BY AASHISH-----")
        else:
            print("woops!! wrong input")
            print("RECALLING")
            last_text()
            actual_exe()
actual_exe()
##-----------------------------------------------------------------------------------
