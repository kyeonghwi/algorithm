import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();

			int n = sc.nextInt();
			ArrayList<Circle> list = new ArrayList();
			for (int j = 0; j < n; j++) {
				int cx = sc.nextInt();
				int cy = sc.nextInt();
				int r = sc.nextInt();
				list.add(new Circle(cx, cy, r));
			}

			int cnt = 0;
			for (Circle circle : list) {
				double dis1 = Math.sqrt(Math.pow(circle.cx - x1, 2) + Math.pow(circle.cy - y1, 2));
				double dis2 = Math.sqrt(Math.pow(circle.cx - x2, 2) + Math.pow(circle.cy - y2, 2));
				boolean in1 = dis1 < circle.r;
				boolean in2 = dis2 < circle.r;
				if (in1 != in2) {
					cnt++;
				}
			}

			System.out.println(cnt);

		}

	}
}

class Circle {
	int cx, cy, r;

	Circle(int cx, int cy, int r) {
		this.cx = cx;
		this.cy = cy;
		this.r = r;
	}
}