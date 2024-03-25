import subprocess
import argparse


def cut(input, output, start, end):
    command = ['ffmpeg',
               '-y',
               '-i', input,
               '-c:a', 'copy',
               '-c:v', 'copy',
               '-ss', start,
               ]

    if end:
        command += '-to', end

    command.append(output)

    print(command)

    s = subprocess.Popen(command, stdin=subprocess.PIPE)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-o', '--output', default="cuts/output.avi", type=str)
    parser.add_argument('-s', '--start', default="00:00:00.00", type=str)
    parser.add_argument('-e', '--end', default=None, type=str)
    args = parser.parse_args()

    cut(args.input, args.output, args.start, args.end)
