package Exercise_6;

class ExceptionHandlingDemo {
    public static void main(String args[]){
        try {
            int a=14;
            int b=0;
            int result=a/b;
        } catch (ArithmeticException e) {
            System.out.println("Division by zero is not allowed!");
        }
        try {
            int[] a={10,20,30};
            System.out.print("Value: "+a[5]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("The array index is out of range!");
        }
        finally{
            System.out.println("The block executes regardless of an exception");
        }
        System.out.println("Program continues after exception handling");
    }
}
