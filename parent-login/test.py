from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

usernames = ['userid','B17XXXXCS']
dobs = ['dob', 'XX-XX-XXXX']
names = ['name', 'XXXXX XXXXX']

for i in range(len(usernames)):
    if i == 0:
        continue
    print(names[i] + " "+usernames[i] + " " + dobs[i])
    bot = webdriver.Firefox()
    bot.get('http://dss.nitc.ac.in/nitcreg/parentlogin.aspx')
    email = bot.find_element_by_id('txtusername')
    password = bot.find_element_by_id('txtDOB')
    email.clear()
    password.clear()
    email.send_keys(usernames[i])
    password.send_keys(dobs[i])
    password.send_keys(Keys.RETURN)

    bot.get('http://dss.nitc.ac.in/nitcreg/TestMarkNew.aspx')
    select = bot.find_element_by_tag_name('select')
    options = [x for x in select.find_elements_by_tag_name("option")]
    for option in options:
        if(option.text == 'Mid Term Test'):
            option.click()
    try:
        table_id = bot.find_element_by_id('_ctl0_ContentPlaceHolder1_grvtest')
    except:
        bot.quit()
        continue
    t_body = table_id.find_element_by_tag_name('tbody')
    rows = t_body.find_elements_by_tag_name('tr')
    for row in rows:
        cols = row.find_elements_by_tag_name('td')
        for col in cols:
            marks = col.find_element_by_tag_name('span')
            print(marks.text)
    print('----')
    bot.quit()
