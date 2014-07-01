#! /usr/bin/env python3

import geldrausssch.geldrausssch_gui
import os

# GO TO EXECUTING DIRECTORY
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# CREATE INSTANCE
app = geldrausssch.geldrausssch_gui.GeldRauSSSch()
app.run()
