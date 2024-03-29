from pytest import fixture

from gba.search import SearchEngine
from tests.store_test import store


@fixture(scope="module")
def search_engine(mistral_instruct, store):
    yield SearchEngine(store=store)


def test_search(search_engine):
    response = search_engine.search_internet(query="Which documents mention dogs?")

    assert "document 2" in response.lower()
    assert "document 1" not in response.lower()
