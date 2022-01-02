# Data for your leisure

This repo is a collection of files for you to use in your applications.

## Available Data Tables

* [A mapping of `gameId: gameName`s](https://github.com/guildedapi/datatables/blob/main/games.json) - the [Game IDs table](https://guildedapi.com/resources/user/#game-ids) in JSON form
* [A mapping of `emojiId: emoji`s](https://github.com/guildedapi/datatables/blob/main/reactions.json) - a parsed & flattened version of the publicly-accessible `StockReactions.js` file provided to clients.
    * If you want to parse this file for yourself, create a `StockReactions-raw.json` and run `StockReactions-parse.py` with Python. It will create or overwrite `reactions.json` in the current working directory.

## Join the Guilded API Server

[The Unofficial API server](https://community.guildedapi.com) is a great place for library and bot developers to hang out and chat. It's also a great starting point for those looking to dive in and learn bot-creation with the API.
