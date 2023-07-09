# GstalderBot
A chatbot to manage a shared house chores

## Install and Use

Fork the repository as it relies on github workflow to run,and add a secret as:</br>
`GSTALDERCONFIG_PROD`</br>
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
where:</br>
**open_ai_key** is your [gpt_api](https://platform.openai.com/account/api-keys) api key</br>
**bot_token** is your [telegram](https://core.telegram.org/bots/api) bot token</br>
**global_chat_id** is the [telegram](https://core.telegram.org/bots/api) group chat where the bot writes for all flatmates</br>
**flatmates** is the list of your flatmates and **chat_it** fits a chat only targeted for a specific flatmate</br>

test
