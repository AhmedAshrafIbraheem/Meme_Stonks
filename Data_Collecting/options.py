from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def options():
    driver = webdriver.Chrome('/Users/Shourav/Downloads/chromedriver')
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


options()
