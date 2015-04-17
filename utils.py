"""
this file is GPLv3

original author Biel Bestué de Luna
"""
import os
import errors

def dir_exist_or_GTFO( directory ):
    """check if the folder exists and is a folder itself"""
    if os.path.exists( directory ) == False:
        errors.GTFO_ERROR("directory '%s' doesn't exists" % ( directory ))
    if os.path.isdir( directory ) == False:
        errors.GTFO_ERROR("*directory* '%s' is not a directory" % ( directory ))

def reduce_white_spaces( string ):
    """for every group of white spaces reduce the ammount of white spaces to one"""
    new_string = []
    working_string_groups = []
    working_string = []

    # detect whitespaces
    whitespace = False
    for c in string:
        if c == " ":
            if whitespace == False:
                whitespace = True
                working_string_groups.append( ''.join( working_string ) )
        else:
            if whitespace == True:
                whitespace = False
                working_string_groups.append( ''.join( working_string ) )

        working_string.append( c )
    working_string_groups.append( ''.join( working_string ) ) #last part

    # substitute groups of whitespaces by a single one
    for group in working_string_groups
        if group[0] == " ":
            new_string.append(" ")
        else:
            new_string.append(group)

    # flush those 
    working_string_groups = []
    working_string = []    

    return ''.join( new_string )

def clear_comments( lines ):
    """erase the comments out of the file content"""
    no_coment_lines = []
    working_line = []
    working_group = []

    asterisk = False

    for line in lines:
        breakncontinue = False
        slash = False
        second_asterisk = False
        working_group = [] #flushed
        working_line = [] #flushed
        for c in line:
            if c == "*":
                if asterisk == True:
                    second_asterisk = True
                else:
                    asterisk = True
                    working_line.append( ''.join( working_group ) )
                    working_group = [] #flushed

            elif c == "/":
                if second_asterisk == True:
                    working_group = [] #flushed
                elif slash == False:
                    slash = True
                    working_line.append( ''.join( working_group ) )
                    working_group = [] #flushed
                elif slash == True:
                    slash = False
                    working_group = [] #flushed
                    breakncontinue = True
                    break # breaks out of the character loop
            else:
                if slash == True:
                    slash = False
                    working_line.append( ''.join( working_group ) )
                    working_group = [] #flushed

            working_group.append( c )

        if breakncontinue:
            continue # continues the lines loops
       
        no_coment_lines.append( ''.join( working_line ) )

    return no_comment_lines

    
        

