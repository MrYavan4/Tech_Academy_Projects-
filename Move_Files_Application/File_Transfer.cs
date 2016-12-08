using System;
using System.IO;
using Microsoft.VisualBasic;

namespace FileTransfer
{
    public class SimpleFileCopy
    {

        static void Main()
        {
            fileTransfer();
        }

        static void fileTransfer()
        {
            string sourcePath = @"C:\Users\tanvir\Desktop\Folder_A";
            string targetPath = @"C:\Users\tanvir\Desktop\Folder_B";

            string[] files = Directory.GetFiles(sourcePath);

            if (!Directory.Exists(targetPath))
            {
                Directory.CreateDirectory(targetPath);
            }

            foreach (var allFiles in files)
            {

                // Get today's Date
                DateTime now = DateTime.Now;

                // Get date less 24 hours
                DateTime old = now.AddHours(-24);

                // Get last access time for files in the directory
                DateTime newFile = File.GetLastWriteTime(allFiles);

                // Check if file where modified in the past 24 hours
                if (now > newFile && newFile > old)
                {

                    // If modified in the last 24 hours copy files and move to target directory
                    File.Copy(allFiles, allFiles.Replace(sourcePath, targetPath), true);

                    // Delete files that have been transfered
                    File.Delete(allFiles);
                }
            }

            Console.WriteLine("Files have been transfered");
        }

    }
}