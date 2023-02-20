from selene import by, be, have
from selene.support.shared import browser


def test_complete_task():
    # open TodoMVC page
    browser.open('https://todomvc.com/examples/emberjs/')

    browser.element('//*[@id="new-todo"]').type('a').press_enter()
    browser.element('//*[@id="new-todo"]').type('b').press_enter()
    browser.element('//*[@id="new-todo"]').type('c').press_enter()

    browser.all('//*[@id="todo-list"]//li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('//*[@id="todo-list"]//li').element_by(have.exact_text('b')).element('.toggle').click()

    browser.all('//*[@id="todo-list"]//li[@class="completed"]').element_by(have.exact_text('b'))
    browser.all('//*[@id="todo-list"]//li[@class="completed"]').element_by(have.no.exact_texts('a', 'c'))