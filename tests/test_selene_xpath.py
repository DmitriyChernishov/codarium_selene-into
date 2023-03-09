from selene import by, be, have
from selene.support.shared import browser


def test_complete_task():
    browser.open('https://todomvc.com/examples/emberjs/')

    browser.element('//*[@id="new-todo"]').type('a').press_enter()
    browser.element('//*[@id="new-todo"]').type('b').press_enter()
    browser.element('//*[@id="new-todo"]').type('c').press_enter()

    browser.all('//*[@id="todo-list"]//li').should(have.exact_texts('a', 'b', 'c'))

    browser.element(f'//*[@id="todo-list"]//li[.//text()="b"]{contain_class("toggle")}').click()

    browser.element(f'//*[@id="todo-list"]{contain_class("completed")}').should(have.exact_text('b'))
    browser.all(f'//*[@id="todo-list"]//li{not_contain_class("completed")}').should(have.exact_texts('a', 'c'))


def contain_class(value):
    return f'//*[contains(concat(" ", normalize-space(@class), " "), " {value} ")]'


def not_contain_class(value):
    return f'[not(contains(concat(" ", normalize-space(@class), " "), " {value} "))]'