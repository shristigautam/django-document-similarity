#!/usr/bin/env python
#
# Copyright (C) 2013 Consumers Unified LLC
# Licensed under the GNU AGPL v3.0 - http://www.gnu.org/licenses/agpl.html

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docsim.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
