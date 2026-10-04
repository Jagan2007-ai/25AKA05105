
package Exercise_6;

public class UserDefineExceptionDemo {
    public static void Age(int age) throws AgeException{
        if(age<0 || age>150){
            throw new AgeException("Invalid "+age+". Age must be between 0 to 150");
        }
        else{
            System.out.println("Valid : "+age);
        }
    }
    public static void main(String args[]){
        try {
            Age(25);
            Age(-5);
        } catch (AgeException e) {
            System.out.println("Caugth Exception: "+e.getMessage());
        }
    }

}

class AgeException extends Exception{
    public AgeException(String messsage){
        super(messsage);
    }
}






