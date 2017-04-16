package lab5;

import java.awt.*;

public abstract class MyPolygon implements Figure
{
	public abstract java.awt.Polygon getPolygon();
    public static int polygons = 0;
    protected int number;
    protected Color figureColor;

    public MyPolygon(Color figureColor)
    {
        number = polygons++;
        this.figureColor = figureColor;
    }

    public int getNumber() 
    {
        return number;
    }

    public void setNumber(int number) 
    {
        this.number = number;
    }

    public Color getFigureColor()
    {
        return figureColor;
    }

    public void setFigureColor(Color figureColor) 
    {
        this.figureColor = figureColor;
    }


    public void draw(Graphics2D graphics)
    {
        graphics.setColor(figureColor);
        graphics.drawPolygon(getPolygon());
        graphics.fillPolygon(getPolygon());
    }

    @Override
    public String toString()
    {
        return "Number: " + number + ", area: " + countArea() + ", perimeter: " + countPerimeter();
    }
}