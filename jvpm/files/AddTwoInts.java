public class AddTwoInts {
    public static void main (String[] args) throws java.io.IOException {
        java.util.Scanner reader = new java.util.Scanner(System.in);
		System.out.println("Enter first integer:");
        int a = reader.nextInt();
		System.out.println("Enter second integer:");
        int b = reader.nextInt();
		System.out.println("The sum is:");
        System.out.println (a+b);
    }
}