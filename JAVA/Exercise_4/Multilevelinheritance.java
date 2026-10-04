
import java.util.Scanner;

public class Multilevelinheritance {
    public static void main(String[] args) {
        System.out.print("Enter the person name: ");
        Scanner sc=new Scanner(System.in);
        Person3 p=new Person3();
        p.name=sc.next();
        System.out.print("Enter person Age: ");
        p.age=sc.nextInt();
        System.out.print("Enter person Id: ");
        p.id=sc.nextInt();
        System.out.print("Enter person Department: ");
        p.department=sc.next();
        p.show();
        sc.close();
    }
}


class Person1{
    String name;
    int age;
    void display(){
        System.out.println("Name: "+name);
        System.out.println("Age: "+age);
    }
}
class Person2 extends Person1{
    int id;
    void displaying(){
        display();
        System.out.println("Id: "+id);
    }
}
class Person3 extends Person2{
    String department;
    void show(){
        displaying();
        System.out.println("Department: "+department);
    }
}

















