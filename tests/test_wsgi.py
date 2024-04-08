import pytest
from cryptoExchange import app

@pytest.fixture
def wsgi_test_client():
    with app.test_client() as client:
        yield client


class TestWSGI:
    TEST_COIN_SYMBOL = "BTC"

    def test_current_price_endpoint(self, wsgi_test_client):
        resp = wsgi_test_client.get(f"/price")
        assert resp.status_code == 404

        resp = wsgi_test_client.get(f"/price/{self.TEST_COIN_SYMBOL}")
        assert resp.status_code == 201

        resp = wsgi_test_client.post(f"/price/{self.TEST_COIN_SYMBOL}")
        assert resp.status_code == 405

        resp = wsgi_test_client.delete(f"/price/{self.TEST_COIN_SYMBOL}")
        assert resp.status_code == 405


    def test_price_history_endpoint(self, wsgi_test_client):
        resp = wsgi_test_client.get(f"/price/history")
        assert resp.status_code == 200

        resp = wsgi_test_client.get(f"/price/history?page=1")
        assert resp.status_code == 200

        resp = wsgi_test_client.get(f"/price/history?page=0")
        assert resp.status_code == 500

        resp = wsgi_test_client.post(f"/price/history")
        assert resp.status_code == 405

        resp = wsgi_test_client.delete(f"/price/history")
        assert resp.status_code == 204

        resp = wsgi_test_client.delete(f"/price/history?page=1")
        assert resp.status_code == 204

        resp = wsgi_test_client.delete(f"/price/history?thisparamdoesnotmatter=1")
        assert resp.status_code == 204
