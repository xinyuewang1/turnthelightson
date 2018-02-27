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
    totl.main('tests/input_assign3_b_v2.txt')