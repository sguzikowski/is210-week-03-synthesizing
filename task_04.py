#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {0}! I have {1} news! I won the raffle with number 0000{2}!'
#CHANGED "{friend} to 0, {0} to 1, and  {1} to 2 because "Key Errors"
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42

EMAIL = NEWS.format(FNAME, NTYPE, RNUM)
