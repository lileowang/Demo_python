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
import socket_client

def main():
    
    # test socket: 
    # - run server first: ctrl + F5
    # - then run client: ctrl + F5
    # - monitor with: netstat -an | find "5151"
    #socket_server.Run()
    socket_client.Run()

    input('\nEnd')

if __name__ == "__main__":
    sys.exit(int(main() or 0))
