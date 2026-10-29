
import java.math.BigDecimal;

public class Main{
    public static void main(String[] args) {

        Users u1 = new Users("Alex", 1234, new BigDecimal(550.50));
        Users u2 = new Users("John", 1235, new BigDecimal(780.70));

        
        u1.withdraw_cash(new BigDecimal(50.49), u1.bank_balance);

    }    

}
