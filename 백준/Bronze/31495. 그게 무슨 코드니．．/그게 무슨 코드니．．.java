import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();

		if (s.length() >= 2 && s.startsWith("\"") && s.endsWith("\"")) {
            if (s.equals("\"\"")) {
                System.out.println("CE");
            } else {
                System.out.println(s.substring(1, s.length() - 1));
            }
        } else {
            System.out.println("CE");

	}
}
}