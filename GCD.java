import java.util.*;

public class GCD {
  private static int gcd_naive(int a, int b) {
    int c = 0;
    if(b == 0)  return a;
    c = a % b;
    return gcd_naive(b, c);
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(gcd_naive(a, b));
  }
}
