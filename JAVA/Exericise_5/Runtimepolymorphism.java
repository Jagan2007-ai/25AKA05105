package Exericise_5;
public class Runtimepolymorphism {
    public static void main(String args[]){
        Animal a=new Dog();
        a.makesound();
        a=new Lion();
        a.makesound();
    }
}








class Animal{
    void makesound(){
        System.out.println("Animal make sounds");
    }
}

class Dog extends Animal{
    @Override
    void makesound(){
        System.out.println("dog barks");
    }
}

class Lion extends Animal{
    @Override 
    void makesound(){
        System.out.println("Lion roars");
    }
}







