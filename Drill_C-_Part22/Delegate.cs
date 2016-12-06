using System;


class Program
{

    static void Main(string[] args)
    {
        MyClass obj = new MyClass();
        obj.LongRunning(CallBack);
    }

    static void CallBack(int i)
    {
        Console.WriteLine(i);
    }

    public class MyClass
    {
        public delegate void CallBack(int i);
	    public void LongRunning(CallBack obj)
	    {
            for(int i = 0; i < 100; i++)
            {
                //Do Something
                obj(i);
            }
	    }
    }
}
