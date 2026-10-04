package Exercise_6;

public class MultipleCatchDemo {
    public static void main(String[] args) {
        try {
            String str=null;
            int[] numbers=new int[5];

            System.out.println("The length of the string is: "+str.length());
            
            numbers[10]=100;

        } catch (NullPointerException e) {
            System.out.println("The string is Null");
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("The array index out of range");
        }
        catch(Exception e){
            System.out.println("There is an error exception is occured");
        }
        finally{
           System.out.println("The program was handle the Exception Successfully");
        }
        System.out.println("The program was executed successfully");
    }
}
