from datetime import datetime

import pytest


def pytest_configure(): # This hook is called for every plugin and initial conftest file after command line options have been parsed.

    print(f"{datetime.now()}: pytest开始执行")


def pytest_unconfigure(): # Called before test process is exited.

    print(f"{datetime.now()}: pytest结束执行")


