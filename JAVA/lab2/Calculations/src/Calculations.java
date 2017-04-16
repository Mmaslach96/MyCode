
public class Calculations 
{

    public static void main(String[] args)
    {
    	//Wektor 1 wywo³anie i deklaracja
        System.out.println("Lets's begin.");
        Vector v1 = new Vector(2);
        v1.setValue(0,4);
        v1.setValue(1,4);
        System.out.println("Vector1:" + v1);
        
        //Wektor2 wywolanie i deklaracja
        Vector v2 = new Vector(2);
        v2.setValue(0,5);
        v2.setValue(1,5);
        System.out.println("Vector2:" + v2);
        
        //Liczeie skalaru Wektora1 i Wektora2
        v1.countScalar(v2);
        
        //Wybieranie wartosci
        v2.selectValue(1);
        
        //Zmiana wartoœci wektora2 z pozycji 0 na wartosæ 5
        v2.changeValue(0,5);
        System.out.println("Vector po zmianie [0] na wartoœæ 5: " + v2);
        
        //Dodawanie wektorów
        v1.addVectors(v2);
        System.out.println("Dodawanie v1 + v2: " + v1);
        
        System.out.println("");
        // ######### MACIERZE ########### //
        
        //Deklaracja nowej macierzy
        Matrix m1 = new Matrix(2,2);
        m1.setValue(0, 0, 5);
        m1.setValue(0, 1, 5);
        m1.setValue(1, 0, 5);
        m1.setValue(1, 1, 5);
        System.out.println("Matrix1: \n" + m1);
        
        //Deklaracja nowej macierzy
        Matrix m2 = new Matrix(2,2);
        m2.setValue(0, 0, 5);
        m2.setValue(0, 1, 5);
        m2.setValue(1, 0, 5);
        m2.setValue(1, 1, 5);
        System.out.println("Matrix1: \n" + m2);
        
        //Dodwanie macierzy
        m1.addMatrix(m2);
        System.out.println("Matrix1 + Matrix2: \n" + m1);
        
        //Zmiana wartoœci macierzy
        m1.changeValue(0, 0, 2);
        System.out.println("Matrix1 po zmianie [0][0] na wartoœæ 2: \n" + m1);
        
        //Wypisywanie wartosci macierzy
        m2.selectValue(0, 1);
        
        //Mno¿enie macierzy przez Wektor
        m2.multiplyVector(v2);
        System.out.println("Matrix2 po mno¿eniu przez Vector2: \n" + m2);
        
   }


}
