package lab3;

import java.util.Arrays;

public class Figures 
{
	 public static void main(String[] args)
	    {
		 	Point a = new Point(5,5);
		 	Point b = new Point(6,7);
		 	System.out.println("Punkt1: " + a);
		 	System.out.println("Odleglosc miedzy punktami wynosi: " + a.countDistance(b));
		 	
		 	Triangle t = new Triangle(new Point(0,0), new Point(0,4), new Point(3,0));
		 	System.out.println("Triangle1: " + t);
		 	Triangle t1 = new Triangle(new Point(5,0), new Point(50,7), new Point(17,0));
		 	System.out.println("Triangle1: " + t1);
		 	Triangle t2 = new Triangle(new Point(0,0), new Point(0,7), new Point(5,0));
		 	System.out.println("Triangle1: " + t2);
		 	
		 	System.out.println("Obwod wynosi: " + t.countPerimeter());
		 	System.out.println("Pole wynosi: " + t.countArea());
		 	System.out.println("Wysokosc z 1 wierzcholka: " + t.countHeight(3));
		 	
		 	Quadrangle q = new Quadrangle(new Point(0,0), new Point(0,10), new Point(10,10), new Point(10,0));
		 	System.out.println("Quadrangle1: " + q);
		 	Quadrangle q1 = new Quadrangle(new Point(2,5), new Point(-7,100), new Point(10,10), new Point(10,0));
		 	System.out.println("Quadrangle1: " + q1);
		 	Quadrangle q2 = new Quadrangle(new Point(0,0), new Point(0,50), new Point(17,19), new Point(15,3));
		 	System.out.println("Quadrangle1: " + q2);
		 	
		 	System.out.println("Obwod wynosi: " + q.countPerimeter());
		 	System.out.println("Pole wynosi: " + q.countArea());
		 	System.out.println("Przekatne wynosza: " + q.countDiagonal(1) + " , " + q.countDiagonal(2));
		 	
		 	t.updateCoordinate(1, 2, 4);
		 	System.out.println("Triangle1: " + t);
		 	
		 	q.updateCoordinate(1, 1, 1);
		 	System.out.println("Quadrangle1: " + q);
		 	
		 	Triangle [] tri = {t,t1,t2};
		 	Quadrangle [] quad = {q,q1,q2};
		 	
		 	System.out.println("Nieposortowane pola trojkatow:");
		 	for (Triangle element : tri)
		 	{
	            System.out.println(element.countArea());
	        }
		 	System.out.println("Posortowane pola trojkatow:");
		 	Arrays.sort(tri);
		 	for (Triangle element : tri)
		 	{
	            System.out.println(element.countArea());
	        }
		 	
		 	System.out.println("Nieposortowane pola kwadratow:");
		 	for (Quadrangle element : quad)
		 	{
	            System.out.println(element.countArea());
	        }
		 	System.out.println("Posortowane pola kwadratow:");
		 	Arrays.sort(quad);
		 	for (Quadrangle element : quad)
		 	{
	            System.out.println(element.countArea());
	        }
	    }
}

//Point Array.sort.B