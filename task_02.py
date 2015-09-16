#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

#Using .replace() and re() aren't the only ways to
#replace values in a string. This task will challenge
#you to use a combination of .index(), slicing, len(),
#and concatenation, you can achieve the same effect.

import inquisition

beep = inquisition.SPANISH #gets quote
boop = len(beep) # gives number (418)
first = beep[0:78] #slice
second = beep[79:159] #slice
third = beep[160:239] #slice
fourth = beep[240:320] #slice
fifth = beep[321:400] #slice
sixth = beep[401:418] #slice


find = "Spanish";
beep.index(find) #prints 19
this = beep[19:27] #picks out the word spanish
that = this.replace("Spanish", " Flemish")

first = beep[0:18]
second = that
third = beep[27:418]

FLEMISH = first + second + third
