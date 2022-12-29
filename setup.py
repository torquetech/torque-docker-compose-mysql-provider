# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""DOCSTRING"""

import os

from setuptools import setup


CURDIR = os.path.abspath(os.path.dirname(__file__))


def load_file(name: str) -> str:
    with open(f"{CURDIR}/{name}", encoding="utf8") as file:
        return file.read().strip()


setup(name="torque-docker-compose-mysql-provider",
      version=load_file("VERSION"),
      author="Torque Team",
      author_email="team@torquetech.io",
      description="",
      long_description=load_file("README.md"),
      long_description_content_type="text/markdown",
      url="https://github.com/torquetech/torque-docker-compose-mysql-provider",
      license="MPL v2.0",
      classifiers=[
          "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)"
      ],
      packages=[
          "torque"
      ],
      python_requires=">=3.10",
      install_requires=[
          "jinja2"
      ],
      entry_points={
          "torque": [
              "torque-docker-compose-mysql-provider=torque.docker_compose_mysql:repository"
          ]
      })
