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

import java.util.concurrent.Future;

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
        
    }
}
