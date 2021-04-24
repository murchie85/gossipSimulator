"""
# Program Name: spread_gossip
# Author: Adam McMurchie
# DOC: 24 April 2021
# Summary: This program transfers gossip info to subjective gossip data
#          by appending a new dict
# ***********ALL STATE IS STORED HERE******************
#


| Object                      | Values |
| ----------- | ----------- |
| **gossipID (key)**              | `string( int(value) )` value increments |
| **creator**                     | [citizen_list]name (Pkey) |
| **target**                      | [citizen_list]name (Pkey) |
| **sentiment** | `random(0,100)` |
| **rumour**                      | `string` |
| **risk**                        | `random(0,100)`|
| **persistence**                 | `random(0,100)` |
| **spread_count**              | `int(value)`value increments |
| **associated_citizens**         | initialised as `random(0,1000)` |
"""


## assumes user is there
def spreadGossip(gossipID,):
