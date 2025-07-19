from playwright.sync_api import Page
from pages.home_test import HomePage
import pytest

def get_data_from_csv():
    import csv
    data = []
    with open("./test_data/Data.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data        
@pytest.mark.parametrize("data", get_data_from_csv())
def test_google_search(page: Page, data):
    page.goto("https://www.nuxi.com", wait_until="load")
    homrtest = HomePage(page)
    homrtest.is_loc_visible()
    homrtest.find_by_name()
    homrtest.find_name()
    
    