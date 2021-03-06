"""
this file is GPLv3

original author Biel Bestué de Luna
"""

"""
structure of a def

several instances of:

return_type name {
    *several types of data dependant of the return type*
}

"""
import os
import utils

class entity_context:
    ENTITIES_DEF_PATH = ""
    EXTENSION = ""
    
    def __init__( game_context, ent_dir="def", extension="def" )
        ent_path = os.path.join( game_context.GAME_DIR, ent_dir )
        utils.dir_exist_or_GTFO( ent_path )
        self.ENTITIES_DEF_PATH = ent_dir
        self.EXTENSION = os.extsep + extension

    def get_list_of_entities(context):
        l_relevantfiles = []

        for f in os.listdir( ENTITYPATH ):
            if f.endswith( EXTENSION ):
                l_relevantfiles.append(f)

        for f in l_relevantfiles:
            #extract list of entities
    
