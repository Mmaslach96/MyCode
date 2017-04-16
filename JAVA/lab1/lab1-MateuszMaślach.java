class SolveEquation 
{
    public static void main(String[] args)
    {
        System.out.println("Program liczy miejsca zerowe dla co najwy¿ej wielomianu drugiego stopnia.");
        Polynomial eq = new Polynomial(0,-5,7);
        eq.count();
        eq.show();
    }
}

class Polynomial
{
	double a,b,c;
	double delta;


	public Solution solution;
	
    public Polynomial(double b1, double c1)
    {
        this.a = 0.0;
        this.b = b1;
        this.c = c1;
        this.solution = new Solution();
    }
    
    public Polynomial(double a1, double b1, double c1)
    {
        this.a = a1;
        this.b = b1;
        this.c = c1;
        this.solution = new Solution();
    }
    
	public void show()
	{
		System.out.println(toString());
		delta = b * b - (4 * a * c);
		
		if(a!=0)
		{
			if(delta>0)
			{
				System.out.println("Równanie ma dwa pierwiastki:"+solution.getX1()+", "+ solution.getX2());
				if(a>0)
				{
					System.out.println("Funkcja ma minimum w punkcie:("+ -b/(2*a) +","+ -delta/(4*a)+ ")");
				}
				if(a<0)
				{
					System.out.println("Funkcja ma maksimum w punkcie:("+ -b/(2*a) +","+ -delta/(4*a)+ ")");
				}
			}
			else if(delta==0)
			{
				System.out.println("Równanie ma pierwiastek podwójny:"+solution.getX());
				if(a>0)
				{
					System.out.println("Funkcja ma minimum w punkcie:("+ -b/(2*a) +","+ -delta/(4*a)+ ")");
				}
				if(a<0)
				{
					System.out.println("Funkcja ma maksimum w punkcie:("+ -b/(2*a) +","+ -delta/(4*a)+ ")");
				}
			}
			else
			{
				System.out.println("Równanie ma pierwiastki urojone: "+solution.getX1()+"i, "+ solution.getX2() + "i");
				if(a>0)
				{
					System.out.println("Funkcja ma minimum w punkcie:("+ -b/(2*a) +","+ -delta/(4*a)+ ")");
				}
				if(a<0)
				{
					System.out.println("Funkcja ma maksimum w punkcie:("+ -b/(2*a) +","+ -delta/(4*a)+ ")");
				}
			}
		}
		else if(b!=0 && a==0)
		{
			System.out.println("Funkcja ma jedno rozwi¹zanie równe: "+ solution.getX());
			System.out.println("Funkcja nie ma ekstremów");
		}
		
		else if(b==0 && a==0)
		{
			System.out.println("Funkcja nie ma pierwiastków");
			System.out.println("Funkcja nie ma ekstremów");
		}
	}
	
	public void count()
	{
		if(a!=0)
		{
			delta = b * b - (4 * a * c); 
			if(delta>0)
			{
				solution.setX1((-b-Math.sqrt(delta))/(2*a));
				solution.setX2((-b+Math.sqrt(delta))/(2*a));
			}
			else if(delta==0)
			{
				solution.setX((-b)/(2*a));
			}
			else
			{
				delta=Math.abs(delta);
				solution.setX1((-b-Math.sqrt(delta))/(2*a));
				solution.setX2((-b+Math.sqrt(delta))/(2*a));
			}
		}
		else if(b!=0 && a==0)
		{
			solution.setX(c/(-b));
		}
		
	}
	
	
	public String toString()
	{
        String y = "";
        if(a != 0) 
        {
            y = a + "x^2";
        }

        if(b != 0) 
        {
            if(a!=0) y+=" + ";
            y += b + "x";
        } 
        	
        if(c != 0) 
        {
        	if(b!=0 || a!=0) y+=" + ";
            y += c;
        } 

        return y;
    }
	
}

class Solution
{
	private double x;
	private double x1;
	private double x2;
	
    public double getX() 
    {
        return x;
    }
 
    public void setX(double x)
    {
        this.x = x;
    }
    
    public double getX1() 
    {
        return x1;
    }
 
    public void setX1(double x1)
    {
        this.x1 = x1;
    }
    
        public double getX2() 
    {
        return x2;
    }
 
    public void setX2(double x2)
    {
        this.x2 = x2;
    }
    
}