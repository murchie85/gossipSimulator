#               Gossip Simulator

![](sprites/concept/Noseytown.png)

In Yuval Harai's pivotal book [Sapiens](https://www.ynharari.com/book/sapiens-2/) the author explains how Story Telling and collective belief define the human race. In fact these uniquely human characteristics may have helped differentiate Sapiens from their historical competitors and allowed us to thrive into the technological society we have today. 

![](https://cf.girlsaskguys.com/q3478164/primary-share.png?33)

## Building Digital Fishwives 

In this project I (Adam McMurchie) plan to build a series of bots which will simulate how a world will evolve overtime via a colection of rules which defines risks and rewards of rumour creation. These rules will be set at three tiers, environmental level, social level and household level. 

 Dumb rules based optimisers will play part of the relatively disengaged population who partake in occasional gossiping. 

 The Digital Fishwife: will be AI optimisers designed with two main optimisers in consideration:

 - Propagate Rumours
 - Gain Status by generating Rumors

 This may seem like the same thing, but one AI Optimiser will be tasked with keeping a rumour going and spreading it to as many people as possible. 

Another optimiser will be tasked with gaining as much points by abusing the system to their benefit (it might not mean spreading it far and wide).



# Objectives
-----------

1. Simulate Gossip Utility in Society
2. Create a world with bots and AIs who interact and talk 
3. Observe how rumours can be used to increase status points. 


# MVP  
-----------------

## Rules
 

- Environment has a time engine. 
- Rumour can be created
- Rumour can be positive or negative (in terms of impact to target)
- Rumour can be about one or multiple targets. Even about no targets.
- Rumour has an associated risk. 
- Rumour has a shelf life/popularity (value decreases to 0)
- Rumours will be associated to citizens who spread or create it.

Too much Rumour creation lowers the value of a rumour. 


creating a rumour can gain you status-points
creating a rumour can dock you status-points [function of risk]


## Citizen Archetypes 

You get four main different types of people. 

- Creator of rumour
- Peristor of rumour 
- Target of Rumour [take statuspoint damage/benefit for rumour value.]
- Non-participant


## Core Citizen Attributes

- Status-Points
- ID Names
- Age


# OBJECTS
-------------


## Citizen 

Initialisation 

- `Id` = uniqueValue (use random name generator so can be in json and prevent duplicates)
- `status_points` = random(0,100)
- `create_gossip_probability` = random int 0-100
- `spread_gossip_probability` = random int 0-100
- `age` = 0
- `friends` = empty
- `subjective_rumour_tracker` empty

#### 2. Subjective Rumour Tracker 

- `Action: [created, spreaded]`
- `rumour: [id]`
- `my_associated: [id]`

## 3. Objective Rumour Database 

- `rumour: [id]`
- `target: [id]`
- `sentiment: int(-1,1)`
- `rumour: string`
- `risk: int[0,2000]`
- `persistence: int(0,100)`
- `associated_citizens: [id]`

# Functions 
--------------------
  
## create_citizens function   


## create_rumour_function

- Can only create a rumour when in contact with one or more people. 







## Utils 

# Simulation Flow
--------------------

1. Initialise Citizens 
2. Intialise rumour db
3. Tick Time increments


| Step        | Requirements |
| ----------- | ----------- |
| Initialise Citizens      | `create_citizen.py`       |
| Initialise Rumour DB   | `create_rumour_db.py`        |

    
### 1. Create Simulation  

### 2. Simulate Citizen

- Time Ticks an increment
- Each Person processes a move
- If user rumour creation Value * randint(0-50) > 100 create rumour

### 3. Simulate Environment

- After given time increment end round
- Tick down rumour popularity rating
- Kill citizen if below a certain status point
- Kill citizen if above a certain age 

- After certain time increment inject new citizens




**All Things below are the full features to be considered**  





# Feature BackLog
--------------


- Include end-of-day review?  
- Create Versions
- MVP
- Pygame
- Friendly fire
- Guilt by association

## STRETCH Atrributes (may not be implemented)

- Stimululus/happiness index (non-spreader)











- Instigator function



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
-   `rumour_id`
-   `target_citezen` (could be null)
-   `rumour_instegation_counter`
- 	`rumour_persistence` success means trending to 1. Failure means trending to 0. 
- 	`rumour_points` how much points a rumour is worth 
- 	`rumour_environment_multiplier` too many rumours reduce this value.
- 	`rumour_replication_multiplier` more people = higher rumour value

- `citizen_object`
-   `create_gossip_probability`
-   `spread_gossip_probability`
- 	`all_known_rumours`
- 	`known citizen list` / `friends`
- 	`rumour_tracker`
-		`who told who this rumour` (stretch goal - to contain ID)
- historical tracker over time 

## Databases 

Rumour Database 

Time Function 


## Risk 

Rumour can backfire if boring
Rumour can backfire if 
Creating gossping about a high status point person increases risk (top 70-95%)
Gossping about top 95-100% is fun, doesn't generate much status points or risk. 


Retaliation 

## Ideal Features

- Visualise it in a game format 
- Visualise it in a datapipeline 


## Environment 

to get it going, just create rumours with any other id != self

Stretch

Location 
move about
can only create rumour or spread rumour or recieve rumour if x < 10 meters of another citizen 

Environment locations affect rumour score

office X2 
home x1
dock street -x1
Neutral Location scores: 


## Additional Resources

1. [sapienship](https://www.sapienship.co/activities/storytelling)