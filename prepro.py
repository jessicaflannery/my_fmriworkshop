#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 07:54:17 2017

@author: jessicaflannery
"""


import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
    print('Hello data in the path' +basedir)
    
def main():
    basedir='/Users/jessicaflannery/Desktop/fMRI reporducibility workshop/data/'
    prepro(basedir)
    
    
main()