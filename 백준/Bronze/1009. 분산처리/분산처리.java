import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			ArrayList<Integer> pattern = new ArrayList<>();
			int rest = a % 10;
			pattern.add(rest);

			while (true) {
				rest = (rest * a) % 10;
				if (pattern.contains(rest)) {
					break;
				}
				pattern.add(rest);
			}

			int idx = b % pattern.size();
			int answer = (idx == 0) ? pattern.get(pattern.size() - 1) : pattern.get(idx - 1);

			if (answer == 0) {
				answer = 10;
			}
			System.out.println(answer);
		}
	}
}