import os
import conftest
from botcity.web import WebBot, By


def test_click_on_image(web: WebBot):
    web.browse(url='https://lf2a.github.io/tests-botcity-framework-web-python/')
    web.add_image(label='mario2', path=os.path.join(conftest.PROJECT_DIR, 'botDemoCiCd', 'resources', 'mario2.png'))
    if not web.find("mario2", matching=0.97, waiting_time=10_000):
        raise RuntimeError('Not found: mario2')
    web.click(2_000)

    element = web.find_element(selector='element-result', by=By.ID)
    assert element.text == '{"data":["img04"]}'
