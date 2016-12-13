using System;
using System.IO;
using System.Text;
 
namespace ErrorExceptionHandeling
{
    class Program
    {
        static void Main(string[] args)
        {
            // Test the logException function. We Assume there is an exception
            Exception ex = new Exception();
            LogException("test", "TestLog", ex.ToString());
        }

        // Creating function write text to log file

        public static void LogException(string strFileName, string strFunctionName, string strContent)
        {
            StreamWriter writer = null;
            StringBuilder strBuilder = null;
            string dir = @"C:\Users\tanvir\Desktop\C#";

            //Check folder exists
            if (!Directory.Exists(dir))
            {
                Directory.CreateDirectory(dir);
            }

            string path = Path.Combine(dir, strFileName + ".log");
            strBuilder = new StringBuilder("Log : ");
            strBuilder.Append(strFunctionName + " | ");
            strBuilder.Append(strContent);

            writer = new StreamWriter(path, true);
            writer.Write(strBuilder);
            writer.Close();
        }
    }
}
