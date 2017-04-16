import java.util.Arrays;

public class Vector
{
	private double[] tab;
	private int size;
	
	public void setTab(double [] tab)
	{
		this.tab=tab;
	}
	
	public double[] getTab()
	{
		return tab;
	}
	
	public void setSize(int size)
	{
		this.size=size;
	}
	
	public int getSize()
	{
		return size;
	}
	
	public Vector(int size)
    {
        this.tab = new double[size];
        this.size = size;
    }

    public void setValue(int i, double value)
    {
        if(i<getSize() && i>=0)
        {
            tab[i] = value;
        }
    }
    
    public void selectValue(int i)
    {
    	System.out.println("Skladowa [" + i + "] wektora wynosi: " + tab[i]);
    }
    
    public void addVectors(Vector v)
    {
    	if(tab.length==v.tab.length)
    	{
    		for(int i = 0; i < tab.length; i++)
    		{
    			this.tab[i] += v.tab[i];
    		}
    	}
    	else
    	{
    		System.out.println("Nie mo¿na dodawaæ dwóch wektorów o ró¿nych wymiarach");
    	}
    }
    
    public void changeValue(int i, double value)
    {
    	if(i<tab.length && i>=0)
    	{
            tab[i] = value;
    	}
    	else
    	{
    		System.out.println("Nie mo¿na zmieniæ wartoœci, z powodu z³ego indeksu");
    	}
    }
    
    public Vector(Vector v)
    {
        this.tab = Arrays.copyOf(v.tab, v.tab.length);
    }
    
    public void countScalar(Vector v)
    {
    	double x=0;
    	if(tab.length==v.tab.length)
    	{
    		for(int i = 0; i < tab.length; i++)
    		{
    			x+=tab[i]*v.tab[i];
    		}
    		System.out.println("Skalar wynosi: " + x);
    	}
    	else
    	{
    		System.out.println("Nie mo¿na liczyæ skalaru dwóch wektorów o ró¿nych wymiarach");
    	}

    }
	
	public String toString()
	{
		int i;
		String s = "";
		for(i=0;i<size;i++)
		{
			s+=" ["+ i +"]"+tab[i]+"  ";
		}
        return s;
    }
}
