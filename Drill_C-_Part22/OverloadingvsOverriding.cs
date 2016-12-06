using System;

namespace OverloadingvsOverriding
{
    public class test
    {

/* Overloading is the act of having multiple methods in the same
 * scope, with the same name but different signature
 */
        public void getStuff(int id)
        {}

        public void getStuff(string name)
        {}

/* Overriding is the concept that allows you to change the functionality of a method 
 in a child class*/

        public class test1
        {
            public virtual  void something(int id)
            {
                //Something goes here
            }
        }

        public class test3 : test1
        {
            public override void something(int id)
            {
                base.something(id);
            }
        }
    }
}
