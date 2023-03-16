from selene import have
from selene.support.shared import browser
from selene_intro.helpers import contain_class


def test_add_and_complete_todo():
    # Given
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('//*[@id="new-todo"]').type('a').press_enter()
    browser.element('//*[@id="new-todo"]').type('b').press_enter()
    browser.element('//*[@id="new-todo"]').type('c').press_enter()
    # When
    browser.element(f'//*[@id="todo-list"]//li[.//text()="b"]//*[{contain_class("toggle")}]').click()
    # Then
    browser.all(f'//*[@id="todo-list"]//*[{contain_class("completed")}]').should(have.exact_texts('b'))
    browser.all(f'//*[@id="todo-list"]//li[not({contain_class("completed")})]').should(have.exact_texts('a', 'c'))
    browser.all('//*[@id="todo-list"]//li').should(have.exact_texts('a', 'b', 'c'))