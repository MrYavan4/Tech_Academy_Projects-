using System;

namespace Program1
{
    class Program
    {
        // This is where the program starts 
        static void Main(string[] args)
        {
            // Prompt the user to enter a name
            Console.WriteLine("Enter your name, please: ");

            //Now read the name entered
            string name = Console.ReadLine();

            // Great the user with the name that was entered 
            Console.WriteLine("Hello, " + name);

            //Wait for the user to acknowledge the results 
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();              
        }
    }
}
