# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 05:02:00 2019

@author: Cassio
"""

# import os
# from scalpl import Cut
import time

# import files
# import dicts2json as dicts
# import importing.classSelenium_v1 as cSel
# from jsonCommands_CC_v0 import *

#import importing.cartolaFcScoutsSource_ns2_v1 as source

from scrappingBot.classSelenium_v2 import SiteSelenium

class ScrappingOlx(SiteSelenium):
    def __init__(self):
        self.sSel = SiteSelenium()
        self.sSel.openingMainPage('https://www.olx.com.br/')

    def doing_nothing(self):
        print('\nEsperando o site carregar completamente\n')
        time.sleep(30)

    def openingState(self,selected_state):
        self.selected_state = selected_state
        self.sSel.findElement(self,findByXPath=True,by='//*[@id="___gatsby"]/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/a[' + str(selected_state) + ']')
        self.sSel.clickingOnLink()

    def openingRegion(self,selected_region):
        self.selected_region = selected_region
        # ['RJ','SP','MG','PR','RS','SC','ES','BA','PE','DF','CE','MS','GO','AM','RN','PB','PA','MT','AL','SE','MA','AC','RO','TO','PI','AP','RR','BRASIL']
        if self.selected_state in [1]:
            xpath = '//*[@id="column-main-content"]/div[2]/div/div[2]/div/div/div[' + str(selected_region) + ']/a'
            # //*[@id="column-main-content"]/div[2]/div/div[2]/div/div/div[2]/a

    def openingCategory(self,selected_category):
        self.selected_category = selected_category
        self.sSel.findElement(self,findByXPath=True,by='//*[@id="left-side-main-content"]/div[2]/div/div/div[2]/div/div/div[1]/div/div[' + str(selected_category) + ']/a')
        self.sSel.clickingOnLink()

        # //*[@id="column-main-content"]/div[2]/div/div[2]/div/div/div[1]/a
        # //*[@id="column-main-content"]/div[2]/div/div[2]/div/div/div[2]/a
        # //*[@id="column-main-content"]/div[2]/div/div[2]/div/div[1]/div/div/div/a

    def closing_connection(self):
        self.sSel.closingDriver()


        # //*[@id="left-side-main-content"]/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]/a
        # //*[@id="left-side-main-content"]/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]/a
        # //*[@id="left-side-main-content"]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/a
        # //*[@id="left-side-main-content"]/div[2]/div/div/div[2]/div/div/div[1]/div/div[13]/a

# def selChmpnshpYr(year):
#     return ''.join(['Campeonato Brasileiro ',year])

# def selChmpnshpRnd(rnd):
#     return ''.join([str(int(rnd)),'ª Rodada'])

# def allPlayers(yrRndCut):
#     cs=cSel.SiteSelenium()
#     for year in yrRndCut.keys():
#         source=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','scoutsAllPlayers_'+str(year)+'.json')
#         if not(files.checkingIfExistsFile(source)):
#             files.creatingFile(False,source)
#             cartola={str(year):{}}
#             with open(source,'w') as outfile:
#                 json.dump(cartola,outfile)
        
#         data=fileLoad(source)
#         scalplCut=Cut(data)
        
#         chmpnshpYr=selChmpnshpYr(year)
#         print(chmpnshpYr)
        
#         for rnd in yrRndCut[year]:
#             # print('rnd',rnd)
#             dicts.delGenericDict(scalplCut,[year,rnd])
            
#             chmpnshpRnd=selChmpnshpRnd(rnd)
#             print(chmpnshpRnd)
                    
#             cs.openingMainPage()
#             time.sleep(60)
#             cs.findElement(findById=True, by='ctl00_cphMainContent_drpCampeonatos') # selecting the field year
#             cs.selectDropDown()
#             time.sleep(30)
#             cs.selectingOnDropDown(selectByText=True,link=chmpnshpYr) #selecting the year
#             time.sleep(30)
#             cs.findElement(findById=True, by='ctl00_cphMainContent_drpRodadas') #selecting the field round
#             cs.selectDropDown()
#             if str(int(rnd))==cs.getFirstSelectedTextOnDropDown('value'): #this verification is necessary due to a page bug
#                 pass #indicates that the round have been selected by default and doesn't click on the button to round selection
#             else: #the round will be selected
#                 cs.selectingOnDropDown(selectByText=True,link=chmpnshpRnd) #selecting the round
#                 cs.findElement(findById=True, by='ctl00_cphMainContent_btnPesquisar') #selecting the button to move to selected year and round
#                 cs.clickingOnLink() #pressing the button to move to selected year and round
#             cs.findElement(findById=True,by='ctl00_cphMainContent_drpPageSize') #selecting the field number of players displayed per page
#             cs.selectDropDown()
#             cs.selectingOnDropDown(selectByText=True,link='100') #selecting a 100 players per page (maximum available)
#             cs.findElement(findById=True,by='ctl00_cphMainContent_drpStatus') #selecting the field status (to select 'ALL' instead 'Probable')
#             cs.selectDropDown()
#             cs.selectingOnDropDown(selectByText=True,link='[TODOS]') #selecting the option to download all players
#             cs.findElement(findById=True,by='ctl00_cphMainContent_btnFiltrar') #pressing the button to filter the number of players displayed per page and the players status
#             cs.clickingOnLink(5) #this time was added intentionally to ensure enough time to upload page
            
#             #get the number of tables with players
#             pages=cs.findElement(findByClassName=True,by='tbpaging')
#             print('pages:',pages)
#     #remove the space between the values in the answwer
#             pages=pages.split()
#     #print('pages:',pages)
#     #getting the last character as integer to have the number of pages
#             lastPage=int(pages[-1])
#     #print('number of pages (int):',lastPage)

# # =============================================================================
# # getting the source code of the players data page
# # =============================================================================
#             pageList=[]
#             for page in range(1,lastPage+1,1):
# #    for page in range(1,2,1): #used for test, downloads only two pages
#                 print ('downloading page',page)
#                 if page>1:
#                     cs.switchingPages(page)
#                 pageHtml=cs.getPageContents()
#                 pageList.append(pageHtml)
#         #creatingDf(yearRnd[1],page,pageHtml)
#         #wtJson.main(yearRnd,'source',pageHtml)
#                 time.sleep(3)  
#             cs.closingDriver()
            
#             dicts.wtGenericDict(source,scalplCut,[year,rnd],pageList)
            

# def probablePlayers(yrRndCut):
#     cs=cSel.SiteSelenium()
#     for year in yrRndCut.keys():
#         source=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','scoutsProbPlayers_'+str(year)+'.json')
#         if not(files.checkingIfExistsFile(source)):
#             files.creatingFile(False,source)
#             cartola={str(year):{}}
#             with open(source,'w') as outfile:
#                 json.dump(cartola,outfile)
# #        if not(files.checkingIfExistsFile(os.getcwd(),'data','scoutsProbPlayers_'+str(year)+'.json')):
# #            files.creatingFile(False,os.getcwd(),'data','scoutsProbPlayers_'+str(year)+'.json')
                
#         data=fileLoad(source)
#         scalplCut=Cut(data)
        
#         chmpnshpYr=selChmpnshpYr(year)
#         print(chmpnshpYr)
        
#         for rnd in yrRndCut[year]:
#             # print('rnd',rnd)
#             dicts.delGenericDict(scalplCut,[year,rnd])

            
#             chmpnshpRnd=selChmpnshpRnd(rnd)
#             print(chmpnshpRnd)
                    
#             cs.openingMainPage()
#             time.sleep(20)
#             cs.findElement(findById=True, by='ctl00_cphMainContent_drpCampeonatos') # selecting the field year
#             cs.selectDropDown()
#             cs.selectingOnDropDown(selectByText=True,link=chmpnshpYr) #selecting the year
#             cs.findElement(findById=True, by='ctl00_cphMainContent_drpRodadas') #selecting the field round
#             cs.selectDropDown()
#             if str(int(rnd))==cs.getFirstSelectedTextOnDropDown('value'): #this verification is necessary die to a page bug
#                 pass #indicates that the round have been selected by default and doesn't click on the button to round selection
#             else: #the round will be selected
#                 cs.selectingOnDropDown(selectByText=True,link=chmpnshpRnd) #selecting the round
#                 cs.findElement(findById=True, by='ctl00_cphMainContent_btnPesquisar') #selecting the button to move to selected year and round
#                 cs.clickingOnLink() #pressing the button to move to selected year and round
#             cs.findElement(findById=True,by='ctl00_cphMainContent_drpPageSize') #selecting the field number of players displayed per page
#             cs.selectDropDown()
#             cs.selectingOnDropDown(selectByText=True,link='100') #selecting a 100 players per page (maximum available)
#             cs.findElement(findById=True,by='ctl00_cphMainContent_btnFiltrar') #pressing the button to filter the number of players displayed per page and the players status
#             cs.clickingOnLink(10) #this time was added intentionally to ensure enough time to upload page. Otherwise an erroneous value of 50 players per page could be used
            
#             #get the number of tables with players
#             pages=cs.findElement(findByClassName=True,by='tbpaging')
#             print('pages:',pages)
#     #remove the space between the values in the answwer
#             pages=pages.split()
#     #print('pages:',pages)
#     #getting the last character as integer to have the number of pages
#             lastPage=int(pages[-1])
#     #print('number of pages (int):',lastPage)

# # =============================================================================
# # getting the source code of the players data page
# # =============================================================================
#             pageList=[]
#             for page in range(1,lastPage+1,1):
# #    for page in range(1,2,1): #used for test, downloads only two pages
#                 print ('downloading page',page)
#                 if page>1:
#                     cs.switchingPages(page)
#                 pageHtml=cs.getPageContents()
#                 pageList.append(pageHtml)
#         #creatingDf(yearRnd[1],page,pageHtml)
#         #wtJson.main(yearRnd,'source',pageHtml)
#                 time.sleep(3)
                
#             cs.closingDriver()
            
#             dicts.wtGenericDict(source,scalplCut,[str(year),str(rnd)],pageList)
            
# # =============================================================================
# # This file will be used to import single data (one round per time).
# # There is a call, not implemented yet, that will be left as provision for
# #     as many imports as required
# # =============================================================================
# def main(yrRnd):
#     print('\nCHOSE WHAT WILL BE IMPORTED')
#     print('Choose one option:')
#     print('"P" or "p" - probable players on round (default)')
#     print('"A" or "a" - all players on round')
#     action=input('Select: ')
    
#     yrRndCut=Cut(yrRnd) #transforming yrRnd dict in a scalplCut temp file

#     if action.upper()=='A':
#         allPlayers(yrRndCut)
#     else:
#         probablePlayers(yrRndCut) #default
    
# #    yrRndTemp=Cut(yrRnd)
# ##    print(yrRndTemp.keys())
# #    for year in yrRndTemp.keys():
# #        print('year',year)
# ##        print('values',yrRndTemp[year])
# #        for rnd in yrRndTemp[year]:
# #            print('rnd',rnd)

# ## =============================================================================
# ## This function will tabulate the data to transform the scrapped raw Data in a
# ##    tabulated format. It will result in a formatted table (uses pandas
# ##    dataframe) that contains the players data for that round without empty
# ##    values and with the following calculated data: DD+DP, FF+FD+FT, MSV1,
# ##    MSV2 and MSV3
# ## =============================================================================
# #    tabScouts.main(yearRnd)

# if __name__=='__main__':
#     main(yrRnd)