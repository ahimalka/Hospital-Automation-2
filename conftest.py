import pytest

@pytest.fixture
def hospital_page(page):
    page.goto ("https://qahackeru3.netlify.app/")

    return page




