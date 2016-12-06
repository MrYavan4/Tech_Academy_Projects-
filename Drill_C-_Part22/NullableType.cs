using System;

class NullableType
{
    static void Main(string[] args)
    {
        bool? someThing = null;

        if (someThing == true)
	{
            Console.WriteLine("SomeThing");
	}
        else if (someThing == true)
        {
            Console.WriteLine("SomeThing Else");
        }
        else
        {
            Console.WriteLine("Default");
        }
    }
}

