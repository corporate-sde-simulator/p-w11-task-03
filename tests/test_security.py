import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from userSearch import UserSearch

class TestSQLInjection:
    @pytest.fixture
    def search(self): return UserSearch()

    def test_normal_search(self, search):
        results = search.search_by_name('Alice')
        assert len(results) == 1

    def test_injection_returns_nothing(self, search):
        results = search.search_by_name("' OR '1'='1")
        assert len(results) == 0, "SQL injection should return 0 results, not dump entire table"

    def test_email_injection(self, search):
        results = search.search_by_email("' OR '1'='1' --")
        assert len(results) == 0, "Email search is vulnerable to SQL injection"

    def test_role_injection(self, search):
        results = search.get_by_role("user' OR role='superadmin")
        assert all(r[3] != 'superadmin' for r in results), "Should not expose superadmin"
