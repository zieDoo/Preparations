import sys
import json
# import re
# import requests
import subprocess

from bs4 import BeautifulSoup as bs
import selenium
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

LINK = "https://sk.bitefight.gameforge.com/game"
LOGIN_NAME = "Lichandro"
PSWD = "16pwd12*kerbATT01"

# print(LOGIN_NAME)


def login(username, password, web_link):

    # driver = webdriver.Chrome(path_to_chromedriver)

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    ### --- TOTO JE NA HEADLESS --- ###
    chrome_options.add_argument("--headless")

    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(web_link)

    # --- PORIESIT LOGIN --- !!! ###
    driver.find_element_by_id('loginName').send_keys(username)
    driver.find_element_by_id('loginPw').send_keys(password)
    driver.find_element_by_id('loginButton').click()

    page = driver.page_source
    page_soup = bs(page, 'html.parser')

    # --- ZAVRI DRIVER --- #
    driver.close()

    return page_soup


def get_info_bar(html_soup) -> dict:

    # print(page_soup)
    info_bar = html_soup.find('div', {'class': 'gold'})
    # print(info_bar)

    html_content_to_text = info_bar.text
    new_content_as_text = " ".join(html_content_to_text.split())
    # print('New text is: ', new_content_as_text)
    new_text = new_content_as_text.replace(' / ', '/')
    # print('New text is: ', new_text)
    # print('Typ of text is: ', type(new_text))

    new_list = list(new_text.split(" "))

    i = 0
    final_list = []

    for element in info_bar:
        title_pre_img = info_bar.find_all('img')
        # print(type(title_pre_img))
        # print(len(title_pre_img))
        values = title_pre_img[i]['alt']
        # print('CO TEDA: ', values)
        # print('values su: ', type(values))
        final_list.append(values)
        # print('Final list is: ', final_list)
        # print('Final type is: ', type(final_list))

        i += 1
        if i == len(title_pre_img):
            # Jump out from cycle
            break

    final_result = dic_func(final_list, new_list)

    # Vrat obsah z tagu s menom "gold"
    return final_result


def get_char_tab(html_soup) -> dict:
    char_tab = html_soup.find('div', {'id': 'character_tab'})
    # print('Co je v TABLE: ', char_tab)
    rows = char_tab.find('tbody').find_all('tr')
    # print('NASE RIADKY Z DRUHEJ TABULKY: ', rows)
    # print(type(rows))
    # print(type(info_bar))

    char_table = []

    for row in rows[:]:
        row_cell = row.text.replace('\n', ' ')
        # print(row_cell)
        # print(type(row_cell))
        char_table.append(row_cell.strip())
    # print(char_table)
    # print(type(char_table))
    into_dict = dict(i.split(':') for i in char_table)

    return into_dict


def dic_func(keys, values) -> dict:
    return dict(zip(keys, values))


def push_out(inside_data):
    # outsite_data = inside_data
    outside_data = json.dumps(inside_data, indent=2)

    # outside_data = inside_data
    # outside_data = json.dumps(inside_data, indent=4, sort_keys=True)
    # outside_data = json.dumps(inside_data, indent=2, ensure_ascii=False)
    # outside_data = json.dumps(inside_data, indent=4, sort_keys=True, ensure_ascii=False)
    # print("TOTO JE Z PYTHONU")
    # return inside_data
    return outside_data




# Return html content after login
full_content = login(LOGIN_NAME, PSWD, LINK)

# Return information bar lists from the html content
information_bar = get_info_bar(full_content)

# Return character table from html content
character_tab = get_char_tab(full_content)

# PRINTING FOR FINDING THE TYPE OF THE OUTPUTS FROM HTML CONTENT
# print(html_content)
# print(type(html_content))

# print(" ")

# VYPISE SLOVNIK z INFO_BARU - Pod seba
# -------------------------------------
# for k, v in information_bar.items():
#    print(k + ':', v)

# print(" ")

# VYPISE SLOVNIK CHARACTERU POSTAVY - Pod seba
# for m, n in character_tab.items():
#    print(m + ':', n.strip())

# ---> print(information_bar)
# ---> print(type(information_bar))
# print(character_tab)

# data_for_php = json.dumps(information_bar, indent=None, separators=(',', ':'))
#data_for_php = json.dumps(information_bar, separators=(',', ':'))
# ---> data_for_php = json.dumps(information_bar)
# print(type(character_tab))


# jemine = push_out(information_bar)
datovic = push_out(information_bar)
# print(datovic.encode('raw_unicode_escape').decode('unicode_escape'))
# print(datovic.encode('ascii').decode('unicode_escape'))
print(datovic)
# print(type(datovic))


pokusovic = push_out(character_tab)
print(pokusovic)
# print(type(pokusovic))



# print(push_out())
# print(type(push_out(ad)))

# ----------------- akoze = push_out(information_bar)
# print('ROZKOPAT: ', type(akoze), len(akoze))
# print(akoze)

# push_out(information_bar)

# -------> print(type(jemine))

# list_files = subprocess.run(["ls", "-l"])

# -------> json_arr = [{'key': i, 'value': jemine[i]} for i in jemine]

# -------> print(json.dumps(json_arr, ensure_ascii=False))

# -------> print(type(json_arr))


# result = json.dumps(jemine, indent=3, sort_keys=True, ensure_ascii=False)
# print(result)
# print(type(result))











# push_out(list_files)

# print("TOTO SU FILESY: ", list_files)

# print()

# print('tak nic: ', type(data_for_php))
# print('aj nieco ine ? : ', data_for_php)


