from subprocess import call
import time

try:
    while True:
        call(['mpv', 'alaram-beep.wav'])
except KeyboardInterrupt:
    print('ok!')
    time.sleep(3)
    print('getting out of except')
print('end')
time.sleep(10)
