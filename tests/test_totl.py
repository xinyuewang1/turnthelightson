#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `totl` package."""

import pytest
from totl import totl

def test_light():
    test = totl.lightTester(3)
    #print(test.lights,test.count())
    test.apply('turn on',0,0)
    assert test.count()==1
    
    test.apply('turn off',0,0)
    assert test.count()==0
    
    test.apply('switch',0,0)
    assert test.count()==1
    #print(test.lights)

def test_readIns():
    #Open and read the file
    #assert totl.main('tests/test1')
    #assert totl.main('tests/test1') == 'h'
    #assert totl.main('tests/test1') == 'turn off 0,0 through 4,4'
    #assert totl.main('tests/test1') == 1
    