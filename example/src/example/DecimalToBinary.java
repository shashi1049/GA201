package example;

public class DecimalToBinary {
	
	public static String decimalToBinary(String decimalStr) {
        try {
            int decimalNum = Integer.parseInt(decimalStr);
            if (decimalNum < 0) {
                return "-" + Integer.toBinaryString(-decimalNum);
            } else {
                return Integer.toBinaryString(decimalNum);
            }
        } catch (NumberFormatException e) {
            return "Invalid input: Not a decimal number";
        }
    }

    public static void main(String[] args) {
        String decimalStr = "123";
        String binaryStr = decimalToBinary(decimalStr);
        System.out.println("Decimal: " + decimalStr + " -> Binary: " + binaryStr);
    }

}
