

import java.util.Scanner;

public class Abstractclassdemo {
    public static void main(String[] args) {
        int choice;
        System.out.println("1.To find the area of Circle");
        System.out.println("2.To find the area of Rectangle");
        System.err.println("q.To exit");
        Scanner sc=new Scanner(System.in);
        Circle c=new Circle();
        Rectangle r=new Rectangle();
        while (true) { 
            System.out.print("Enter your choice(q to exit)");
            choice=sc.nextInt();
            if(choice == 1){
                System.out.print("Enter the radius of Circle: ");
                c.radius=sc.nextDouble();
                c.area();
            }
            else if(choice == 2){
                System.out.print("Enter the length of the Rectangle: ");
                r.length=sc.nextDouble();
                System.out.print("Enter the breadth of the Rectangle: ");
                r.breadth=sc.nextDouble();
                r.area();
            }
            else if(choice == 'q'){
                System.out.println("Thanks for using out services");
                break;
            }
            else{
                System.out.println("Enter a valid choice");
            }
        }
    }
}


abstract class Shape{
    abstract void area();
}

class Circle extends Shape{
    double radius;
    void area(){
        System.out.println("The area of circle is: "+(Math.PI*radius*radius));
    }
}
class Rectangle extends Shape{
    double length;
    double breadth;
    void area(){
        System.out.println("The area of Rectangle is: "+(length*breadth));
    }
}















