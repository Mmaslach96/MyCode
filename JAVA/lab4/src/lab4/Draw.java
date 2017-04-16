package lab4;
import java.awt.*;

public abstract class Draw 
{
    public Color figureColor;
    public abstract Polygon getPolygon();
    
    public Draw(Color figureColor) 
    {
        this.figureColor = figureColor;
    }

    public Color getFigureColor()
    {
        return figureColor;
    }

    public void setFigureColor(Color figureColor) 
    {
        this.figureColor = figureColor;
    }

    public void drawFigure(Graphics2D graphics)
    {
        graphics.setColor(figureColor);
        graphics.drawPolygon(getPolygon());
        graphics.fillPolygon(getPolygon());
    }
}