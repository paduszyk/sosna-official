#!/usr/bin/env python

import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

# Append the source dir to the PYTHONPATH env. variable

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


def main():
    """
    Set up the test runner and run tests.
    """
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"

    django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])

    sys.exit(bool(failures))


if __name__ == "__main__":
    main()
