from selene import have
from selene.support.shared import browser
from selene_intro.helpers import contain_class, not_contain_class


def test_complete_task():
    browser.open('https://todomvc.com/examples/emberjs/')

    browser.element('//*[@id="new-todo"]').type('a').press_enter()
    browser.element('//*[@id="new-todo"]').type('b').press_enter()
    browser.element('//*[@id="new-todo"]').type('c').press_enter()

    browser.all('//*[@id="todo-list"]//li').should(have.exact_texts('a', 'b', 'c'))

    browser.element(f'//*[@id="todo-list"]//li[.//text()="b"]{contain_class("toggle")}').click()

    browser.element(f'//*[@id="todo-list"]{contain_class("completed")}').should(have.exact_text('b'))
    browser.all(f'//*[@id="todo-list"]//li{not_contain_class("completed")}').should(have.exact_texts('a', 'c'))