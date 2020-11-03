import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button(browser):
    browser.get(link)
    time.sleep(20)

    assert browser.find_element_by_css_selector(".btn-add-to-basket1"),  "help me to find the button"

