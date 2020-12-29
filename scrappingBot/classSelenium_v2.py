# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
#help(webdriver)
#https://selenium-python.readthedocs.io/

class SiteSelenium:
    def __init__(self):
        self.driver=webdriver.Chrome(r'C:\python\chromedriver_win32\chromedriver')

    def openingMainPage(self,site):
        self.driver.get(site)
        
    def credentials(self):
    # =============================================================================
    # Detecting the user name and password fields, fill them and hitting the enter
    # button to access the website initial page
    # =============================================================================
        self.usrnm=self.driver.find_element_by_id('frm2:nomeUsuario')
        self.pswrd=self.driver.find_element_by_id('frm2:senha')
        self.usrnm.send_keys('chmendonca')
        self.pswrd.send_keys('grudinho')
        self.driver.find_element_by_id('frm2:btLogar').click()
    # =============================================================================
    # Returning the driver    
    # =============================================================================
#        return self.driver

    def findElement(self,findByClassName='',findById='',findByLinkText='',findByText='',findByXPath='',by=''):
            if findByClassName==True:
                self.element=self.driver.find_elements_by_class_name(by)[0].text
            elif findById==True:
                self.element=self.driver.find_element_by_id(by)
            elif findByLinkText==True:
                #(no longer used) driver.execute_script("if(typeof jsfcljs == 'function'){jsfcljs(document.getElementById('frm1'),{'frm1:j_id1913':'frm1:j_id1913','idMenu':'4'},'');}return false")
                #link = driver.find_element_by_link_text('Faturas')
                self.element=self.driver.find_element_by_link_text(by)
            elif findByText==True:
                self.element=self.driver.find_element_by_text(by)
            elif findByXPath == True:
                self.element = self.driver.find_element_by_xpath(by)
                
            element=self.element
            return element
        
    #def buttonClick(self,button):
  #      def pressButton(driver,button):
       # filterButton=driver.find_elements_by_id(button)[0]
      #  filterButton.click()
     #   time.sleep(5)
    
    def clickingOnLink(self,delayAfterClick=3):
    # =============================================================================
    # This function simulates a click
    # It receives the means to identify the link and the link. Set the means as
    # 'True' to the logic to understand the command. Independently of the mean
    # the path is always called as link
    # =============================================================================
        self.element.click()
        time.sleep(float(delayAfterClick))
    
    def selectDropDown(self):
    # =============================================================================
    # This function selects a dropdown windown
    # It receives the means to identify the dropdown and returns a list of elements.
    # For this case, only the first elment of the dropdown is returned
    # =============================================================================
        #self.selectedOption = Select(driver.find_elements_by_id('frm2:faturas')[0])
        self.selectedOption = Select(self.element)
            
    def selectingOnDropDown(self,selectByText='',link=''):
    # =============================================================================
    # This function selects the dropdown information based on text
    # It receives from the calling scripg the text (link) that will be selected on
    #  the windown and sets the value to appear on the screen.
    # Important: this function is used following the "selectDropDown", otherwise an
    # error will be set and it is not handled by this script      
    # =============================================================================
        if selectByText==True:
            self.selectedOption.select_by_visible_text(link)

    def getFirstSelectedTextOnDropDown(self,attributeType=''):
    # =============================================================================
    # This function gets the first selected option based on attribute (ex. 1. for 'CC' the attribute is
    # text; 2. for 'cartola' the attribute is 'value')
    # The first selected option in this select tag (or the currently selected option in a normal select)
    # Obs.: other option to get the text 'text=selectedOption.first_selected_option.text'
    # =============================================================================
        #self.firstSel=self.selectedOption.first_selected_option.get_attribute('text')
        return self.selectedOption.first_selected_option.get_attribute(attributeType)

    def getPageContents(self):
    # =============================================================================
    # This function gets the first selected option based on attribute (ex. text)
    # =============================================================================
        return self.driver.page_source

# =============================================================================
# Moving between tables
# =============================================================================
    def switchingPages(self,page):
        # print('calling next page:%s' %page)
#    driver.execute_script("__doPostBack('ctl00$cphMainContent$gvList','Page${}')".format(page))
#    first attempt
#    pg=self.driver.execute_script(""" return document.querySelector('[onclick*="Page$2"]')""")
#    returned None
#    second attempt
        pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$%s"]')""" %page)
#        if page==2:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$2"]')""")
#        if page==3:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$3"]')""")
#        if page==4:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$4"]')""")
#        if page==5:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$5"]')""")
#        if page==6:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$6"]')""")
#        if page==7:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$7"]')""")
#        if page==8:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$8"]')""")
#        if page==9:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$9"]')""")
#        if page==10:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$10"]')""")
#        if page==11:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$11"]')""")
#        if page==12:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$12"]')""")
#        if page==13:
#            pg=self.driver.execute_script(""" return document.querySelector('[href*="Page$13"]')""")
#        print(pg)
        pg.click()
    #print('waiting a few seconds to have time to upload the page on Chrome')
        time.sleep(20)

#    https://stackoverflow.com/questions/53848923/selenium-webdriver-stop-loading-when-switching-pages

    def closingDriver(self):
        time.sleep(3)
        self.driver.close()
#    
#if __name__=='__main__':
#    main()
    
#teste=SiteSelenium()
#teste.openingMainPage()
#teste.clickingOnLink(findByLinkText=True,link='Faturas')
#teste.selectDropDown(findById=True,link='frm2:faturas')
#teste.getFirstSelectedTextOnDropDown(attributeType='text')
#teste.closingDriver()