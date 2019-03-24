## Python CTypes Interface to ISDA CDS model

ISDA_Clib.dll is the x64 windows DLL built from ISDA C sources, you must use 64-bit python 3.x. See my ISDA_CLib git repo for the complete VS 2017 solution to build the dll from sources.

c_interface.py contains the ctypes function and type declarations to the functions exported from the above dll

cds_trade.py is where you define your CDS deal attributes and the par spreads for that refob for that date

isda_model.py calls functions from c_interface.py

isda_model_test.py is a one CDS test with results

market_data.py is where you enter your zero rates (deposits and swaps)

utils.py is a helper functions file


