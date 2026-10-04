public class Singleinheritance {
    public static void main(String args[]){
        Student s=new Student();
        s.name="kira";
        s.age=20;
        s.id=144;
        s.display();
        s.displayStudent();
    }
}




class Person{
    String name;
    int age;
    void display(){
        System.out.println("Name: "+name);
        System.out.println("Age: "+age);
    }
}
class Student extends Person{
    int id;
    void displayStudent(){
        System.out.println("Id: "+id);
    }
}
