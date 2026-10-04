public class TestMethodOverloading {
    public static void main(String[] args) {
        MethodOverloading m=new MethodOverloading();
        m.sum(10,20);
        m.sum(10,20,30);
        m.sum(10,11.2);
    }
}
class MethodOverloading{
    void sum(int a,int b){
        System.out.println("The sum of two integers: "+(a+b));
    }
    void sum(int a,int b,int c){
        System.out.println("The sum of three integers: "+(a+b+c));
    }
    void sum(int a,double b){
        System.out.println("The sum of two values: "+(a+b));
    }
    void sum(double a,double b){
        System.out.println("The sum of two double values: "+(a+b));
    }
    void sum(double a,double b,double c){
        System.out.println("The sum of three double values: "+(a+b+c));
    }
}
