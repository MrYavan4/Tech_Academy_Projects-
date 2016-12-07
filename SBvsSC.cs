using System;
using System.Text;

namespace StringBuilderVsSrtingClass
{
    class Program
    {
        static void Main(string[] args)
        {

            // String Class: Strings are immutable, as such in order to add to them
            // one has to create a new string instance. This can be seen bellow

            string strMyValue = "Hello";

            // Create a new string instance instead of changing the old one

            strMyValue += "How Are ";
            strMyValue += "You?";

            Console.WriteLine(strMyValue);




            // String Builder: StringBuilder is mutable, which means you can use operations like
            // insert, replace, append without creating a new instance of it

            StringBuilder sbMyValue = new StringBuilder("");
            sbMyValue.Append("Hello ");
            sbMyValue.Append("How Are ");
            sbMyValue.Append("You?");

            Console.WriteLine(sbMyValue);

        }
    }
}
