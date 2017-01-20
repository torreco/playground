package afford;

import java.math.BigDecimal;

public class Quote {

    private final Integer words;
    private final BigDecimal price;
    private final BigDecimal listPrice;

    public Quote(Integer words, BigDecimal price, BigDecimal listPrice) {
        this.words = words;
        this.price = price;
        this.listPrice = listPrice;
    }

    public Integer getWords() {
        return words;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public BigDecimal getListPrice() {
        return listPrice;
    }

    @Override
    public String toString() {
        return "afford.Quote{" +
                "price=" + price +
                ", listPrice=" + listPrice +
                '}';
    }
}