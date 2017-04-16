package lab5;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class FigureComponent extends JComponent
{

    private ArrayList<MyPolygon> p;
    private Figure[] figures;

    public FigureComponent() {
        this.p = new ArrayList<>(5);
        this.figures = new Figure[5];

        p.add(new Quadrangle(new Point(0, 250), new Point(400, 250), new Point(400, 450), new Point(0,450), Color.YELLOW));
        p.add(new Quadrangle(new Point(600, 55), new Point(455, 166.66), new Point(780, 130), new Point(700,30), Color.YELLOW));
        p.add(new Quadrangle(new Point(600, 5), new Point(455, 66), new Point(78, 130), new Point(70,30), Color.YELLOW));
        p.add(new Triangle(new Point(0, 0), new Point(200, 200), new Point(0, 200), Color.RED));
        p.add(new Triangle(new Point(200, 200), new Point(400, 200), new Point(400, 0), Color.RED));

        int i = 0;
        for(MyPolygon polygon : p) 
        {
            figures[i++] = polygon;
        }
       
        
        System.out.println("List of polygons:");
        p.forEach(System.out::println);
        System.out.println("Size of list of polygons: " + MyPolygon.polygons);

        System.out.println("Array of figures:");
        for(Figure figure : figures)
        {
            System.out.println("Area: " + figure.countArea() + ", perimeter: " + figure.countPerimeter());
        }
    }

    public void paintComponent(Graphics g)
    {
        Graphics2D graphics = (Graphics2D) g;

        for(MyPolygon polygon : p)
        {
            polygon.draw(graphics);
        }
    }
}

