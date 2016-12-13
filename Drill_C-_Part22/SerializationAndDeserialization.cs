using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace Serialization_Deserialization
{
    [Serializable]
    public class Person
    {
        public int age = 0;
        public String name = null;

        static void Main(string[] args)
        {
            Person person = new Person();

            person.age = 30;

            person.name = "James";

            
            
            //Serialization Logic Starts

            Stream writerstream = File.Open("filename.txt", FileMode.Create);

            BinaryFormatter binformat = new BinaryFormatter();

            Console.WriteLine("The Persons name is: {0}, and he is {1} yeats old", person.name, person.age);

            binformat.Serialize(writerstream, person);

            writerstream.Close();

            // Serialization Logic Ends
            


            // Deserialization Logic Starts

            person = null;

            Stream streamreader = File.Open("filename.txt", FileMode.Open);

            binformat = new BinaryFormatter();

            Console.WriteLine("Reading Person Information");

            person = (Person)binformat.Deserialize(streamreader);

            streamreader.Close();
            // Deserialization Logic Ends
        }
    }
}
