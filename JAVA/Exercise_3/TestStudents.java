
import java.util.Scanner;

public class TestStudents {

    public static void main(String args[]) {
        String name, branch;
        int id;
        System.out.print("Enter the student name: ");
        Scanner sc = new Scanner(System.in);
        name = sc.nextLine();
        System.out.print("Enter the student id: ");
        id=sc.nextInt();
        System.out.print("Branch: ");
        branch=sc.next();
        Student s=new Student();
        s.setdetails(name, id, branch);
        s.Display();
    }
}

class Student{
    String name,brach;
    int id;
    void setdetails(String name,int id,String branch){
        this.name=name;
        this.id=id;
        this.brach=branch;
    }
    void Display(){
        System.out.println("Student Details");
        System.out.println("name: "+name);
        System.out.println("id: "+id);
        System.out.println("branch: "+brach);
    }
}