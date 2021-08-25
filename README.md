# LOCAL-IP-TextMessaging-Python-Scripts
Python scripts for a local WLAN IP based text messaging service with additional packet loss testing functionaliy and a detailed bit by bit ACK analysis

## Description

In this project, two computers (although 2+ computers can be daisy chained for advanced functionality) can communicate with each other as long as they're connected to the same WLAN/LAN network. IP address of each terminal is required to establish the connection. Has the functionaity to simulate packet loss for testing purposes. ACK check is implemented as a part of such a feature.

## How to run
ackClient and ackServer both need to be launched on both of the communicating computers for functionality. For simplicity lets name the computers "Lana" and "Dana".

Server Lana needs to launched before Client Dana can be run and vice-versa.
Server, when laucnhed actively searches for incoming connections from the same LAN. Client Dana is launched and asks for the server IP. Here we input ip "Lana"
Client Lana is launched and is connected to Server Dana by inputting the IP
Client Dana establishes a connection with Server Lana, and vice versa. The connections are acknowledged on both of the servers. Now we decide the the TCP window size and packet loss parameters (if required)
Messages can be sent both back and forth

## Packet Loss Testing

ACK stats of each bit transferred are shown during the process. ACK Loss is shown in case of simulated packet loss. In this case, the Client tries to resend the lost bit until Server acknowledges the bit as fully recieved. All the parameters on PAcket Loss are fully tunable in case the user doesnt want to test the Packet Loss functionality

## Future

A Windows graphical user interface (GUI) is in works for simple automation of the basic procedure to get this platform running. It's simpler, looks nicer and is more user friendly
