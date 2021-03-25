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

@step(r'I fill in composer with "([^"]+)"')
def fill_in_composer_step(self,composer):
    browser.fill('composer',composer)
    b=browser.find_by_id('submit-button')
    b.click()

@step(r'I fill in title with "([^"]+)"')
def fill_in_title_step(self,title):
    browser.fill('title',title)
    b=browser.find_by_id('submit-button')
    b.click()

@step(r'I fill in instrument with "([^"]+)"')
def fill_in_instrument_step(self,inst):
    browser.fill('instrument',inst)
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

@step(r"I should see no items in the list")
def _I_should_see_no_items_in_the_list(self):
    l=browser.find_by_tag("li")
    assert len(l) == 0, f"List length is {len(l)}"

@step(r'When I click on reset')
def _I_click_on_reset(self):
    r=browser.find_by_name("reset")
    r.click()
