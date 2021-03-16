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

@step(r"I am on the home page")
def _I_am_on_the_home_page(self):
    browser.visit('http://127.0.0.1:5000/')

@step(r"I should see a list of pieces")
def _I_should_see_a_list_of_pieces(self):
    browser.find_by_tag('ul')
