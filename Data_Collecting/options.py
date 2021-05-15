from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Options function first creates a remote connection to the website to be scraped using selenium, in this case barchart.com, then renders the
# obfuscated javascript code of the website in the remote environment so it can be accessed by the options function. Then the
# individual cells containing the desired data is iteratively accessed and saved to a list of lists and then accessed by the database
# located in controller.py.

def options():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.barchart.com/options/unusual-activity/stocks')

    #Lists of lists to store options data
    options_data = []

    #iterative loop that accesses scraped options data cells and saves them in options_data list.
    for i in range(1, 11):
        stock = driver.find_element_by_xpath(
            f'//*[@id="main-content-column"]/div[6]/div/div[2]/div/div/ng-transclude/table/tbody/tr[{i}]')
        data = stock.text.split()

        # [Symbol, Type, Price, Strike Price, Expiration Date, Ask Price, Volume, Open Interest]
        curr = [data[0], data[2], data[1], data[3], data[4], data[8], data[10], data[11]]
        options_data.append(curr)

    #close remote chrome connection to avoid too many website requests and prevent being blocked by barchart.com
    driver.close()
    return options_data
