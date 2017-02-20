# RXJava

### Goal

Explore and code real examples of how to use RXJava with external services.

## Environment setup

Use gradle to run this project.

## Integrations

### Slack integration

* Slack integration to publish a message to a given channel(SlackApiService.java).

### NLP observable

* Integration with Google NLP API to do sentiment analysis(NLPApiService.java).

### Twitter observable

* Twitter integration to build a continues stream of twits about a topic(TwitterApiService.java).

## TODO

### Exercise 1

* Go to ExampleRunner.java and implement on the run function a service that:
  1. Collect twits.
  2. Send them to the NLP API.
  3. Based on the sentiment include an emoji.
  4. Send it as a message to slack.

### Exercise 2

* Go to ExampleRunner.java and implement on the run function a service that:
  1. Build and observable of trending topics.
  2. Collect twits about trending topics.
  3. Emit twits based on the lates trending topic(use [switch](http://reactivex.io/documentation/operators/switch.html)).
  4. Filter neutral comments.
  5. Send them to the NLP API.
  6. Based on the sentiment include an emoji.
  4. Send it as a message to slack.
