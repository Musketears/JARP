#!/bin/sh

nordvpn login --token $NORDVPN_TOKEN
nordvpn connect

cd /JARP
source .venv/bin/activate
python3 jarp.py

# Keep the container running
while true; do sleep 1000; done
