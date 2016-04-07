import javax.swing.JFrame;
/**
*FYCompsci Exam Code by Matthew Wang; JFrame
*This is the window where all of the magic is hosted in!
*/
public class myFrame extends JFrame{
	/**
	*This is our default "constructor", It runs every time we instantiate our class!
	*This one takes no parameters
	*/
	public myFrame(){
		this.setSize(400,300);
		this.setTitle("My Exam Game");
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setVisible(true);
	}
	/**
	*This is our overloaded constructor, It runs every time we instantiate our class!
	*This one takes two parameters, screen width and height
	*/
	public myFrame(int screenWidth,int screenHeight){
		this.setSize(screenWidth,screenHeight);
		this.setTitle("My Exam Game");
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setVisible(true);
	}
	/**
	*This is our other overloaded constructor, It runs every time we instantiate our class! You can have as many overloaded constructors as you want
	*This one takes three parameters, screen name, width and height
	*/
	public myFrame(int screenWidth,int screenHeight, String screenTitle){
		this.setSize(screenWidth,screenHeight);
		this.setTitle(screenTitle);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setVisible(true);
	}
	/**
	*This is our main function, it runs on startup
	*/
	public static void main(String[] args){
		myFrame window = new myFrame(400,300,"Extending our Knowledge");//instantiating our class!
		myCanvas canvas = new myCanvas(400,300);
		window.getContentPane().add(canvas);//here, we're using a getter to get the content pane of our window, and then add our canvas! 
	}
}
