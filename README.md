# Imagine-Linker
![Imagine LInker logo](https://github.com/Frosteco/Imagine-Linker/blob/main/Imagine%20Linker%20logo.png "I'll shatter that DMCA of yours!")

Imagine Linker is a Reddit bot that monitors a subreddit and DMs users who requested it.

Every time user comments under a post, the bot checks whether the comment matches the trigger expression.

If it finds an exact match, it sends a DM to the user who posted the comment.

The monitored subreddit, trigger expression and the structure of DMs can be specified in the config file.

## Why was this bot created?

This reddit bot was created in June 2025 after the subreddit r/toarumajutsunoindex got banned for "excessive copyright removals". The most probable cause of this ban could have been the links on the subreddit's wiki. These links led to various websites, providing the means to purchase and read the source material. Due to a changing nature of global licenses (mainly the licensing of New testament series by Yen Press), the subreddit got a DMCA claim and was shut down by Reddit.

### What is a DMCA claim and is it bad?
The DMCA claim and takedown process is a tool for copyright holders to get copyrighted material taken down of websites. A DMCA claim informs a company that they are hosting or linking to copyrighted material.

Since Reddit doesn't want to deal with international court, it quickly removes the claimed material. And since Reddit is a large website with a lot of data, it doesn't have the resources to do a thorough check of every DMCA claim's scale. Therefore, Reddit will ban the entire subreddit instead of just removing the wiki.

While the reason of DMCA's existence is valid, the way it is enforced is often radical and vague (the original laws were not made with high-speed Internet in mind). Years of content were lost simply because of a sudden change in licensing and it's radical enforcement. The claims may also be false positives, having the same effect without the right to do so. While it is possible to appeal for these claims, Reddit is still a company that makes money and fears legal actions (a thorough investigation may not be as thorough, since time = money, time = legal action and legal action = money).


## Why use a bot for sharing links?
Sharing links using this bot has many benefits for a subreddit:
1. Ban prevention - using a bot instead of a wiki for links will tranfer the potencial ban onto the bot, leaving a subreddit ban-safe
2. Liability transfer - if the bot is operated by a third party user (with no connection to the subreddit's mod team), the liability is shifted away from the subreddit
3. Decentralization - If one user's bot gets a DMCA claim, they can remove the bot without any remorse to avoid problems and another user can quickly set up their own bot with the links
4. Open-source - anyone can implement this bot on any subreddit, fork it to their liking or help develop the original codebase

## Getting started
1. Create the bot's reddit account (write down the account's name and password
2. Login to https://www.reddit.com/prefs/apps/ with the bot's account
3. Click "Create app" - fill out "name" with random selected name, select "script" option, fill out "redirect uri" with "http://www.example.com/unused/redirect/uri"
4. Write down the client_id and client_secret (the 2 long strings on the app profile)
5. Download the folder "Imagine Linker" from GitHub
### A) Running from your device
6. Open "config.py", fill out the config by following comments
7. Run "bot.py" (ctrl+F5 in VS Code, or Rightclick - Open with - Python)
8. Your device has to be online 24/7 if possible, or make it run on startup so people get a DM at least once a day (don't worry, it ignores previously parsed comments so there should be no spam)
### B) Running from cloud
6. Create an account on https://www.pythonanywhere.com/registration/register/beginner/ (free account)
7. Click "Browse files", then "Upload files"
8. From "Imagine Linker" folder upload "bot.py" and "config.py"
9. Open "bot.py" on the PythonAnywhere, select ">>>Run"
10. Don't worry about the CPU usage going up (soft limit, it resets every day and app just works slower after 100%)
