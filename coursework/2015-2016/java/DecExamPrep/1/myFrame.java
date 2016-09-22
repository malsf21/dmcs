import javax.swing.JFrame;

public class myFrame extends JFrame {
	public myFrame (){
		this.setSize(400,300);
		this.setTitle("My Window");
		this.setVisible(true);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	public static void main(String[] args){
		myFrame window = new myFrame();
		myCanvas canvas = new myCanvas();
		window.getContentPane().add(canvas);
	}
}
