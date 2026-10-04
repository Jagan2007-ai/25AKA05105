package Exericise_5;

public class Interfacedemo {
    public static void main(String[] args) {
        Child c=new Child();
        c.show();
    }
}






interface Mother{
    int propert=50000;
    int height=100;
}
interface  Father{
    int property=140000;
    int height=50;
}
class Child implements  Father, Mother{
    int total=Father.property+Mother.propert;
    double avg=(Father.height+Mother.height)/2.0;
    void show(){
        System.out.println("Mother property: "+Mother.propert);
        System.out.println("Father Property: "+Father.property);
        System.err.println("Total property: "+total);
        System.out.println("Father height: "+Father.height);
        System.out.println("Mother height: "+Mother.height);
        System.out.println("Total avg hiegth: "+avg);
    }
}









