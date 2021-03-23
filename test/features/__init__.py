from aloe import before, step, world
# from urllib.parse import urljoin
#
# from pytest_bdd import scenario, given, when, then
# from splinter import Browser
# from lettuce import *
# from nose.tools import assert_equals
#
# browser = Browser()
# browser.url = 'http://127.0.0.1:5000/'

from splinter import Browser
browser=Browser(headless=True)

@step(r"I visit the web site")
def visit_site_step(self):
    browser.visit('http://127.0.0.1:5000')

@step(r"I am on the home page")
def _I_am_on_the_home_page_step(self):
    browser.visit('http://127.0.0.1:5000/')

@step(r"I should see the list")
def _I_should_see_a_list_of_pieces_step(self):
    browser.find_by_tag('ul')
    browser.find_by_name('filterbox')

@step(r"I fill in composer with Bach")
def fill_in_composer_step(self):
    browser.fill('composer','Bach')
    b=browser.find_by_id('submit-button')
    b.click()

@step(r"I fill in title with Prelude")
def fill_in_composer_step(self):
    browser.fill('title','Prelude')
    b=browser.find_by_id('submit-button')
    b.click()

@step(r"I fill in composer with Bach")
def fill_in_composer_step(self):
    browser.fill('composer','Bach')
    b=browser.find_by_id('submit-button')
    b.click()

@step(r"I fill in instrument with Piano")
def fill_in_instrument_step(self):
    browser.fill('instrument','Piano')
    b=browser.find_by_id('submit-button')
    b.click()


@step(r"I should see a refresh button")
def _I_should_see_a_refresh_button_step(self):
    browser.find_by_name("refresh")

@step(r"I should see one item in the list")
def _I_should_see_one_item_in_the_list(self):
    l=browser.find_by_tag("li")
    assert len(l) == 1, f"List length is {len(l)}"

@step(r"I should see two items in the list")
def _I_should_see_two_item_in_the_list(self):
    l=browser.find_by_tag("li")
    assert len(l) == 2, f"List length is {len(l)}"

@step(r"I fill in title with w")
def _I_fill_in_title_with_w(self):
    browser.fill("title","w")

@step(r"I should see no items in the list")
def _I_should_see_no_items_in_the_list(self):
    l=browser.find_by_tag("li")
    assert len(l) == 0, f"List length is {len(l)}"