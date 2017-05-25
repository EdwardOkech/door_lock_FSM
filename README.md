A bunch of scripts implementing a keycard lock mechanism using the fsm(finite state machine) mechanism

link to detailed explanation of keycard lock:
https://en.wikipedia.org/wiki/Keycard_lock

link to detailed explanation of fsm:
https://en.wikipedia.org/wiki/Finite-state_machine

        Bussines logic
++++++++++++++++++++++++
1. A card object with user details will try unlock a keycard lock
2. User's has to be still in contract/registered in school (our supposedly implementation environment   is in school/office)
3. If right user door should open


         Model
+++++++++++++++++++++++++++

[user with card] =>    [Inserts card in door]            =>     [if right user door open] => [Doorshuts]
                      (Door should be in lock state)    | |     (Door in unlock state)    (after 5 secs)
                                                        | |
                                                        | |  [If wrong user/card]
                                                         V      (wrong card:contract has ended)
                                                                  (go back to step one)



         How to run script
+++++++++++++++++++++++++++++++
$ clone repo
$ cd door_look_FSM
$ ./main.py 





