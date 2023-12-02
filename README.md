# learning-bot-creation
this is a small as possible project written in a "mess around" manner to learn how to make bots with python

Dispatcher is the main router, they are needed for handling incoming updates from Telegram
- Routes are a way to process events
- Routes has some specified events they can handle, as depicted below  
![image](https://github.com/KidPudel/learning-bot-creation/assets/63263301/3abed1ae-a5f5-45eb-aded-ee43a4327d29)

# event handlers
[event handlers](https://docs.aiogram.dev/en/dev-3.x/dispatcher/router.html)  
[official docs](https://core.telegram.org/bots/api#august-18-2023)

the order is metter

# methods
https://docs.aiogram.dev/en/dev-3.x/api/methods/index.html

# filters
[filters](https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/command.html) are for events (updates) to be routed to the specific handler that match filter set.  
Searching filters is always stops on first match set of filters are passed (empty filters are always passses, so **the order is matter**) . By defauilt all updates has empty filter set, so all updates will be passed to the handler that has no filters
