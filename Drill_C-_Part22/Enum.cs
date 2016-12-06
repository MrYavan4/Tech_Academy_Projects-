using System;
using System.Windows.Forms;

namespace Enumaration
{
    public class TempExp
    {
        enum Tempurature
        {
            Low,
            Medium,
            High,
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Temperature value = Tempurature.Medium;
            if (value == Tempurature.Medium)
            {
                MessageBox.Show ("Temperature is Mediuam..");
            }
        }
    }
}
