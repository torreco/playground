package com.torre.rxjavaexample.services;

import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import org.springframework.stereotype.Service;

@Service
public class SlackApiService {

    public void publishMessage(String channel, String text, String iconEmoji) throws UnirestException {
        Unirest.post("https://slack.com/api/chat.postMessage")
                .field("channel", channel)
                .field("text", text)
                .field("token", token)
                .field("icon_emoji", iconEmoji)
                .asJson();
    }

}
