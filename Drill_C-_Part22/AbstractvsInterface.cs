using System;

// Abstract Class
public abstract class Customer
{
    // Abstract Classes can inherite from both interfaces and other
    // abstract classes
    int ID; // Abstract Class can have a field
    public void Print()
    {
        Console.WriteLine("print");
    }
} 

public interface ICustomer
{
    // Interfaces cannot have fields
    // Interfaces can inherite from other interfaces but not from a 
    // abstract class.
    void Print();
}

public class Program
{
	public static void Main()
	{

	}
}
