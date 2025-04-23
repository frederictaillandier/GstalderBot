# This project is deprecated and replaced with its [RUST version](https://github.com/frederictaillandier/gstaldergeist)





![gstaldergeistlogo-fotor-bg-remover-2023072801149](https://github.com/frederictaillandier/GstalderBot/assets/5926779/95773e06-b210-4486-a8af-e4a2cae75aaa)

# Gstaldergeist

A telegram chatbot to manage a shared house chores

## Install and Use

Fork the repository and set an env variable as : 


`GSTALDERCONFIG_PROD`
as</br>
```json
{
    "open_ai_key": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "bot_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "global_chat_id": "999999999999",
    "flatmates": [
        {"name": "John", "chat_id": "1234567890" },
        {"name": "Thomas", "chat_id": "1234567891"},
        {"name": "Philipp", "chat_id": "1234567892"},
    ]
}
```

using these parameters:
**bot_token** is your [telegram](https://core.telegram.org/bots/api) bot token</br>
**global_chat_id** is the [telegram](https://core.telegram.org/bots/api) grouphttps://github.com/frederictaillandier/gstaldergeist chat where the bot writes for all flatmates</br>
**flatmates** is the list of your flatmates and **chat_it** fits a chat only targeted for a specific flatmate</br>


if a ```config.json``` file was given to you then simply 

```export GSTALDERCONFIG=`cat config.json` ```

and then run with 

```python3 main.py ```

## Production environment

An instance of this project runs on an AWS cloud using: 

![image](https://github.com/frederictaillandier/GstalderBot/assets/5926779/608d4a94-5b03-407a-8be6-58b45ae2b6b8)  AWS Event bridge

![image](https://github.com/frederictaillandier/GstalderBot/assets/5926779/a1c383a0-1070-49f1-a2fc-61dd27425174)  AWS Elastic container service

## TESTS

This project is trying to use the Test Driven Development approach. 
So, in order to run the tests, use:

```tox -e py```

![image](https://github.com/frederictaillandier/GstalderBot/assets/5926779/96835696-8428-4a25-8309-3a1ea17c90b8)
![image](https://github.com/frederictaillandier/GstalderBot/assets/5926779/733c27bb-086e-4016-ab94-35e8820a77bc)

