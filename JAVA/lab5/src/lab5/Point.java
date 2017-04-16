package lab5;

public class Point 
{
	private double v1,v2;
	
	public Point(double v1, double v2)
    {
        this.v1 = v1;
        this.v2 = v2;
    }
	
    public double getV1()
    {
    	return v1;
    }
    
    public double getV2()
    {
    	return v2;
    }
    
	public void setV1(double v1)
	{
		this.v1=v1;
	}
	
	public void setV2(double v2)
	{
		this.v2=v2;
	}
	
	public double countDistance(Point p)
	{
		return Math.sqrt(Math.abs(((p.v1-v1)*(p.v1-v1))+((p.v2-v2)*(p.v2-v2))));
	}
	
	public String toString()
	{
		String s = "";
		s="("+ v1 + "," + v2 +")";
        return s;
    }
    
}
