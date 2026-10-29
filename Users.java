import java.math.BigDecimal;

public class Users {
        String name;
        int id_number;
        BigDecimal bank_balance;
        String account_number;
        

        public Users(String name, int id_number, BigDecimal bank_balance){
            this.name = name;
            this.id_number = id_number;
            this.bank_balance = bank_balance;

            this.account_number = "A1_" + id_number;
        }

        public BigDecimal withdraw_cash(BigDecimal amount, BigDecimal bank_balance){
            if (amount.compareTo(BigDecimal.ZERO) <= 0){
                System.out.println("Withdrawals must be more than KSH 0!");
                return bank_balance;
            }

            if (amount.compareTo(bank_balance) > 0) {
                System.out.println("\n\nInsuficent funds in your account !! \nDeposit to your account and try again.\nThank you for using Falcon eWallet"); 
                
                return bank_balance;
            }

            bank_balance = bank_balance.subtract(amount);

            System.out.println("Transuction succesfull, new wallet balance is: KSh " +bank_balance);
            return bank_balance;
        }

        public BigDecimal deposit_cash(BigDecimal amount, BigDecimal bank_balance){
            if (amount.compareTo(BigDecimal.ZERO) <= 0){
                System.out.println("You can only deposit amounts gretter than ZERO!");
                return bank_balance;
            }

            bank_balance = bank_balance.add(amount);

            System.out.println("Transuction succesfull, new wallet balance is: KSh " +bank_balance);
            return bank_balance;
        }
}
