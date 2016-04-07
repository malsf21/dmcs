import javax.swing.JFrame;

public class myFrame extends JFrame{
	public myFrame(){
		this.setSize(400,300);
		this.setVisible(true);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	/**
	* Overloaded constructor, often more useful and general purpose
	* than the default constructor
	*/

	public myFrame(int frameWidth, int frameHeight){
		this.setSize(frameWidth,frameHeight);
		this.setVisible(true);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	public myFrame(int frameWidth, int frameHeight, String title){
		this.setSize(frameWidth,frameHeight);
		this.setTitle(title);
		this.setVisible(true);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}


	public static void main(String[] args){
		//instantiates instance of class template
		myFrame frame = new myFrame(640,400);
		myCanvas canvas = new myCanvas(640,400);
		frame.getContentPane().add(canvas);
	}

}
