using System;

public class ValueVsRef
{

    public class Differences
    {
        // Value Types
        // They are stored on stack
        // Contains actual value
        // Can not Contain null values unless using nullable types

        int x = 20;
        bool y = true;

        // Reference Type
        // They are stroed on the Heap
        // Contains Reference to a Value
        //Can Contain null Values

        int[] xArray = new int[20];
        Object obj = i;
    }
}
