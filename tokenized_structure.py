"""
this file is GPLv3

original author Biel Bestué de Luna
"""

"""
most of the game data in idTechX is tokenized in that maner:

return_type name {
    *several types of data dependant of the return type*
}

so let's devise a way to read this
"""

#import utils
"""
def gather_braketed_data( string, start_line, index ):

def gather_next_token_in_line( string, start_line, index ):
    line_string = 
    max_len = len(line_string)
    final_index = 0
    error_handling = False

    i = index + 1 #next charactr in line
    while i <= range(0, max_len):        
        if i >> max_len:
            print("no more tokens in that line")
            error_handling = True

        if line_string[i] == " ":
            break

        final_index = i
        i = i + 1

    if line_string != "{":
        if error_handling == False:
            return line_string[index:final_index]
        else:
            return ""
    else:
        return gather_braketed_data( start_line, index )
"""
import utils

def mark_token_groups_line_start( strn ):
    lines = strn.

class tokenized_file:
    token_groups = []

    filename = ""
    contextdata = []

    def gather_tokens():

    def __init__( contextdata, filename )
        self.filename = filename
        self.contexdata = contextdata    

    

class token_data:
    l_return_types = ["entityDef", "model", "particle"]
    l_ommit_return_types = ["export"]
    return_type = ""
    token_name = ""
    l_spawnargs = []
    token_group_string = ""

    def __init__( token_group ):
        self.token_group_string = token_group

    def gather_all_data():
        #check if it's a string at all
        for i in range(0, len(token_group_string)):
            if str[i] == " ":
                

        for c in token_group_string
        first_space_index


class tokenized_return_types:
    l_return_types = ["entityDef", "model", "particle"] #TODO needs more work indeed!
    return_type = ""


class tokenized_name:

class tokenized_data:
    """whatever is inside the brakets"""
    data_type = ""

    def __init__( dtype ):
        self.data_type = dtype.return_type

    def read_data():
        string = ""
    
