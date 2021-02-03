#!/bin/bash

set -e
rm -rf repositories
mkdir repositories

git clone --branch Feature/IS311/Gamitude_void_command_recognition https://github.com/slakerZ/gamitude-web.git --single-branch repositories/gamitude-web
git clone https://github.com/slakerZ/gamitude-backend.git repositories/gamitude-backend