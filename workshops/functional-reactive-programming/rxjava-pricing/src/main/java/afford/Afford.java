package afford;

import rx.Observable;


public class Afford {

    public static void main(String[] args) {
        // REPLACE WITH API KEYS
        APIService api = new APIService("<client_id>", "<client_key>");

        Observable<Balance> oBalance = api.balance();

        Observable
                .from(new Integer[]{1, 20, 40, 60, 80, 100, 120, 140, 150})
                .flatMap(w -> api.quote(w))
                .withLatestFrom(oBalance, (quote, balance) -> new Project(quote.getWords(), quote.getListPrice(), balance.getAmount()))
                .takeWhile(Project::isAffordable)
                .subscribe(
                        project -> System.out.println(project),
                        e -> e.printStackTrace(),
                        () -> System.out.println("Complete")
                );
    }
}
