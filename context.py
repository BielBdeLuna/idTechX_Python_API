"""
this file is GPLv3

original author Biel Bestué de Luna
"""

"""
    this file defines the working context of the game including: the base, a base_mod, and a mod
"""
import utils
import sys

class game_context:
    """establishes a context for the whole game"""
    GAME_DIR = ""
    BASE_DIR_NAME = ""
    BASE_MOD_DIR_NAME = ""
    MOD_DIR_NAME = ""

    OS = ""
    ARCH = "" #TODO for multi-threaded works

    def __init_( path, reldir="base" ):
        """establishes the path where the game executable resides\nand also establishes the base directory name, usually named: 'base'"""
        utils.dir_exist_or_GTFO( path )
        utils.dir_exist_or_GTFO( reldir )       
        self.GAME_DIR = path
        self.BASE_DIR_NAME = reldir
        self.OS = sys.platform
        #self.ARCH = sys.

    def set_base_mod_dir_name( reldir ):
        """sets a base mod dir name for the context, example: 'd3xp'"""
        utils.dir_exist_or_GTFO( reldir )
        self.BASE_MOD_DIR_NAME = reldir
    
    def set_mod_dir_name( reldir ):
        """sets a mod dir name for the context"""
        utils.dir_exist_or_GTFO( reldir )
        self.MOD_DIR_NAME = reldir

