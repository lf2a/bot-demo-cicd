import os
import pytest
import platform

from botcity.web import WebBot, Browser, By

OS_NAME = platform.system()
PROJECT_DIR = os.path.abspath('')


def setup_firefox(headless: bool) -> WebBot:
    web = WebBot(headless)
    web.browser = Browser.FIREFOX
    web.driver_path = os.path.join(PROJECT_DIR, 'botDemoCiCd', 'resources', 'geckodriver')
    return web


@pytest.fixture
def web(request):
    is_headless = request.config.getoption("--headless")
    web = setup_firefox(is_headless)
    yield web
    web.stop_browser()


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_const', const=True)
