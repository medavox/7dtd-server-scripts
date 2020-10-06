from telnetlib import Telnet
#import schedule
import time
import sys


#chunkcache cc => shows all loaded chunks in cache
#gettime gt => Get the current game time
#kickall => Kicks all users with optional reason. "kickall reason"
#listplayers lp => lists all players
#listplayerids lpi => Lists all players with their IDs for ingame commands
#listthreads lt => lists all threads
#loglevel => Telnet/Web only: Select which types of log messages are shown
#mapdata => Writes some map data to an image
#mem => Prints memory information and unloads resources or changes garbage collector
#pplist => Lists all PersistentPlayer data
#profilenetwork => Writes network profiling information
#saveworld sa => Saves the world manually.
#say => Sends a message to all connected clients
#shutdown => shuts down the game
#version => Get the currently running version of the game and loaded mods

"""


I don't want to be partly responsible for poor self-care,
by leaving the server running all hours.
There's a reason that most pubs close for the night,
and so should the server.

at 0230, 0245, 0255 and 0259:
if the server is running, run the expect script

the expect script:
    log in using the password stored in a file
    run 'lp'
    if the playercount is 0,
        shutdown immediately
    else
        execute the particular thing:
            say the next part of the scripted text
            or actually do `kickall` then `shutdown`

"""

def say_or_shutdown(tn, msg):
    tn.write(b"listplayers\r")
    playersResult = tn.expect([b"Total of 0 in the game"], 3)
    if playersResult[0] == -1 and playersResult[1] == None:
        tn.write(b'say "' + msg + b'"\r')
    else:
        tn.write(b"say Server is empty, shutting down immediately...\r")
        tn.write(b"shutdown\r")



try:
    #2am, 2.30, 2.45, 2.55, 2.59, 30 seconds, 10 seconds
    with Telnet("192.168.1.69", 1989) as tn:
        tn.write(b"shebshapaya\r")
        #midnight
        say_or_shutdown(tn, b"NOTICE: the server will automatically shut down at 3am")
        time.sleep(7200)
        #2am
        say_or_shutdown(tn, b"the server will be shutting down in an hour, at 3am")
        time.sleep(1800)
        #02:30
        say_or_shutdown(tn, b"Alright, last orders you lot! Haven't you got beds to get to?")
        say_or_shutdown(tn, b"(server is shutting down for the night in 30 minutes, at 3am)")
        time.sleep(900)
        #02:45
        say_or_shutdown(tn, b"Server is shutting down in 15 minutes, at 3am")
        time.sleep(600)
        #02:55
        say_or_shutdown(tn, b"Server is shutting down in 5 minutes!")
        time.sleep(240)
        #02:59
        say_or_shutdown(tn, b"Server is shutting down in 1 minute!!")
        time.sleep(30)
        say_or_shutdown(tn, b"30 seconds till server shutdown!!!")
        time.sleep(20)
        say_or_shutdown(tn, b"10 seconds. This is your last warning! Goodnight!")
        time.sleep(10)
        tn.write(b'kickall "Go the fuck to sleep"\r')
        tn.write(b"shutdown\r")
except ConnectionRefusedError as cre:
    sys.exit()