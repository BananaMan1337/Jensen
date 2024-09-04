using System;

// Parent djur
class Djur
{
    // Ras atribute
    public string Ras { get; protected set; }

    // ljud
    public virtual void Ljud()
    {
        Console.WriteLine("Djur gör ett ljud.");
    }
}

// child för hund och katt som tar från djur
class Hund : Djur
{
    // olika raser i en lista
    private static readonly string[] HundRaser = { "Golden", "Tax", "German Sheppard", "Långben" };

    public Hund()
    {
        // väljer en slumpmässigt vald ras
        Random random = new Random();
        Ras = HundRaser[random.Next(HundRaser.Length)];
    }

    // skriver över djurets ljud med hunden
    public override void Ljud()
    {
        Console.WriteLine($"Hunden av rasen {Ras} skäller");
    }
}

// child för katt
class Katt : Djur
{
    // kattraser
    private static readonly string[] KattRaser = { "Sköldpadsfärgad", "Ragdoll", "Garfield", "Tiger", "lejon" };

    public Katt()
    {
        // väljer en kattras slumpmässigt
        Random random = new Random();
        Ras = KattRaser[random.Next(KattRaser.Length)];
    }

    // skriver över djur till kattens ljud
    public override void Ljud()
    {
        Console.WriteLine($"Katten av rasen {Ras} jamar");
    }
}

class Program
{
    static void Main(string[] args)
    {
        // lista med alla objekt
        Djur[] djurLista = new Djur[] {
            new Djur(),
            new Katt(),
            new Hund()
        };

        // Anropa Ljud-metoden på varje objekt i listan
        foreach (Djur djur in djurLista)
        {
            djur.Ljud();
        }
    }
}
