package afford;

import java.math.BigDecimal;

public class Balance {
    private final BigDecimal amount;

    private final String currency;

    public Balance(BigDecimal amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public String getCurrency() {
        return currency;
    }

    @Override
    public String toString() {
        return "afford.Balance{" +
                "amount=" + amount +
                ", currency='" + currency + '\'' +
                '}';
    }
}