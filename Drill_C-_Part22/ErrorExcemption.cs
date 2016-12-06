using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.IO;

namespace LoggingErrors
{
    
    // Log and exception
	public static void LogExceptions(Exception exc, string source)
	{
        string logFile = @"C:\Users\tanvir\Desktop\Folder_B\test.txt";
        logFile = httContext.Current.Server.Mypath(logFile);

        // Open the log file for append and write the log
        StreamWriter sw = new StreamWriter(logFile, true);
        sw.WriteLine("********** {0} **********", DateTime.Now);

        sw.Close();
    }
}
