print("Thinking of tweeting huh? Well don't. You'll get sucked into a rabbit hole. If you insist though...")
tweet = input("Enter your tweet here to check it:")

tweet = len(tweet)
if tweet > 140:
    tweetmath = tweet - 140

if tweet < 140:
    print(f"Your {tweet} character tweet is totes valid. Noice")
else:
    print(f"Your {tweet} tweet is {tweetmath} chars too long. Condense your conspiracy theories.")


