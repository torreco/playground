package com.torre.rxjavaexample.services;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.Unirest;
import io.reactivex.Flowable;
import org.json.JSONObject;
import org.springframework.stereotype.Service;

import java.util.concurrent.Future;

import static io.reactivex.Flowable.*;

@Service
public class NLPApiService {

    public Flowable<JSONObject> sentimentAnalysis(String text){
        JSONObject document = new JSONObject()
                .put("type", "PLAIN_TEXT")
                .put("content", text);
        Future<HttpResponse<JsonNode>> responseFuture = Unirest
                .post("https://language.googleapis.com/v1/documents:analyzeSentiment")
                .queryString("key", key)
                .body(new JSONObject()
                        .put("encodingType", "UTF8")
                        .put("document", document)
                )
                .asJsonAsync();
        return fromFuture(responseFuture).map(
                HttpResponse::getBody
        ).map(
                JsonNode::getObject
        ).map((JSONObject o) ->
                o.getJSONArray("sentences").getJSONObject(0)
        ).map((JSONObject o) ->
                new JSONObject()
                        .put("text", o.getJSONObject("text").getString("content"))
                        .put("score", o.getJSONObject("sentiment").getDouble("score"))
        );
    }
}
