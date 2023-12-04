# learning-bot-creation
this is a small as possible project written in a "mess around" manner to learn how to make bots with python

Dispatcher is the main router, they are needed for handling incoming updates from Telegram
- Routes are a way to process events
- Routes has some specified events they can handle, as depicted below  
![image](https://github.com/KidPudel/learning-bot-creation/assets/63263301/3abed1ae-a5f5-45eb-aded-ee43a4327d29)

# event handlers
[event handlers](https://docs.aiogram.dev/en/dev-3.x/dispatcher/router.html)  
[official docs](https://core.telegram.org/bots/api#august-18-2023)
## process of handling
1. looking through current router (from outter -> nested) first is Dispatcher
2. in router looking sequentially, from top to bottom (the first that satisfy filters (non-filtered handler is always the strongest))
the order is matter

# methods
https://docs.aiogram.dev/en/dev-3.x/api/methods/index.html

# filters
[filters](https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/command.html) are for events (updates) to be routed to the specific handler that match filter set.  
Searching filters is always stops on first match set of filters are passed (empty filters are always passses, so **the order is matter**) . By defauilt all updates has empty filter set, so all updates will be passed to the handler that has no filters

# state machine
when you need to do some steps and determine on what bot message user is responding to

This is done with a StateGroup, just define a states, to determine what step is now and what user must enter
(like with enum group), just set state and then in a filters of a handler add needed state
[fine-state-machine](https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html)
