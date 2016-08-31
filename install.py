"""
Copyright (c) 2015 Red Hat, Inc
All rights reserved.

This software may be modified and distributed under the terms
of the MIT license. See the LICENSE file for details.
"""

import os
import shutil

from cct.module import Module

class Install(Module):

    def _move(self, src, dst):
        if not os.path.exists(dst):
            os.makedirs(dst)

        for f in os.listdir(src):
            shutil.move(os.path.join(src,f), dst)

    def launch(self):
        self._move("/tmp/cct/jboss-common/dynamic-resources", "/usr/local/dynamic-resources")

    def s2i(self):
        self._move("/tmp/cct/jboss-common/s2i", "/usr/local/s2i")
