from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def options():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.barchart.com/options/unusual-activity/stocks')

    options_data = []

    for i in range(1, 11):
        stock = driver.find_element_by_xpath(
            f'//*[@id="main-content-column"]/div[6]/div/div[2]/div/div/ng-transclude/table/tbody/tr[{i}]')
        data = stock.text.split()

        # [Symbol, Type, Price, Strike Price, Expiration Date, Ask Price, Volume, Open Interest]
        curr = [data[0], data[2], data[1], data[3], data[4], data[8], data[10], data[11]]
        options_data.append(curr)

    driver.close()
    return options_data
