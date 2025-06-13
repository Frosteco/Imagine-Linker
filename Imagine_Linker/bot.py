import praw
import time
import logging
from config import CONFIG

# Logs
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

def create_reddit_instance():
    reddit_conf = CONFIG["reddit"]
    return praw.Reddit(
        client_id=reddit_conf["client_id"],
        client_secret=reddit_conf["client_secret"],
        username=reddit_conf["username"],
        password=reddit_conf["password"],
        user_agent=reddit_conf["user_agent"]
    )

def main():
    reddit = create_reddit_instance()
    subreddit = reddit.subreddit(CONFIG["reddit"]["subreddit"])
    message_body = "\n\n".join(CONFIG["links"])
    dm_subject = CONFIG["dm_subject"]

    logging.info("Bot active, monitoring subreddit r/%s", CONFIG["reddit"]["subreddit"])

    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            author = comment.author.name if comment.author else "[deleted]"
            logging.info("Parsing comment by u/%s", author)
            
            if comment.body.strip().lower() == CONFIG["trigger_expression"]:
                logging.info("DM request recognised and processed - u/%s thanks you for your service!", author)
                reddit.redditor(author).message(
                    subject=dm_subject,
                    message=message_body
                )
        except Exception as e:
            logging.error("Error: %s", e)
        time.sleep(1)

if __name__ == "__main__":
    main()