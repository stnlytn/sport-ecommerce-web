#!python3
# -*- coding:utf8 -*-
# builtin modules
import re
import sys
import time
import json
import pprint
import pathlib
import logging
import argparse
from os.path import realpath, dirname, join
from typing import Dict, List

# third party module
import boto3
import requests
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)