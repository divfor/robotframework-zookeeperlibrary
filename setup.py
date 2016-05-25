#!/usr/bin/env python

#  Copyright (c) 2010 Franz Allan Valencia See
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""Setup script for Robot's YamlLibrary distributions"""

from distutils.core import setup

import sys, os
sys.path.insert(0, os.path.join('src', 'ZookeeperLibrary'))

from version import VERSION

def main():
    setup(name         = 'robotframework-zookeeperlibrary',
          version      = VERSION,
          description  = 'Zookeeper utility library for Robot Framework',
          author       = 'Fred Huang',
          author_email = 'divfor@gmail.com',
          url          = 'https://github.com/divfor/robotframework-zookeeperlibrary',
          package_dir  = { '' : 'src'},
          install_requires = ["kazoo"],
          packages     = ['ZookeeperLibrary']
          )
        

if __name__ == "__main__":
    main()
