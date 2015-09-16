#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition
inquisition.SPANISH.index("Spanish")
FLEMISH = (inquisition.SPANISH[0:18]
           + inquisition.SPANISH[19:27].replace("Spanish", " Flemish")
           + inquisition.SPANISH[27:418])
