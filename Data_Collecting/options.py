from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


def options():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.barchart.com/options/unusual-activity/stocks')

    Symbol = []
    # Company_Name = []
    Type = []
    Price = []
    Strike_Price = []
    Expiration_Date = []
    Ask_Price = []
    Volume = []
    Open_Interest = []

    # stock = driver.find_element_by_xpath('//*[@id="main-content-column"]/div[6]/div/div[2]/div/div/ng-transclude/table/tbody/tr[1]')
    # stock2 = driver.find_element_by_xpath('//*[@id="main-content-column"]/div[6]/div/div[2]/div/div/ng-transclude/table/tbody/tr[2]')
    # stock3 = driver.find_element_by_xpath('//*[@id="main-content-column"]/div[6]/div/div[2]/div/div/ng-transclude/table/tbody/tr[3]')

    for i in range(1, 11):
        stock = driver.find_element_by_xpath(
            f'//*[@id="main-content-column"]/div[6]/div/div[2]/div/div/ng-transclude/table/tbody/tr[{i}]')
        data = stock.text.split()
        Symbol.append(data[0])
        # Company_Name.append()
        Type.append(data[2])
        Price.append(data[1])
        Strike_Price.append(data[3])
        Expiration_Date.append(data[4])
        Ask_Price.append(data[8])
        Volume.append(data[10])
        Open_Interest.append(data[11])

    print(Symbol)
    print(Type)
    print(Price)
    print(Strike_Price)
    print(Expiration_Date)
    print(Ask_Price)
    print(Volume)
    print(Open_Interest)

    # print(stock2.text)
    driver.close()

#AHMED: DELETE THIS IF YOU DONT NEED IT OR WHATEVER BOSS
def test():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.barchart.com/options/unusual-activity/stocks')

    options = []


    for i in range(1, 11):
        info = []
        stock = driver.find_element_by_xpath(
            f'//*[@id="main-content-column"]/div[6]/div/div[2]/div/div/ng-transclude/table/tbody/tr[{i}]')
        data = stock.text.split()
        info.append(data[0])
        # Company_Name.append()
        info.append(data[2])
        info.append(data[1])
        info.append(data[3])
        info.append(data[4])
        info.append(data[8])
        info.append(data[10])
        info.append(data[11])
        options.append(info)

    print(options)
    print(options[0])
    print(options[1])
    print(options[9])

    # print(stock2.text)
    driver.close()



