#!/bin/bash

mkdir -p buildozer
rm -rf buildozer/src
cp setup.py buildozer
cp -r src/ buildozer
cp -r ../feedreader-base/src/ buildozer/
cp buildozer.spec buildozer
cd buildozer
buildozer android debug deploy run