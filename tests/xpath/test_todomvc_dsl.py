from selene import have
from selene.support.shared import browser
from selene_intro.dsl import x, its


def test_complete_todo_dsl():
    # Given
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element(x.all().by(its.have_id('new-todo')).build()).type('a').press_enter()
    browser.element(x.all().by(its.have_id('new-todo')).build()).type('b').press_enter()
    browser.element(x.all().by(its.have_id('new-todo')).build()).type('c').press_enter()
    # When
    browser.element(x.all().by(its.have_id('todo-list')).child('li').by(its.with_text('b')).descendant()
                    .by(its.with_class('toggle')).build()).click()
    # Then
    browser.all(x.all().by(its.have_id('todo-list')).descendant().by(its.with_class('completed')).build())\
        .should(have.exact_texts('b'))
    browser.all(x.all().by(its.have_id('todo-list')).child('li').by(f"[not({its.with_class('completed')})]").build())\
        .should(have.exact_texts('a', 'c'))
    browser.all(x.all().by(its.have_id('todo-list')).child('li').build()).should(have.exact_texts('a', 'b', 'c'))