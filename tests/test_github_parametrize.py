from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.mark.parametrize(["browser_width", "browser_height"],
                         [(1980, 1024), (900, 600)],
                         ids=["Desktop version", "Mobile version"],
                         )
def test_with_param(browser_width, browser_height):
    browser.config.window_width = browser_width
    browser.config.window_height = browser_height

    browser.open('/')

    if (browser_width == 1980) and (browser_height == 1024):
        s(".HeaderMenu-link--sign-in").click()
    elif (browser_width == 900) and (browser_height == 600):
        s(".Button-label").click()
        s(".HeaderMenu-link--sign-in").click()
    else:
        pytest.fail("Unknown browser format: it makes sense to verify test input values.")


