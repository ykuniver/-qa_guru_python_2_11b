from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.fixture(scope='function')
def application(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize("application", [(900, 600), (1980, 1024)], indirect=True)
def test_with_param(application):

    if (browser.config.window_width != 900) and (browser.config.window_height != 600):
        pytest.skip("This test is to be used on mobile browser")

    browser.open('/')

    s(".Button-label").click()
    s(".HeaderMenu-link--sign-in").click()


