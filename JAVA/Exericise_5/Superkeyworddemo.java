package Exericise_5;
public class Superkeyworddemo {
    public static void main(String[] args) {
        Dog d=new Dog("Tommy","German Shepard");
        d.show2();
    }
}






class Animal{
    String name;
    Animal(String name){
        this.name=name;
    }
    void show1(){
        System.out.println("The Animal name is: "+name);
    }
}

class Dog extends Animal{
    String bread;
    Dog(String name,String bread){
        super(name);
        this.bread=bread;
    }
    void show2(){
        show1();
        System.out.println("The Bread is: "+bread);
    }
}









