import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button(browser):
    browser.get(link)

    #time.sleep(5)
    add_button = bool(browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"))

    assert add_button == True, "Add to cart button doesn't exist!"