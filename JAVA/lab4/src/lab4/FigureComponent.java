package lab4;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JComponent;

public class FigureComponent extends JComponent
{
 	public void paintComponent(Graphics o)
	{
 	    Graphics2D graphics = (Graphics2D) o;
 		
 		Quadrangle[] quadrangles = new Quadrangle[2];
 		quadrangles[0] = new Quadrangle(new Point(0, 250), new Point(400, 250), new Point(400, 450), new Point(0,450), Color.YELLOW);
        quadrangles[1] = new Quadrangle(new Point(600, 55), new Point(455, 166.66), new Point(780, 130), new Point(700,30), Color.YELLOW);

        for(Quadrangle quadrangle : quadrangles)
        {
            quadrangle.drawFigure(graphics);
        }
 		

        Triangle[] triangles = new Triangle[2];
        triangles[0] = new Triangle(new Point(0, 0), new Point(200, 200), new Point(0, 200), Color.RED);
        triangles[1] = new Triangle(new Point(200, 200), new Point(400, 200), new Point(400, 0), Color.RED);
        
        for(Triangle triangle : triangles)
        {
            triangle.drawFigure(graphics);
        }
	}
}
