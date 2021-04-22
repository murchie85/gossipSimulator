# Gossip Simulator 

## Building Digital Fishwives 


![](https://cf.girlsaskguys.com/q3478164/primary-share.png?33)

In Yuval Harai's pivotal book [Sapiens](https://www.ynharari.com/book/sapiens-2/) the author explains how Story Telling and collective belief define the human race. In fact these uniquely human characteristics may have helped differentiate Sapiens from their historical competitors and allowed us to thrive into the technological society we have today. 

In this project I (Adam McMurchie) plan to build a series of bots which will simulate how a world will evolve overtime via a colection of rules which defines risks and rewards of rumour creation. These rules will be set at three tiers, environmental level, social level and household level. 

 Dumb rules based optimisers will play part of the relatively disengaged population who partake in occasional gossiping. 

 The Digital Fishwife: will be AI optimisers designed with two main optimisers in consideration:

 - Propagate Rumours
 - Gain Status by generating Rumors

 This may seem like the same thing, but one AI Optimiser will be tasked with keeping a rumour going and spreading it to as many people as possible. 

Another optimiser will be tasked with gaining as much points by abusing the system to their benefit (it might not mean spreading it far and wide).



Objectives
-----------

Simulate Gossip Utility in Society



## Main Attributes

Status-Points

ID Names

Age


## Archetypes 

- Creator of rumour
- Peristor of rumour 
- Target of Rumour [take statuspoint damage/benefit for rumour value.]



- Instigator function

Can create rumour about one or multiple targets

negative rumour positive-status-points positive-risk	

- Speader function

- Target

Is affected by a rumour 



## Bot Behaviour

- creator boolean on/off
- Spreader boolean on/off



## AI Optimisers

1. Spread rumour as far and wide as possible and/or to get it to last forever [AI DAVE]
2. Selfish create rumour to gain status points. [AI BOB]
3. Generic optimizer - looks for trends and copies the most succesful



Rules
-----------------


Environment has a time engine. 

Rumour can be created

Rumour can be positive or negative (in terms of impact to targ)

Rumour has a shelf life (value decreases to 0)

Too much Rumour creation lowers the value of a rumour. 


creating a rumour can gain you status-points
creating a rumour can dock you status-points [function of risk]




## Application Design
-----------------

## Functions 

- `create_rumour.py` 
- `modify_rumour.py`
- `create_citizen.py`
- `modify_status_points.py`

## Objects 

- `rumour_object`
-   `rumour_instegation_counter`
- 	`rumour_persistence` success means trending to 1. Failure means trending to 0. 
- 	`rumour_points` how much points a rumour is worth 
- 	`rumour_environment_multiplier` too many rumours reduce this value.
- 	`rumour_replication_multiplier` more people = higher rumour value

## Databases 

Rumour Database 

Time Function 




## Additional Resources

1. [sapienship](https://www.sapienship.co/activities/storytelling)