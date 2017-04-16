package lab5;

import java.awt.Color;
import java.awt.Polygon;

public class Quadrangle extends MyPolygon implements Comparable<Quadrangle>
{
	private Point a,b,c,d;
	
	public Quadrangle(Point a, Point b, Point c, Point d, Color figureColor)
    {
		super(figureColor);
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
 	
    public Polygon getPolygon()
    {
        Polygon p = new Polygon();
        p.addPoint((int) a.getV1(), (int) a.getV2());
        p.addPoint((int) b.getV1(), (int) b.getV2());
        p.addPoint((int) c.getV1(), (int) c.getV2());
        p.addPoint((int) d.getV1(), (int) d.getV2());
        return p;
    }
	
    public String toString() 
    {
        return super.toString();
    }
}