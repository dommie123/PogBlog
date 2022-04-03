from src.models import user_model
import pytest

class TestUser():
    @pytest.fixture()
    def test_setup(self):
        # TODO test setup
        pass
    
    def test_teardown(self):
        pass

    def test_login(self, test_setup):
        pass

    def test_logout(self, test_setup):
        pass

    def test_post_something(self, test_setup):
        pass

    def test_positive_vote(self, test_setup):
        pass

    def test_meh_vote(self, test_setup):
        pass

    def test_negative_vote(self, test_setup):
        pass

    def test_comment_on_post(self, test_setup):
        pass

    def test_share_post(self, test_setup):
        pass

    def test_change_settings(self, test_setup):
        pass