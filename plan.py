from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_data(Klasse : str):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://user:password@www.stundenplan24.de/schoolnumber/mobil")
    driver.get("https://www.stundenplan24.de/10019573/mobil/index.html")

    driver.execute_script(f"SeiteAKPlanAufrufen('{Klasse}')")

    html_list = driver.find_element_by_id("plan")
    list = html_list.find_elements_by_tag_name("li")
    
    maintem = ""
    for item in list:
        # print(item.text)
        maintem += item.text + "\n"
    driver.quit()
    return maintem
