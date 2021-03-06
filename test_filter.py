import pytest

from main.filtering import PatchworkHomePage
from main.result import FilteredPatchResults

from selenium.webdriver import Chrome


@pytest.fixture
def browser():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
  
   
# fails due to bug in application

def test_filter_by_series(browser):
  
  patchwork_page = PatchworkHomePage(browser)
  patchwork_page.load()
  patchwork_page.show_filters() 
  
  patchwork_page.filter_by_series('fix series querry')
  filtered_results = FilteredPatchResults(browser)
  assert filtered_results.active_filters_contains('Series') > -1
  
# fails due to bug in application 

def test_filter_by_submitter(browser):

  patchwork_page = PatchworkHomePage(browser)
  patchwork_page.load()
  patchwork_page.show_filters() 
     
  patchwork_page.filter_by_submitter('Stephen Finucane')
  filtered_results = FilteredPatchResults(browser)
  assert filtered_results.active_filters_contains('Submitter') > -1
  
def test_filter_by_state(browser):
  
  patchwork_page = PatchworkHomePage(browser)
  patchwork_page.load()
  patchwork_page.show_filters() 
  
  patchwork_page.filter_by_state('New')
  filtered_results = FilteredPatchResults(browser)
  assert filtered_results.active_filters_contains('State') > 1
  
def test_filter_by_search_term(browser):
  
  patchwork_page = PatchworkHomePage(browser)
  patchwork_page.load()
  patchwork_page.show_filters()
  
  patchwork_page.filter_by_search_term('query')
  filtered_results = FilteredPatchResults(browser)
  assert filtered_results.active_filters_contains('Search') > 1
  
def test_filter_by_archived(browser):
  
  patchwork_page = PatchworkHomePage(browser)
  patchwork_page.load()
  patchwork_page.show_filters() 
  
  patchwork_page.filter_by_archived('both')
  filtered_results = FilteredPatchResults(browser)
  assert filtered_results.active_filters_contains('Archived') > 1
  
def test_filter_by_delegate(browser):
  
  patchwork_page = PatchworkHomePage(browser)
  patchwork_page.load()
  patchwork_page.show_filters() 
  
  patchwork_page.filter_by_delegate('Nobody')
  filtered_results = FilteredPatchResults(browser)
  assert filtered_results.active_filters_contains('Delegate') > 1
