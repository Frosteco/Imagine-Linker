# config.py

CONFIG = {
    "reddit": {
        "client_id": "", # PRAW ID, unique for each bot
        "client_secret": "", # PRAW ID, unique for each bot
        "username": "", # bot account username, change when DMCA claim
        "password": "", # bot account password, change when account hacked
        "user_agent": "Instance of Imagine Linker, by", #fill in bot account username, has to be unique, never lie or spoof other programs, change when DMCA claim
        "subreddit": "" # subreddit's name without r/
    },
    "dm_subject": "Links", # name of the message, max 100 letters
    "trigger_expression": "!links", # this exact phrase activates the bot, letter case is ignored
    "links": [
        "Enjoy the links!",
        "⸜(˶ˆᗜˆ˵)⸝♡",
        "---",
        "[Linkname1](https://example.com/1)",
        "[Linkname2](https://example.com/2)",
        "[Linkname3](https://example.com/3)"
    ] # each comma-separated line is a new line in the DM
}
