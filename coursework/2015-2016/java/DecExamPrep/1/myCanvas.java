import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class myCanvas extends Canvas implements KeyListener{
	private int myX;
	private int myY;	
	/**
	* myCanvas default constructor, builds individual instances of class
	*/
	public myCanvas() {
		myX = 10;
		myY = 10;
		this.setSize(400,400);
		this.setFocusable(true);
		this.addKeyListener(this);
	}

	/**
	* myCanvas overloaded constructor, builds individual instances of class
	*/
	public myCanvas(int w, int h) {
		myX = 10;
		myY = 10;
		this.setSize(w,h);
		this.setFocusable(true);
		this.addKeyListener(this);
	}
	@Override
	public void paint(Graphics graphics){
		graphics.fillOval(myX,myY,30,30);
	}
	
	public void keyPressed(KeyEvent event){
		if (event.getKeyCode() == 77){
			myX+=10;
		}
		repaint();
	}
	public void keyReleased(KeyEvent event){

	}
	public void keyTyped(KeyEvent event){

	}
	
}
