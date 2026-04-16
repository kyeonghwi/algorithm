import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			int dis = y - x;

			int n = 0;

			int max = (int)Math.sqrt(dis);
			
			if (max == Math.sqrt(dis)) {
				System.out.println(max*2-1);
			} else if (dis<=max*max + max) {
				System.out.println(max*2);
			} else {
				System.out.println(max*2 +1);
			}
		}
	}
}
