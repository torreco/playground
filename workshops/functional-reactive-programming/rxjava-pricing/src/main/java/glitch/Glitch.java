package glitch;

import rx.Observable;

public class Glitch {

    public static void main(String[] args) {
        Observable<Integer> ones = Observable.range(1, 2);
        Observable<Integer> hundreds = ones.map(x -> x * 100);

        Observable<Integer> sum = ones.withLatestFrom(hundreds, (o, h) -> o + h);
        sum.subscribe(s -> System.out.println(s));
    }
}
