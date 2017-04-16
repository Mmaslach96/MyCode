package lab3;

public class Quadrangle implements Comparable<Quadrangle>
{
	private Point a,b,c,d;
	
	public Quadrangle(Point a, Point b, Point c, Point d)
    {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }
	
	public double isQuadrangle(Point a, Point b, Point c, Point d)
	{
		double x,y,z;
		x=Math.max(a.countDistance(b), b.countDistance(c));
		y=Math.max(x, c.countDistance(d));
		z=Math.max(y, d.countDistance(a));
		if(z < a.countDistance(b) + b.countDistance(c) + c.countDistance(d) + d.countDistance(a) - z && a.countDistance(b) > 0 && b.countDistance(c) > 0 && c.countDistance(d) > 0 && d.countDistance(a) > 0)
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
		if(isQuadrangle(a,b,c,d)==1)
		{
			return a.countDistance(b)+b.countDistance(c)+c.countDistance(d)+d.countDistance(a);
		}
		else return 0;
	}
	
	public double countArea()
	{
		double p;
		if(isQuadrangle(a,b,c,d)==1)
		{
			p=countPerimeter()/2;
			return Math.sqrt((p-a.countDistance(b))*(p-b.countDistance(c))*(p-c.countDistance(d))*(p-d.countDistance(a)));
		}
		else return 0;
	}
	
	public double countDiagonal(double n)
	{
		if(isQuadrangle(a,b,c,d)==1)
		{
			if(n==1)
			{
				return a.countDistance(c);
			}
			else if(n==2)
			{
				return b.countDistance(d);
			}

			else return 0;
		}
		else return 0;
	}
	
	public void updateCoordinate(double n,double v1, double v2)
	{
		if(isQuadrangle(a,b,c,d)==1)
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
			
			else if(n==4)
			{
				d.setV1(v1);
				d.setV2(v2);
			}
		}
			
	}
	
 	public int compareTo(Quadrangle q)
 	{
        return Double.compare(countArea(), q.countArea());
 	}
	
	public String toString()
	{
		String s = "";
		if(isQuadrangle(a,b,c,d)==1)
		{
			s+="("+ a.getV1() + "," + a.getV2() +") ";
			s+="("+ b.getV1() + "," + b.getV2() +") ";
			s+="("+ c.getV1() + "," + c.getV2() +") ";
			s+="("+ d.getV1() + "," + d.getV2() +")";
		
        	return s;
		}
		else
		{
			s = "To nie jest czworokat :(";
			return s;
		}
    }
}

