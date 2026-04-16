import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int n = sc.nextInt();
			for (int a = 0; a < n; a++) {
				for (int b = 0; b < n; b++) {
					if (a == 0 || b == 0 || a == n - 1 || b == n - 1) {
						System.out.print("#");
					} else {
						System.out.print("J");
					}
				}
				System.out.println();
			}
			System.out.println();
		}
	}
}