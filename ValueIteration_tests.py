"""
((.venv) ) python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2

RUNNING 1 EPISODES

BEGINNING EPISODE: 1

Started in state: (1, 1)
Took action: west
Ended in state: (1, 0)
Got reward: 0.0

Started in state: (1, 0)
Took action: exit
Ended in state: TERMINAL_STATE
Got reward: -100

EPISODE 1 COMPLETE: RETURN WAS -90.0


AVERAGE RETURNS FROM START STATE: -90.0

((.venv) ) python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.0

RUNNING 1 EPISODES

BEGINNING EPISODE: 1

Started in state: (1, 1)
Took action: east
Ended in state: (2, 1)
Got reward: 0.0

Started in state: (2, 1)
Took action: east
Ended in state: (3, 1)
Got reward: 0.0

Started in state: (3, 1)
Took action: east
Ended in state: (4, 1)
Got reward: 0.0

Started in state: (4, 1)
Took action: east
Ended in state: (5, 1)
Got reward: 0.0

Started in state: (5, 1)
Took action: east
Ended in state: (6, 1)
Got reward: 0.0

Started in state: (6, 1)
Took action: exit
Ended in state: TERMINAL_STATE
Got reward: 10

EPISODE 1 COMPLETE: RETURN WAS 5.904900000000001


AVERAGE RETURNS FROM START STATE: 5.904900000000001

((.venv) ) python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.0 --noise 0.2

RUNNING 1 EPISODES

BEGINNING EPISODE: 1

Started in state: (1, 1)
Took action: north
Ended in state: (1, 2)
Got reward: 0.0

Started in state: (1, 2)
Took action: exit
Ended in state: TERMINAL_STATE
Got reward: -100

EPISODE 1 COMPLETE: RETURN WAS 0.0


AVERAGE RETURNS FROM START STATE: 0.0

((.venv) ) python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.2 --noise 0.2

RUNNING 1 EPISODES

BEGINNING EPISODE: 1

Started in state: (1, 1)
Took action: west
Ended in state: (0, 1)
Got reward: 0.0

Started in state: (0, 1)
Took action: exit
Ended in state: TERMINAL_STATE
Got reward: 1

EPISODE 1 COMPLETE: RETURN WAS 0.2


AVERAGE RETURNS FROM START STATE: 0.2

((.venv) ) python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.9

RUNNING 1 EPISODES

BEGINNING EPISODE: 1

Started in state: (1, 1)
Took action: north
Ended in state: (2, 1)
Got reward: 0.0

Started in state: (2, 1)
Took action: north
Ended in state: (3, 1)
Got reward: 0.0

Started in state: (3, 1)
Took action: north
Ended in state: (2, 1)
Got reward: 0.0

Started in state: (2, 1)
Took action: north
Ended in state: (3, 1)
Got reward: 0.0

Started in state: (3, 1)
Took action: north
Ended in state: (4, 1)
Got reward: 0.0

Started in state: (4, 1)
Took action: north
Ended in state: (5, 1)
Got reward: 0.0

Started in state: (5, 1)
Took action: north
Ended in state: (4, 1)
Got reward: 0.0

Started in state: (4, 1)
Took action: north
Ended in state: (5, 1)
Got reward: 0.0

Started in state: (5, 1)
Took action: north
Ended in state: (6, 1)
Got reward: 0.0

Started in state: (6, 1)
Took action: exit
Ended in state: TERMINAL_STATE
Got reward: 10

EPISODE 1 COMPLETE: RETURN WAS 3.8742048900000015


AVERAGE RETURNS FROM START STATE: 3.8742048900000015
"""