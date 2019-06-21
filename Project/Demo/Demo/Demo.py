# Author:      Li Leo Wang
# Start Date:  2019-06-19
# Description:
#      - A test harness for temporary trying out code.
# Notes:
#      - (none)
#
# Change history:
#      - Refer to GitHub comments related to each source file.
#

import sys
import socket_server

def main():
    socket_server.Run()
    input('\nEnd')

if __name__ == "__main__":
    sys.exit(int(main() or 0))
