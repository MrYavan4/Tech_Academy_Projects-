using System;

// Public Acess 

class publicAcess
{
    public int x = 10;
    public int y = 20;
}

class MainClass
{
    static void Main()
    {
        publicAcess p = new text();
        p.x = 10;
        p.y = 20;
        Console.WriteLine("x = {} and y = {}", p.x, p.y);
    }
}

// Protected Access 

// The protected keyword is a member access modifier. 
// A protected member is accessible within its class and by derived class instances.

class Protected
{
    protected int x = 10;
    protected int y = 20;
}

class MainClass : Protected
{
    static void Main()
    {
        MainClass test = new MainClass();

        // Direct access to protected members
        test.x = 10;
        test.y = 20;
        Console.WriteLine("x = {} and y = {}", test.x, test.y);
    }
}

// Internal: Only accessible within the same assembly 

public class AssemblyClass
{
    internal static int x = 0;
}

public class TestAssembly
{
    static void Main()
    {
        // This will be OK
        AssemblyClass test = new AssemblyClass();

        // This will give us a CS0117 error
        AssemblyClass.x = 222;
    }
}

// Private
// The private keyword is a member access modifier. 
//Private access is the least permissive access level. 
//Private members are accessible only within the body of the class or the struct in which they are declared

class Employee2
{
    private string name = "FirstName, LastName";
    private double salary = 100.0;

    public string GetName()
    {
        return name;
    }

    public double Salary
    {
        get { return salary; }
    }
}

class PrivateTest
{
    static void Main()
    {
        Employee2 e = new Employee2();

        // The data members are inaccessible (private), so
        // they can't be accessed like this:
        //    string n = e.name;
        //    double s = e.salary;

        // 'name' is indirectly accessed via method:
        string n = e.GetName();

        // 'salary' is indirectly accessed via property
        double s = e.Salary;
    }
}