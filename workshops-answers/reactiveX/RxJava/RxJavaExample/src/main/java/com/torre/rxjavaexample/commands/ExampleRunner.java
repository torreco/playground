package com.torre.rxjavaexample.commands;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.Unirest;
import com.torre.rxjavaexample.services.NLPApiService;
import com.torre.rxjavaexample.services.SlackApiService;
import com.torre.rxjavaexample.services.TwitterApiService;
import io.reactivex.Flowable;
import org.json.JSONObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

@Component
public class ExampleRunner implements CommandLineRunner {

    private static final Logger logger = LoggerFactory.getLogger(ExampleRunner.class);

    @Autowired
    private TwitterApiService twitterApiService;

    @Autowired
    private SlackApiService slackApiService;

    @Autowired
    private NLPApiService nlpApiService;

    @Override
    public void run(String... args) throws Exception {

//        twitterApiService.getTwits("#MissColombia").flatMap((String text) ->
//                nlpApiService.sentimentAnalysis(text)
//        ).filter((JSONObject o) ->
//                o.getDouble("score") >= 0.2 || o.getDouble("score") <= -0.2
//        ).map((JSONObject o) -> {
//            if(o.getDouble("score") >= 0.2) {
//                return o.put("emoji", ":smile:");
//            } else {
//                return o.put("emoji", ":cry:");
//            }
//        }).subscribe((JSONObject o) -> {
//            slackApiService.publishMessage("#co-chapter-bed", o.getString("text"), o.getString("emoji"));
//        });

        String[] topics = {
                "#tvoh",
                "#Dybala",
                "#SexySports"
        };
        Flowable.switchOnNext(
                Flowable.interval(0L, 2L, TimeUnit.MINUTES).map(
                (Long i) -> i.intValue()
        ).map(
                (Integer i) -> i % topics.length
        ).map(
                (Integer i) -> topics[i]
        ).map(
                (String topic) -> twitterApiService.getTwits(topic)
        )).flatMap((String text) ->
                nlpApiService.sentimentAnalysis(text)
        ).filter((JSONObject o) ->
                o.getDouble("score") >= 0.1 || o.getDouble("score") <= -0.1
        ).map((JSONObject o) -> {
            if(o.getDouble("score") >= 0.6) {
                return o.put("emoji", ":smile:");
            } else {
                return o.put("emoji", ":cry:");
            }
        }).subscribe((JSONObject o) -> {
            slackApiService.publishMessage("#wc-development", o.getString("text"), o.getString("emoji"));
        });
    }
}
