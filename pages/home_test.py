from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.title = page.get_by_role("link", name="Products", exact=True)
        self.loc = page.get_by_role("link", name="Products", exact=True)
        self.role= page.get_by_role("link", name="Solutions")
        self.schedule = page.get_by_role("link", name="Resources")
    def is_title_correct(self):
        img=expect(self.title.get_by_role("navigation")).to_match_aria_snapshot("- link \"Products\":\n  - /url: /our-products")
        #expect(img).to_have_screenshot() # Compares a specific element
        print("image matched")
        self.title.click()
    def is_loc_visible(self):
        self.loc.click()
    def find_by_name(self):
        self.role.click()
    def find_name(self):
        self.schedule.click()


