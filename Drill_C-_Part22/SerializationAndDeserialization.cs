using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Threading.Tasks;

namespace Serialization
{
    class SerialzingData
    {
        Stream stream = null;
        BinaryFormatter bformatter = null;
        String txtFilename = "";
        public SerialzingData(string filename)
        {
            txtFilename = filename;
            stream = File.Open(txtFilename, FileMode.Create);
            bformatter = new BinaryFormatter();
        }

        public void SerlializeObject(Object objectToSerialize)
        {
            bformatter.Serialize(stream, objectToSerialize);
        }

        public void DeserializeObject()
        {
            Object objectToDeserialize = null;
            stream = File.Open(txtFilename, FileMode.Open);
        }
        public void closeStream()
        {
            stream.Close();
        }
    }
}
