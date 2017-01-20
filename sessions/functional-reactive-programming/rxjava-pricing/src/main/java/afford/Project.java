package afford;

import java.math.BigDecimal;

public class Project {
    private final Integer words;
    private final BigDecimal listPrice;
    private final BigDecimal amount;

    public Project(Integer words, BigDecimal listPrice, BigDecimal amount) {
        this.words = words;
        this.listPrice = listPrice;
        this.amount = amount;
    }

    public boolean isAffordable() {
        return listPrice.compareTo(amount) < 0;
    }

    @Override
    public String toString() {
        return "afford.Project{" +
                "words=" + words +
                ", listPrice=" + listPrice +
                ", amount=" + amount +
                '}';
    }
}
