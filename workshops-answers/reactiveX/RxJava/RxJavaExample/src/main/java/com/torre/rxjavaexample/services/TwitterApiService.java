package com.torre.rxjavaexample.services;

import io.reactivex.BackpressureStrategy;
import io.reactivex.Flowable;
import io.reactivex.FlowableEmitter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import twitter4j.Status;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.conf.ConfigurationBuilder;

@Service
public class TwitterApiService {

    private TwitterStreamFactory twitterStreamFactory = null;

    public TwitterApiService(){
        this.twitterStreamFactory = this.buildTwitterStreamFactory();
    }

    private TwitterStreamFactory buildTwitterStreamFactory(){
        ConfigurationBuilder cb = new ConfigurationBuilder();
        cb.setOAuthConsumerKey(consumerKey)
                .setOAuthConsumerSecret(consumerSecret)
                .setOAuthAccessToken(accessToken)
                .setOAuthAccessTokenSecret(accessTokenSecret);
        return  new TwitterStreamFactory(cb.build());
    }

    public Flowable<String> getTwits(String topic){
        return Flowable.create((FlowableEmitter<Status> emitter) -> {
            TwitterStream twitterStream = this.twitterStreamFactory.getInstance();
            twitterStream.onStatus((Status e) -> {
                        emitter.onNext(e);
                    })
                    .onException((Exception e) -> {
                        emitter.onError(e);
                    });
            twitterStream.filter(topic);
        }, BackpressureStrategy.LATEST).map(Status::getText);
    }

}
