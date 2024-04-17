import subprocess
import argparse
import threading


def append(inputs, output):
    command = ['ffmpeg',
               '-y',]
    
    print(inputs)
    filter = ""
    for index, input in enumerate(inputs):
    	command += '-i', input
    filter += "concat=n="+str(len(inputs))+":v=1:a=1"
    
    command += ['-filter_complex',
                filter,
               ]

    command.append(output)

    print(command)

    s = subprocess.Popen(command, stdin=subprocess.PIPE)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', nargs='+', help='List of inputs', required=True)
    parser.add_argument('-o', '--output', default="cuts/output.avi", type=str)
    args = parser.parse_args()

    append(args.input, args.output)
