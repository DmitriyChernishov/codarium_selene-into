from selene import by, be, have
from selene.support.shared import browser


def test_complete_todo():
    # open TodoMVC page
    browser.open('https://todomvc.com/examples/emberjs/')

    # Try to add elements in to do
    browser.element(by.id('new-todo')).type('a').press_enter()
    browser.element(by.id('new-todo')).type('b').press_enter()
    browser.element(by.id('new-todo')).type('c').press_enter()

    # Checking that the was successfully add elements
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    # Mark the element as completed
    browser.element('#todo-list>li#ember11').element('input.toggle').click()

    # Checking which element is completed and which are active
    browser.element('#todo-list>li.completed').element('label').should(have.exact_text('b'))
    browser.element('#todo-list>li.completed').element('label').should(have.no.exact_texts('a', 'c'))