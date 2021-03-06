# Twitter Bot

This plugin is performs auto likes of mentions or auto following followers.

# Configuration

This node requires configuration. You need to have a dev account in the twitter. To do that
visit https://apps.twitter.com/ and create your own app. If you don't know how to do it
visit: https://smashballoon.com/doc/create-your-own-twitter-app/

**Important**

You need to add at least `Read and write permissions` for that app to work correctly.

## Resource configuration

Please add a resource inside Tracardi that have the following schema:

```json
{
  "access_token": "<ACCESS_TOKEN>",
  "access_token_secret": "<ACCESS_TOKEN_SECRET>",
  "consumer_key": "<API_KEY>",
  "consumer_secret": "<API_KEY_SECRET>"
}
```

* consumer_key: None, You can find in Consumer Keys API Key and Secret
* consumer_secret: None, - You can find it in Consumer Keys API Key and Secret
* access_token: None - You can find it in Authentication Tokens Access Token and Secret
* access_token_secret: None - You can find it in Authentication Tokens Access Token and Secret

# Plugin configuration

To access credentials you will have to provide a resource id that point to the schema typed above. 

## Example of plugin configuration

```json
{
  "source": {
    "id": "55584df6-9ee3-4acd-a0ea-e555122f3dbc"
  },
  "action": "mention"
}
```

This config will like all recent mentions.

# Input

This node does not process input payload.

# Output

This node only return True if tweet posting was successfully.
