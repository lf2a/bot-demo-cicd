import platform

from botcity.web import WebBot, Browser, By

from botcity.maestro import AutomationTaskFinishStatus as FinishStatus

from . import exceptions


class Bot(WebBot):

    def action(self, execution=None):
        os_name = platform.system()
        self.headless = True
        self.browser = Browser.FIREFOX
        if os_name == 'Linux':
            self.driver_path = self.get_resource_abspath(filename='geckodriver')
        else:
            self.driver_path = self.get_resource_abspath(filename='geckodriver.exe')

        try:
            self.open_browser(url='https://lf2a.github.io/tests-botcity-framework-web-python/')
            self.print_result()

            print(f"{execution.task_id} {execution.server} {execution.token} {execution.parameters}")

            if execution:
                self.finish_task(FinishStatus.SUCCESS, f"Task Finished with success.", execution.task_id)
        except Exception as e:
            if execution:
                self.finish_task(FinishStatus.FAILED, f"Task Finished with error ({e}).", execution.task_id)
        finally:
            self.stop_browser()

    def finish_task(self, finish_status, message, task_id):
        self.maestro.finish_task(
            task_id=task_id,
            status=finish_status,
            message=message
        )

    def not_found(self, label):
        print(f"Element not found: {label}")
        raise exceptions.ImageNotFoundError(f"Element not found: {label}")

    def open_browser(self, url):
        self.browse(url)
        self.wait(2_000)

    def print_result(self):
        if not self.find("mario2", matching=0.97, waiting_time=10_000):
            self.not_found("mario2")
        self.click(2_000)

        element = self.find_element(selector='element-result', by=By.ID)
        assert element.text == '{"data":["img04"]}'
        print(element.text)
        print("updated!")


if __name__ == '__main__':
    Bot.main()
