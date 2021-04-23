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


# MVP  

## Simulation Flow  
    
### 1. Create Simulation  
  
create_citizens function 

Citizen Initialisation 

- `Id` = uniqueValue (use random name generator so can be in json and prevent duplicates)
- `status_points` = random(0,100)
- `create_gossip_probability` = random int 0-100
- `spread_gossip_probability` = random int 0-100
- `age` = 0
- `friends` = empty
- `subjective_rumour_tracker` empty

### 2. Subjective Rumour Tracker 

- `Action: [created, spreaded]`
- `rumour: [id]`
- `target: [id]`
- `associated: [id]`

### 3. Objective Rumour Database 

- `rumour: [id]`
- `target: [id]`
- `rumour: string`
- `risk: int[0,2000]`
- `persistence: int(-1,1)`
- `associated: [id]`


### 4. Simulate Citizen

- Time Ticks an increment
- Each Person processes a move
- If user rumour creation Value * randint(0-50) > 100 create rumour

### 5. Simulate Environment

- After given time increment end round
- Kill rumours below a certain persistence
- Kill citizen if below a certain status point
- Kill citizen if above a certain age 

- After certain time increment inject new citizens




(will need to remove a given rumour from everyone if it dissapears.... or just stop it propagating)






**All Things below are the full features to be considered**  





## SOE

- Create Versions
- MVP
- Pygame

## Considerations Features

- Include end-of-day review?  
- Friendly fire
- Guilt by association

Objectives
-----------

Simulate Gossip Utility in Society


[-10] did you know ID is having an affair with ID 
[]

## Main Attributes

Status-Points

ID Names

Age



### STRETCH Atrributes (may not be implemented)

- Stimululus/happiness index (non-spreader)


## Archetypes 

- Creator of rumour
- Peristor of rumour 
- Target of Rumour [take statuspoint damage/benefit for rumour value.]
- Non-participant



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