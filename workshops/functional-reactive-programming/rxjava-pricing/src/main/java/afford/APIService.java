package afford;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.Unirest;
import org.json.JSONObject;
import rx.Observable;

import java.util.concurrent.Future;


public class APIService {

    private final String user;
    private final String password;

    public APIService(String user, String password) {
        this.user = user;
        this.password = password;
    }

    public Observable<Balance> balance() {
        Future<HttpResponse<JsonNode>> responseFuture =
                Unirest
                        .get("https://api.voicebunny.com/balance")
                        .basicAuth(this.user, this.password)
                        .asJsonAsync();

        return Observable.from(responseFuture)
                .map(response -> response.getBody())
                .map(jsonNode -> {
                    JSONObject obj = jsonNode.getObject().getJSONObject("balance");
                    return new Balance(obj.getBigDecimal("amount"), obj.getString("currency"));
                });
    }

    public Observable<Quote> quote(Integer words) {

        Future<HttpResponse<JsonNode>> responseFuture =
                Unirest
                        .post("https://api.voicebunny.com/projects/quote")
                        .field("numberOfWords", words)
                        .field("language", "eng-us")
                        .basicAuth(this.user, this.password)
                        .asJsonAsync();

        return Observable.from(responseFuture)
                .map(response -> response.getBody())
                .map(jsonNode -> {
                    JSONObject obj = jsonNode.getObject().getJSONObject("quote");
                    return new Quote(words, obj.getBigDecimal("price"), obj.getBigDecimal("listPrice"));
                });
    }
}
