import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;

public class myCanvas extends Canvas implements KeyListener {

	private int myX;
	private int myY;
	private int playerW;
	private int playerH;

	public myCanvas(){
		this.setSize(400,300);
		this.setVisible(true);
		this.setFocusable(true);
		this.addKeyListener(this);
		myX = 10;
		myY = 10;
		playerW = 30;
		playerH = 30;
	}

	public myCanvas(int canvasWidth, int canvasHeight){
		this.setSize(canvasWidth,canvasHeight);
		this.setVisible(true);
		this.setFocusable(true);
		this.addKeyListener(this);
		myX = 10;
		myY = 10;
		playerW = 30;
		playerH = 30;
		
	}
	
	/**
	* paint is overriden method from Canvas.java
	* @param g is graphics to draw on
	*/
	@Override
	public void paint(Graphics g){
		g.fillOval(myX,myY,playerW,playerH);
	}
	
	public void keyPressed(KeyEvent e){
		System.out.println(e.getKeyCode());
		if (e.getKeyCode() == KeyEvent.VK_D){
			myX += 10;
		}
		else if (e.getKeyCode() == KeyEvent.VK_A){
			myX -= 10;
		}
		else if (e.getKeyCode() == KeyEvent.VK_S){
			myY += 10;
		}
		else if (e.getKeyCode() == KeyEvent.VK_W){
			myY -= 10;
		}
		

		repaint();
	}
	public void keyReleased(KeyEvent e){

	}
	public void keyTyped(KeyEvent e){

	}
	
	
}
