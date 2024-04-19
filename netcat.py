import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)
    return output.decode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BHP Netcat Tool',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''Example:
                                                            netcat.py -t IP -p PORT -l -c # command shell
                                                            netcat.py -t IP -p PORT -l -u=test.txt # upload file
                                                            netcat.py -t IP -p PORT -l -e=\"cat /etc/passwd\" # execute command
                                                            echo 'TEST' | ./netcat.py -t IP -p PORT # echo text to server port
                                                            netcat.py -t IP -p PORT # connect to listener
                                                        '''))
    parser.add_argument
                                     
                                    


