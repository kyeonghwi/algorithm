import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] dis = new int[4];
		int sum = 0;
		for (int i = 0; i < 4; i++) {
			dis[i] = sc.nextInt();
			sum += dis[i];
		}
		System.out.println(sum / 60);
		System.out.println(sum % 60);
	}
}