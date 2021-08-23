import os
import time 
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1366x768") 

os.environ['WDM_LOG_LEVEL'] = '0'


def movie_bot(n,q, self):         # 'n' takes the name parameter and 'q' takes quality parameter
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options =chrome_options)
    
    name=n
    quality=q

    driver.get("https://moviesverse.org.in/?s="+name)

    #Waiting for the page to load then accessing the content box containing all the movie posts.

    try:
        
        try:
            content_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "content_box"))
            )
            articles = content_box.find_element_by_tag_name("article")          #Picking the first result post(most relevent).

            link = driver.find_element_by_tag_name("article").click()   #Accessing the first result post(most relevent) and clicking on that link.
        
        except:
            driver.quit()
            exit()
        
        try:
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])       #Switching to that extra pop-up window.
            driver.close()                                      #And closing it.
        except:
            pass
        driver.implicitly_wait(10)
        driver.switch_to.window(driver.window_handles[0])       #switching back again to main window.

        #now Accessing the download button according to quality choice.

        try:
            el1 = driver.find_element_by_xpath("(//a[@class='maxbutton-1 maxbutton maxbutton-download-links'])[1]")
        except:
            pass
            #error1 = 'Could not find the 480p link!'
        try:
            el2 = driver.find_element_by_xpath("(//a[@class='maxbutton-1 maxbutton maxbutton-download-links'])[2]")
        except:
            pass
            #error2 = 'Could not find the 720p link!'
        try:
            el3 = driver.find_element_by_xpath("(//a[@class='maxbutton-1 maxbutton maxbutton-download-links'])[3]")       
        except:
            pass
            #erroe3 = 'Could not find the 1080p link!'
        
        try:

            if quality == '3':              #For 1080p.
            
                if el3:
                    el3.click()
                
                elif el2:
                    el2.click()
                else:
                    el1.click()
        
            elif quality == '2':            #For 720p

                if el2:
                    el2.click()
                elif el3 :
                    el3.click()
                else:
                    el1.click()

            elif quality == '1':            #For 480p
            
                if el1:
                    ele1.click()
                elif el2:
                    el2.click()
                else:
                    el3.click()
            else:
                pass
        except:
            driver.quit()

        try:

            driver.implicitly_wait(10)
            driver.switch_to.window(driver.window_handles[2])
            driver.close()
        except:
            pass
            #print('no pop-up this time!')
        
        try:
            driver.implicitly_wait(10)
            driver.switch_to.window(driver.window_handles[1])       #Switching to the new opened tab containg next link.
        except:
            pass
        #First confirming the presence of page otherwise waiting for it then accessing the download button link.

        # try:
        #     print('here')
        #     header_id = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="masthead"]'))    
        #     )
        #     print('worked')
        # except:
        #     pass

        try:    
            driver.implicitly_wait(10)
            link2 = driver.find_element_by_class_name("maxbutton-1")
            
            link50 = driver.current_url
            global threadoo
            threadoo = threading.Thread(target= non_resumable, args=[link50])
            threadoo.daemon = True
            threadoo.start()


            link2.click()
            
        except:
            print('error')
            pass
            
        driver.implicitly_wait(20)
        driver.switch_to.window(driver.window_handles[2])

        #Explicetly waiting for the presence of that button and then clicking it
        try:
            el4 = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@id='landing']/div/center/img)"))
            )
            el4 = driver.find_element_by_xpath("(//div[@id='landing']/div/center/img)").click()            #Clicking Unlock download-link

        except:
            pass
            #print('unlocking gone')


        driver.implicitly_wait(10)                                                       #Implicitely waiting for "generate link" button to appear

        el5 = driver.find_element_by_xpath("(//a[@id='generater']/img)").click()        #After finding that button, clicking on it.

        #print('\nGenerated the link')

        driver.implicitly_wait(10)                                                      #Again waiting implicitely for "Download link is here" button to appear

        el6 = driver.find_element_by_id("showlink").click()                             #As button shows up clicking on it

        #print('\nOn drive share page')
        
        driver.implicitly_wait(10)

        driver.switch_to.window(driver.window_handles[3])

        driver.implicitly_wait(10)

        global link4, link5
        
        try:

            el7 = driver.find_element_by_xpath("(//a[@class='btn btn-outline-danger btn-sm btn-block'])")
            # print('lets see what happens next!')
            
            link4 = el7.get_attribute('href')
            
            driver.implicitly_wait(5)

            el8 = driver.find_element_by_xpath("//*[@id='direct']")
            el8.click()
         
            #print('On the G-drive page')
        
        except:
            pass
                
        try:
            el9 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"uc-download-link"))
            )

            el9 = driver.find_element_by_id("uc-download-link")

            link5 = el9.get_attribute('href')
            driver.quit()
            
        except:
            #print('You may have used this too many times, so wesite is blocking requests from your IP!!')
            link5='Not Found!'
            #pass
        driver.quit()


    except:
        self.root.ids.status.text = 'Sorry can not find anyhing named  "'+ name + '"  please recheck the spelling and try again.'
        driver.quit()
        

def non_resumable(link50):
    global link21, link51

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options =chrome_options)
    driver.get(link50)

    driver.implicitly_wait(5)

    el71 = driver.find_element_by_class_name("maxbutton-3")
    el71.click()

    driver.implicitly_wait(10)
    driver.switch_to.window(driver.window_handles[1])

    try:
        el41 = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH,"(//div[@id='landing']/div/center/img)"))      #    //div[@id='landing']/div/center/img
        )
        el41 = driver.find_element_by_xpath("(//div[@id='landing']/div/center/img)")             #Clicking Unlock download-link  
        el41.click()
            
    except:
        pass 

    try:
        driver.implicitly_wait(10)                                                       #Implicitely waiting for "generate link" button to appear

        el51 = driver.find_element_by_xpath("(//a[@id='generater']/img)").click()

        driver.implicitly_wait(10)                                                      #Again waiting implicitely for "Download link is here" button to appear

        el61 = driver.find_element_by_id("showlink").click()

        driver.implicitly_wait(10)

        driver.switch_to.window(driver.window_handles[2])

        driver.implicitly_wait(10)

        el81 = driver.find_element_by_xpath("(//*[@id='download']/center/form/button)")     #//*[@id="download"]/center/form/button
        link51 = el81.get_attribute('href')

        el21 = driver.find_element_by_xpath("(//*[@id='download']/center/form/a)")        #In case of No resume link 
        el21.click()
        driver.implicitly_wait(5)
        link21 = driver.current_url

        print(link21)
        print(link51)
        driver.quit()
    except:
        driver.quit()


def watch_nowa():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link4)
    return

def watch_nowb():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link21)
    return

def download_moviea():
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link5)
    driver.implicitly_wait(10)
    driver.find_element_by_id("uc-download-link").click()
    return

def download_movieb():
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link51)
    return