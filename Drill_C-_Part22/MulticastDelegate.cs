using System;
using System.Collections.Generic;

delegate void MeDelegate();

class MainClass
{
    static void Main()
    {
        MeDelegate d = ReturnFive;
        d += ReturnTen;
        d += ReturnTwenty;
        int value = d();
        List<int> ints = new List<int>();
        foreach (MeDelegate del in d.GetInvocationList())
            ints.Add(del());
        foreach (int i in ints)
            Console.WriteLine(i);
    }

    static int ReturnFive()
    {
        return 5;
    }

    static int ReturnTen()
    {
        return 10;
    }
    static int ReturnTwenty()
    {
        return 20;
    }
}
