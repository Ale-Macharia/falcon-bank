
import java.math.BigDecimal;
import java.util.ArrayList;

public class Main{
    public static void main(String[] args) {
        ArrayList<Users> customers = new ArrayList<>();


        Users u1 = new Users("Alex", 1234, new BigDecimal(550.50));
        Users u2 = new Users("John", 1235, new BigDecimal(780.70));

        u1.withdraw_cash(new BigDecimal(50.49));

        customers.add(u1);

        // for (Users users in Users customers){

        // }

    }    

}
