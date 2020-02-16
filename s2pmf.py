""" s2pmf.py
    
    Usage:
        s2pmf.py -h
        s2pmf.py <required> [-i]

    Options:
        -h,--help       : show this help message
        -i,--input      : file input path
        -l,--loop       : number of loops
        -p,--percentage : percentage speed increase per loop

"""

import ffmpeg
import subprocess
from docopt import docopt
from multiprocessing import Process, Lock

def speed_up(input_file, percentage):
    input = ffmpeg.input(input_file)
    speed = input.audio.filter("atempo", percentage)
    output = ffmpeg.output(speed, 'output.mp3')
    ffmpeg.run(output)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
    # speed_up(arguments['<required>'], arguments['--percentage'])
    # subprocess.call(["ffplay", "-nodisp", "output.mp3"])