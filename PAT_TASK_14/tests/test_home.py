import pytest
from PAT_TASK_14.pages.dashboard_page import DashboardPage

@pytest.mark.positive
def test_logout_functionality(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.wait_for_url_contains("dashboard")
    dashboard_page.verify_logout_functionality()
    dashboard_page.wait_for_url_contains("login")
    print(logged_in_user.current_url)
    curr_url = logged_in_user.current_url
    assert "login" in curr_url