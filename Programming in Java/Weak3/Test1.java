import java.util.Scanner;
public class Fibonacci {

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println(fib(n));
    }
    //Template code:
    static int fib(int n) {
     if(n ==1) return 0
     else if(n == 2) return 1
     else{
         int first = 0, second = 1;
         for(int i= 3; i<=n; ++i){
             int temep = first;
             first = second;
             second = first + temp;
         }
         return second;
     }
     }

    }
