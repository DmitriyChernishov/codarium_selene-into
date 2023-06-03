from selene import have
from selene.support.shared import browser
from selene_intro.dsl import x, Its


def test_complete_todo_dsl_v2():
    # Given
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element(x.all().by(Its.id('new-todo')).build()).type('a').press_enter()
    browser.element(x.all().by(Its.id('new-todo')).build()).type('b').press_enter()
    browser.element(x.all().by(Its.id('new-todo')).build()).type('c').press_enter()
    # When
    browser.element(x.all().by(Its.id('todo-list')).child('li').by(Its.text('b')).descendant()
                    .by(Its.css_class('toggle')).build()).click()
    # Then
    browser.all(x.all().by(Its.id('todo-list')).descendant().by(Its.css_class('completed')).build())\
        .should(have.exact_texts('b'))
    browser.all(x.all().by(Its.id('todo-list')).child('li').by_not((Its.css_class('completed'))).build())\
        .should(have.exact_texts('a', 'c'))
    browser.all(x.all().by(Its.id('todo-list')).child('li').build()).should(have.exact_texts('a', 'b', 'c'))
    # End
    browser.config.quit_driver()
