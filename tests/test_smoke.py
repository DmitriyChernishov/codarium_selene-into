from selene import have, be
from selene.support.shared import browser
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s


def check_available():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    #clear_completed_js_loaded = "return $._data($('#clear-completed').get(0), 'events').hasOwnProperty('click')"
    #browser.wait.for_(have.js_returned(True, clear_completed_js_loaded))
    is_TodoMVC_loaded = 'return (Object.keys(require.s.contexts._.defined).length === 39)'
    browser.should(have.js_returned(True, is_TodoMVC_loaded))


def test_add_todo():
    # Given
    browser.open('https://todomvc4tasj.herokuapp.com/')
    check_available()
    browser.element('#new-todo').should(be.enabled).type('a').press_enter()
    browser.element('#new-todo').should(be.enabled).type('b').press_enter()
    browser.element('#new-todo').should(be.enabled).type('c').press_enter()

    browser.all("#todo-list>li").should(have.texts('a', 'b', 'c'))

    browser.all("#todo-list>li").element_by(have.exact_text('b')).element(".toggle").click()
    browser.clear_local_storage()


def test_complete_todo():
    # Given
    browser.open('https://todomvc4tasj.herokuapp.com/')
    check_available()
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    # When
    browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
    # Then
    browser.all('#todo-list>li.completed').should(have.exact_texts('b'))
    browser.all('#todo-list>li:not(.completed)').should(have.exact_texts('a', 'c'))
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
    browser.clear_local_storage()


def test_delete_todo():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    check_available()
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    browser.element('#todo-list>li:nth-of-type(2) .destroy').click()

    browser.all('#todo-list>li').should(have.exact_texts('a'))
    browser.clear_local_storage()


def test_edit_todo():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    check_available()
    browser.element('#new-todo').type('a').press_enter()

    # When
    browser.element('.view > label').double_click()
    browser.element('#todo-list>li').should(have.css_class('.active editing'))
    # Then
    browser.element('.view > label').clear()
    browser.element('.view > label').type('Test update')
    browser.all('#todo-list>li').should(have.exact_texts('Test update'))
    # End
    browser.clear_local_storage()