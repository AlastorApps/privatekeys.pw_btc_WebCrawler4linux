#shibu thomas  
#this code was created on 18-5-2020 | adapted for Linux (with Firefox) on 10-3-2025 by Luca Armiraglio
#the path where u have installed Firefox should be changed accordingly - now it's set at the default one


from random import randint
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import selenium.common.exceptions

#file
file=open("pages_with_balance.txt","w")
def setup_driver():
    browser = webdriver.Firefox()
    return browser

def random_page(last_page=None):
    try:
        page_number=randint(1,2573157538607026564968244111304175730063056983979442319613448069811514699875)
        driver=setup_driver()
        driver_url="https://privatekeys.pw/bitcoin/keys/"+str(page_number)
        driver.get(driver_url)
        btcBalanceInThePage=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/main/div[@class='container-fluid']/h3[@class='text-center']/span[@class='js-balances-bitcoin']/span[@class='badge badge-light']")))
        balance_on_the_page=float(btcBalanceInThePage.text)
        driver.close()
    except Exception:
        balance_on_the_page=0
        # page_number=None
        print("timeout retrying......")
        driver.close()
    return (balance_on_the_page,page_number)


if __name__ == "__main__":
    condition=True
    try:
        while(condition):
            balance,page=random_page()
            if(balance>0):
                print("go to bitcoin directory page  number {} on privatekeys.pw".format(page))
                file.writelines(page+"\n")
    except KeyboardInterrupt:
        file.close()
        print("crtl+d pressed")
        sys.exit()

    except selenium.common.exceptions.NoSuchWindowException:
        file.close()
        print("browser window closed")
        sys.exit()
