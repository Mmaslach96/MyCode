package lab3;

public class Triangle implements Comparable<Triangle>
{
	private Point a,b,c;
	
	public Triangle(Point a, Point b, Point c)
    {
        this.a = a;
        this.b = b;
        this.c = c;
    }
	
	public double isTriangle(Point a, Point b, Point c)
	{
		if(a.countDistance(b)+ b.countDistance(c) > c.countDistance(a) && b.countDistance(c)+ c.countDistance(a) > a.countDistance(b) && c.countDistance(a)+ a.countDistance(b) > b.countDistance(c) )
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
	
	public double countPerimeter()
	{
		if(isTriangle(a,b,c)==1)
		{
			return a.countDistance(b)+b.countDistance(c)+c.countDistance(a);
		}
		else return 0;
	}
	
	public double countArea()
	{
		double p;
		if(isTriangle(a,b,c)==1)
		{
			p=countPerimeter()/2;
			
			return Math.sqrt(p*(p-a.countDistance(b))*(p-b.countDistance(c))*(p-c.countDistance(a)));
		}
		else return 0;
	}
	
	public double countHeight(double n)
	{
		double p;
		if(isTriangle(a,b,c)==1)
		{
			p=countArea();
			if(n==1)
			{
				return 2*p/a.countDistance(b);
			}
			else if(n==2)
			{
				return 2*p/b.countDistance(c);
			}
			else if(n==3)
			{
				return 2*p/c.countDistance(a);
			}
			else return 0;
		}
		else return 0;
	}
	
	public void updateCoordinate(double n, double v1, double v2)
	{
		if(isTriangle(a,b,c)==1)
		{
			if(n==1)
			{
				a.setV1(v1);
				a.setV2(v2);
			}
			else if(n==2)
			{
				b.setV1(v1);
				b.setV2(v2);
			}
			else if(n==3)
			{
				c.setV1(v1);
				c.setV2(v2);
			}
		}		
	}
	
 	public int compareTo(Triangle t)
 	{
        return Double.compare(countArea(), t.countArea());
 	}
	
	public String toString()
	{
		String s = "";
		if(isTriangle(a,b,c)==1)
		{
			s+="("+ a.getV1() + "," + a.getV2() +") ";
			s+="("+ b.getV1() + "," + b.getV2() +") ";
			s+="("+ c.getV1() + "," + c.getV2() +")";
		
        	return s;
		}
		else
		{
			s = "Nie istenieje taki trojkat :(";
			return s;
		}
    }
	
}
