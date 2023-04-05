import requests

def test_existing_repo_can_be_found():
    pass


def test_non_existing_repo_can_be_found():
    r = github_api_client.search_repo("smdnfbsmdfbsmfdsbfmsdb")
    assert r['total_count'] ==0

def test_search_not_working_without_q():
    pass