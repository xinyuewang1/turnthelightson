#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `totl` package."""

import pytest
from totl import turnOnTheLight
from totl.lightTester import LightTester

def test_light():
    test = LightTester(3)
    #print(test.lights,test.count())
    test.apply('turn on',0,0)
    assert test.count()==1
    
    test.apply('turn off',0,0)
    assert test.count()==0
    
    test.apply('switch',0,0)
    assert test.count()==1
    #print(test.lights)

def test_size():
    test = LightTester(3)
    assert test.size() == 3
     
def test_readIns():
    #Open and read the file
    #assert totl.main('tests/test1')
    #assert totl.main('tests/test1') == 'h'
    #assert totl.main('tests/test1') == 'turn off 0,0 through 4,4'
    #assert totl.main('tests/test1')==1
    #assert turnOnTheLight.main('tests/test1')==7
    #assert turnOnTheLight.main('tests/input_assign3_b_v2.txt') < 10000
    #assert turnOnTheLight.main('tests/test2') == 0
    
    #existence of the input file
    assert turnOnTheLight.main('../tmp.txt') == None
    
    