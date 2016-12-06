using System;

class Animal
{
    public double height { get; set; }
    public double weight { get; set; }
    public string sound { get; set; }

    public string name;
    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    public Animal()
    {
        //Use of "This"
        this.height = 0;
        this.weight = 0;
        this.name = "No Name";
        this.sound = "No Sound";
        numOfAnimals++;

    }
}
