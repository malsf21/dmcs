import java.awt.*;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;
import java.util.Random;

public class myCanvas extends Canvas implements KeyListener {

	private int myX;
	private int myY;
	private int playerW;
	private int playerH;

	enemy[] enemies = new enemy[100];

	public myCanvas(){
		this.setSize(400,300);
		this.setVisible(true);
		this.setFocusable(true);
		this.addKeyListener(this);
		myX = 10;
		myY = 10;
		playerW = 30;
		playerH = 30;
		Random rand = new Random();
		int x;
		int y;

		for (int i = 0; i < enemies.length; i++){
			x = rand.nextInt(this.getWidth());
			y = rand.nextInt(this.getHeight());
			enemies[i] = new enemy(x,y,5);
		}
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
		Rectangle r = new Rectangle(myX,myY,playerW,playerH);
		for (int i = 0; i < enemies.length; i++){
			if (enemies[i] != null){
				g.drawOval(enemies[i].enemyX, enemies[i].enemyY, enemies[i].enemySize, enemies[i].enemySize);
			

				if (r.intersects(enemies[i].enemyX,enemies[i].enemyY, enemies[i].enemySize, enemies[i].enemySize)){
					enemies[i] = null;
					playerW += 5;
					playerH += 5;
				}
			}
		}
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
