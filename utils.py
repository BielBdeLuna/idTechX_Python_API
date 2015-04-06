"""
this file is GPLv3

original author Biel Bestué de Luna
"""
import os
import errors

def dir_exist_or_GTFO( directory ):
    """check if the folder exists and is a folder itself"""
    if os.path.exists( directory ) == False:
        errors.GTFO_ERROR("directory '%s' doesn't exists" % ( msg ))
    if os.path.isdir( directory ) == False:
        errors.GTFO_ERROR("*directory* '%s' is not a directory" % ( msg ))

