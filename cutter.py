import subprocess

# Command and params for ffmpeg
command = ['ffmpeg',
           '-i', "/home/laura/supervisionsportclub/records/24-03/XCOUTFY_2024-03-24_12-43-29CAM_280800.avi",
           '-c:a', 'copy',
           '-c:v', 'copy',
           '-ss', '01:03:45',
           #'-to', '02:08:00',
           'cuts/teste.avi',
           ]

# Using subprocess and pipe to fetch frame data
s = subprocess.Popen(command, stdin=subprocess.PIPE)
