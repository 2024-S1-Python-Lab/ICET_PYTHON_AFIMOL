class Product
{
    int pcode;
    String pname;
    int pprice;
    Product(int code,String name,int price)
    {
        pcode=code;
        pname=name;
        pprice=price;
    }
    void display(){
    System.out.println("Product code : " +pcode);
    System.out.println("Product name : " +pname);
    System.out.println("Product price : " +pprice);
    }
}
class MainProduct
{
    public static void main(String args[])
    {
        Product ob1=new Product(123,"pen",10);
        Product ob2=new Product(124,"pencil",5);
        Product ob3=new Product(125,"pasta",100);
        System.out.println("\n Product with lower price :");
        if(ob1.pprice<ob2.pprice)
        
            if(ob1.pprice<ob3.pprice)
                ob1.display();
            else
            
                ob3.display();
            
        else if(ob3.pprice<ob2.pprice)
        
            ob3.display();
        
        else
        
            ob2.display();
        
        
    }
}