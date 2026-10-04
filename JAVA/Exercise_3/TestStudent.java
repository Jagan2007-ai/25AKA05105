
public class TestStudent {
    public static void main(String args[]){
        Students s=new Students("kira", 144,"CSE");
        s.display();
    }
}
class Students{
    String name,branch;
    int id;
    Students(String name,int id,String branch){
        this.name=name;
        this.id=id;
        this.branch=branch;
    }
    void display(){
        System.out.println("Student details ");
        System.out.println("Name: "+name);
        System.out.println("Id: "+id);
        System.out.println("Branch: "+branch);
    }
}