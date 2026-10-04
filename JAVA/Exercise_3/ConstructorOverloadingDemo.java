
import java.util.Scanner;

public class ConstructorOverloadingDemo {
    public static void main(String[] args) {
        String name;
        int id;
        double marks;
        ConstructorStudent s1=new ConstructorStudent();
        System.out.print("enter the student name: ");
        Scanner sc=new Scanner(System.in);
        name=sc.next();
        System.out.print("Enter the student Id: ");
        id=sc.nextInt();
        System.out.print("Enter the Student marks: ");
        marks=sc.nextDouble();
        ConstructorStudent s2=new ConstructorStudent(name,id,marks);
        System.out.println("Student 1: ");
        s1.display();
        System.out.println("Student 2: ");
        s2.display();
        sc.close();
    }
}


class ConstructorStudent{
    String name;
    int id;
    double marks;
    ConstructorStudent(){
        name="Not assigned";
        id=0;
        marks=0.0;
    }
    ConstructorStudent(String name,int id,double  marks){
        this.name=name;
        this.id=id;
        this.marks=marks;
    }
    void display(){
        System.out.println("Student Detials ");
        System.out.println("Name: "+name);
        System.out.println("id: "+id);
        System.out.println("Marks: "+marks);
    }
}















