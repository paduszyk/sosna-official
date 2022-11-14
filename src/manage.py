#!/usr/bin/env python

import sys

import dotenv

# NOTE Don't forget to define DJANGO_SETTINGS_MODULE environment variable!

dotenv.load_dotenv()


def main():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django could not be imported.") from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
