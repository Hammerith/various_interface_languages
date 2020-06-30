import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_basket_button(browser):
    browser.get(link)
    # time.sleep(30)
    button_add = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button_add > 0, 'button not found'




