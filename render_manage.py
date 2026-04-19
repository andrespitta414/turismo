#!/usr/bin/env python
import sys

from django.core.management import execute_from_command_line

from render_bootstrap import bootstrap_django_settings


def main() -> None:
    bootstrap_django_settings()
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
