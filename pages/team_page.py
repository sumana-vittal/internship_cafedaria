from pages.base_page import Page


class TeamPage(Page):

    def verify_team_page_opens(self):
        self.verify_partial_url("team")
