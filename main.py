from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('https://finance.yahoo.com/quote/BTC-EUR/history/?guccounter=2')

dates = driver.find_elements_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr/td[1]/span')
closes = driver.find_elements_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr/td[5]/span')

eur_btc_rates = []

for i in range(len(dates))[:9]:
    new_Data={'Date': dates[i].text,
              'BTC Closing Value': closes[i].text}
    eur_btc_rates.append(new_Data)

df_data=pd.DataFrame(eur_btc_rates)
df_data.to_excel('eur_btc_rates.csv.xlsx', index=False)

driver.quit()







