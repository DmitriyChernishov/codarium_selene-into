from selene import have
from selene.support.shared import browser
from selene_intro.helpers import XPathBuilder


def test_add_and_complete_todo():
    # Given
    browser.open('https://todomvc.com/examples/emberjs/')

    browser.element('//*[@id="new-todo"]').type('a').press_enter()
    browser.element('//*[@id="new-todo"]').type('b').press_enter()
    browser.element('//*[@id="new-todo"]').type('c').press_enter()
    xpath = XPathBuilder()
    result = xpath\
            .have_id("todo-list")\
            .tag("li")\
            .with_text("b")\
            .child(XPathBuilder.tag("*").with_class("toggle").build())\
            .build()
    browser.element((f'//*[@id="todo-list"]/{result}')).click()