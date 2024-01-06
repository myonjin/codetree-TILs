import java.util.Scanner;


public class Main {

    public static int a;
    public static int b;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        f();
        System.out.println(a + " " + b);
    }

    public static void f() {
        if (a > b) {
            a = a * 2;
            b = b + 10;
        } else {
            a = a + 10;
            b = b * 2;

        }
    }
}