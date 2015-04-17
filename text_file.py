import utils

class text_file:
    lines = []

    def gather_lines_from_file( filename ):
        with open(filename) as f:
            lines = f.readlines()
        self.lines = lines

    def discard_lines_from_file():
        correct_lines = []

        comment = False
        asterisk = False
        data_in_that_line = True

        for l in lines:
            interpreted_line = []
            working_chars = []
            last_char = ""
            i = 0
            data_in_that_line = True
            if comment == True:
                data_in_that_line = False
                

            for i in range(0, len(l)):
                c = l[i]
                if c == "/"
                    if l[i + 1] == "/"
                    if i == 0
                        data_in_that_line = False
                    comment = True

                i = i + 1

            if comment == False and data_in_that_line == True:
                correct_lines_string = ''.join(correct_lines)
                correct_lines.append(correct_lines_string)
                    
            

        self.lines = correct_lines

    def __init__( filename )
        gather_lines_from_file( filename ) 
        discard_lines_from_file()
