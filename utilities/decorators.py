import functools
from qase.pytest import qase


def qase_screenshot(func):
    """
    Decorator to attach screenshot to Qase test case
    :param func:
    :return: wrapper_decorator
    """

    @functools.wraps(func)
    def wrapper_decorator(self, *args, **kwargs):
        value = func(self, *args, **kwargs)
        if "FrameLocator" not in str(self.page):
            qase.attach(
                (
                    self.page.screenshot(full_page=True),
                    "image/png",
                    f"{func.__name__}.png",
                )
            )
        print(f"Screenshot attached for {func.__name__}")
        return value

    return wrapper_decorator
