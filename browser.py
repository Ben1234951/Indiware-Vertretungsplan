from selenium import webdriver
from tinydb import Query, TinyDB
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(chrome_options=options)

db = TinyDB("database.json")
User = Query()


def get_data(Klasse : str, id, day_before=None,day_after=None, wie_oft=None):
    username = db.get(User.user_id == id).get("username")
    password = db.get(User.user_id == id).get("password")
    schoolnumber = db.get(User.user_id == id).get("schoolnumber")

    driver.get(f"https://{username}:{password}@www.stundenplan24.de/{schoolnumber}/mobil")
    driver.get(f"https://www.stundenplan24.de/{schoolnumber}/mobil/index.html")
    driver.execute_script(f"SeiteAKPlanAufrufen('{Klasse}')")
    if day_after == True:
        for i in range(wie_oft):
            driver.execute_script("SeiteKpWechselNaechstesDatum()")
    elif day_before == True:
        for i in range(wie_oft):
            driver.execute_script("SeiteKpWechselVorigesDatum()")

    html_list = driver.find_element_by_id("plan")
    list = html_list.find_elements_by_tag_name("li")
    
    maintem = ""
    for item in list:
        # print(item.text)
        maintem += item.text + "\n"
    datum = driver.find_element_by_class_name("plkopfzeile").text
    return maintem, datum

def write_class(id, Klasse):
    db.upsert({"Klasse" : Klasse}, User.user_id == id)

def read_class(id):
    result = db.get(User.user_id == id)
    x = result.get("Klasse")
    return x