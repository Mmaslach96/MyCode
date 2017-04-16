package lab4;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class FirstJFrame extends JFrame
{
	
	private JPanel contentPane;
	
	
	public static void main(String[] args)
	{
		EventQueue.invokeLater(new Runnable() 
		{
			public void run() 
			{
				try
				{
					FirstJFrame frame = new FirstJFrame();
					frame.setVisible(true);
				} 
				catch (Exception e) 
				{
					e.printStackTrace();
				}
			}
		});
	}

	public FirstJFrame() 
	{
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSizeAndLocation();
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
        contentPane.add(new FigureComponent());
        setContentPane(contentPane);
	}
	
	
	public void setSizeAndLocation()
	{
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		double width = screenSize.getWidth();
		double height = screenSize.getHeight();
		setBounds((int)(width-width/2)/2, (int)(height-height/2)/2, (int)width/2, (int)height/2);
	}
}
