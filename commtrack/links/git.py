# Copyright 2019 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import logging
import os

from commtrack.git import constants
from commtrack.link import Link

LOG = logging.getLogger(__name__)


class Git(Link):
    """Managing operations on Git based servers."""

    def __init__(self, name, address):
        super(Git, self).__init__(name, address, constants.LINK_TYPE)
        self.name = name
        self.address = address

    def locate_project(self, project):
        """Returns project path.

        If project couldn't be find, return None.
        """
        for path in constants.PROJECT_PATHS:
            if os.path.isdir(path):
                LOG.debug("Located project {}: {}".format(project, path))
                return path
        return

    def search(self, address, params):
        """Returns result of the search based on the given change."""
        project_path = self.locate_project(params['project'])
        if not project_path:
            pass
        print(project_path)
