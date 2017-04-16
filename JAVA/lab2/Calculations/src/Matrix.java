
public class Matrix 
{
	private double[][] tab;
	private int size1,size2;
	
	public Matrix(int size1, int size2)
    {
        this.tab = new double[size1][size2];
        this.size1 = size1;
        this.size2 = size2;
    }
	
	public void setValue(int i, int j, double value)
    {

		if(i < size1 && i>=0 && j<size2 && j>=0)
        {
            tab[i][j] = value;
        }
    }
	
	public void addMatrix(Matrix m)
    {
    	if(size1==m.size1 && size2==m.size2)
    	{
    		for(int i = 0; i < size1; i++)
    		{
    			for(int j = 0; j < size2; j++)
    			{
    				this.tab[i][j] += m.tab[i][j];
    			}
    		}
    	}
    	else
    	{
    		System.out.println("Nie mo�na dodawa� dw�ch wektor�w o r�nych wymiarach");
    	}
    }
	
    public void changeValue(int i, int j, double value)
    {
    	if(i<size1 && i>=0 && j<size2 && j>=0)
    	{
            tab[i][j] = value;
    	}
    	else
    	{
    		System.out.println("Nie mo�na zmieni� warto�ci, z powodu z�ego indeksu");
    	}
    }
    
    public void selectValue(int i,int j)
    {
    	System.out.println("Skladowa [" + i +"," + j + "] wektora wynosi: " + tab[i][j]);
    }
    
    public void multiplyVector(Vector v)
    {
    	if(size1==v.getSize())
    	{
    		for(int i = 0; i < size1; i++)
    		{
    			for(int j = 0; j < size2; j++)
    			{
    				tab[i][j] = tab[i][j] * v.getTab()[i];
    			}
    		}
    	}
    	else
    	{
    		System.out.println("Nie mo�na mno�y� macierzy przez wektor o r�nych wymiarach");
    	}

    }
	
	public String toString()
	{
		int i,j;
		String s ="";
		for(i=0;i<size1;i++)
		{
			for(j=0;j<size2;j++)
			{
				s+="["+ i + ","+ j +"]"+tab[i][j]+"  ";
			}
			s+="\n";
		}
        return s;
    }
	
	
	
}
