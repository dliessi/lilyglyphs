#!/usr/bin/env python

# ########################################################################
#                                                                        #
#      This file is part of the 'lilyglyphs' LaTeX package.              #
#                                ==========                              #
#                                                                        #
#              https://github.com/uliska/lilyglyphs                      #
#                                                                        #
#  Copyright 2012 by Urs Liska, lilyglyphs@ursliska.de                    #
#                                                                        #
#  'lilyglyphs' is free software: you can redistribute it and/or modify  #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation, either version 3 of the License, or     #
#  (at your option) any later version.                                   #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#                                                                        #
# ########################################################################

# ########################################################################
#                                                                        #
# genGlyphCommands.py                                                    #
#                                                                        #
# generate commands based on Emmentaler glyphs                           #
#                                                                        #
# ########################################################################

import os, sys
import lib.common as lg, lib.globals as gl
from lib.inputfilegeneric import InputFileGeneric
from lib.latexfile import LatexFile

def main(input_file):
    lg.check_lilyglyphs_root(gl.D_STASH)
    gl.D_DEFS = gl.D_STASH
    # load file with command definitions,
    # parse it and generate LaTeX commands file
    def_file = InputFileGeneric(input_file)

    # load file from disk
    def_file.load()

    # parse the file and generate the Commands entries
    def_file.read_entries()

    # generate the contents of a LaTeX file from the Command entries.
    def_file.generate_latex_file()

    # write out the LaTeX file to disk
    def_file.write_latex_file()

def usage():
    print 'genGlyphCommands.py'
    print 'is part of the lilyglyphs package'
    print ''
    print 'Usage:'
    print 'Pass the name (without path) of an input definitions file'
    print '(this has to be located in the /stash_new_commands directory.'
    print 'Please refer to the manual (documentation/lilyglyphs.pdf).'


# ####################################
# Finally launch the program
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'No filename argument given.\n'
        usage()
        sys.exit(2)
    main(sys.argv[1])