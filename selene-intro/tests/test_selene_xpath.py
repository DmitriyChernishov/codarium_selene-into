from selene import by, be, have
from selene.support.shared import browser


def test_complete_task():
    # open TodoMVC page
    browser.open('https://todomvc.com/examples/emberjs/')

    # Try to add elements in to do list
    browser.element(by.xpath('//*[@id="new-todo"]')).type('a').press_enter()
    browser.element(by.xpath('//header/input')).type('b').press_enter()
    browser.element(by.xpath('//input')).type('c').press_enter()

    # Checking that the added elements present in list
    browser.elements('//*[@id="todo-list"]//label').should(have.exact_texts('a', 'b', 'c'))

    # Do completed element b
    browser.element('//li[2]//input[@class="toggle"]').click()

    # Checking which element is completed and which are active
    browser.all('//li[@class="completed ember-view"]//label').should(have.exact_texts('b'))
    browser.all('//li[@class="completed ember-view"]//label').should(have.no.exact_texts('a', 'c'))