import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;


public class myCanvas extends Canvas implements KeyListener{
	private int myX;
	private int myY;
	public myCanvas(){
		this.setSize(400,300);
		this.setFocusable(true);
		this.setVisible(true);
		this.addKeyListener(this);
		myX = 10;
		myY = 10;
	}

	@Override
	public void paint(Graphics graphics){
		graphics.fillOval(myX,myY,30,30);
	}

	public void keyPressed(KeyEvent event){
	
	}

	public void keyReleased(KeyEvent event){
	
	}
	public void keyTyped(KeyEvent event){
	
	}
}
