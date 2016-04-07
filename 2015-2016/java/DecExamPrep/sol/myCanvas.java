import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;
import java.awt.Color;
/**
*This is our class where all of our fun stuff gets painted on screen (as well as user input
*If you notice, we extend canvas, inheritng all of its properties, and implement keyListener, using its methods
*/
public class myCanvas extends Canvas implements KeyListener{
	//here, we initialize our variables. we encapsulate them so nobody can mess with them! 
	private int playerX;
	private int playerY;
	private int playerW;
	private int playerH;
	private Color playerColor;
	/**
	*This is our default constructor, which builds our class on launch
	*Default constructors take no parameters
	*/
	public myCanvas(){
		this.setSize(400,300);
		this.setFocusable(true);
		this.setVisible(true);
		this.addKeyListener(this);
		playerX = 10;
		playerY = 10;
		playerW = 30;
		playerH = 30;
		playerColor = Color.GREEN;
	}
	/**
	*This is our overloaded constructor, which builds our class on launch
	*This bad boy takes two parameters, the screen width and height
	*/
	public myCanvas(int screenWidth, int screenHeight){
		this.setSize(screenWidth,screenHeight);
		this.setFocusable(true);
		this.setVisible(true);
		this.addKeyListener(this);
		playerX = 10;
		playerY = 10;
		playerW = 30;
		playerH = 30;
		playerColor = Color.GREEN;

	}
	/**
	*This is our other overloaded constructor, which builds our class on launch
	*This giant constructor takes six parameters, the screen width and height, as well as player starting x, y, and width and height
	*/
	public myCanvas(int screenWidth, int screenHeight, int startX, int startY, int playerWidth, int playerHeight){
		this.setSize(screenWidth,screenHeight);
		this.setFocusable(true);
		this.setVisible(true);
		this.addKeyListener(this);
		playerX = startX;
		playerY = startY;
		playerW = playerWidth;
		playerH = playerHeight;
		playerColor = Color.GREEN;
	}
	/**
	*Woah! We're adding modularity to our code, by making our own method!
	*This method takes in two parameters, moveX and move Y, and moves the player accordingly from those values!
	*/
	public void movePlayer(int moveX,int moveY){
	//includes collision detection!
		if (playerX + moveX <= 0){
			playerX = playerX;
		}
		else if (playerX + moveX >= 300){
			playerX = playerX;
		}
		else{
			playerX += moveX;
		}
		if (playerY + moveY <= 0){
			playerY = playerY;
		}
		else if (playerY + moveY >= 400){
			playerY = playerY;
		}
		else{
			playerY += moveY;
		}
	} 
	/**
	*Here, we override the canvas default "paint function", which paints stuff to the screen using graphics.
	*/
	@Override
	public void paint(Graphics g){
		g.setColor(playerColor);
		g.fillOval(playerX,playerY,playerW,playerH);
	}
	public void setPlayerPosition(int newX, int newY){
		playerX = newX;
		playerY = newY;
	}
	/**
	*This time, we're adding a setter; in order to change private variables, other users, not us, need to use this
	*/
	public void setPlayerColor(Color settingPlayerColor){
		playerColor = settingPlayerColor;
	}
	/**
	*This time, we're adding a setter; but to change the player's size
	*/
	public void setPlayerSize(int newWidth, int newHeight){
		playerW = newWidth;
		playerH = newHeight;
	}

	/**
	*Here, we're overriding the KeyListener event KeyPressed
	*We add some logic to allow our guy to move
	*/
	public void keyPressed(KeyEvent e){
		if (e.getKeyCode() == KeyEvent.VK_DOWN){//these if statements are checking what keys are being pressed, and moving the player accordingly
			movePlayer(0,10);
		}
		else if (e.getKeyCode() == KeyEvent.VK_UP){
			movePlayer(0,-10);
		}
		else if (e.getKeyCode() == KeyEvent.VK_LEFT){
			movePlayer(-10,0);
		}
		else if (e.getKeyCode() == KeyEvent.VK_RIGHT){
			movePlayer(10,0);
		}
		else if (e.getKeyCode() == 77){//easter egg! Pressing 77, or "M", resets the ball back to its starting position. probably because m is the best letter :P
			setPlayerPosition(10,10);
		}

		setPlayerColor(Color.RED);//running our getters and setters!
		setPlayerSize(40,40);
		repaint();//repainting so we can see our changes
	}
	/**
	*Here, we're overriding the KeyListener event KeyReleased
	*We add some logic to allow our guy to change colours
	*/

	public void keyReleased(KeyEvent e){
		setPlayerColor(Color.GREEN);
		setPlayerSize(30,30);
		repaint();
		
	}
	/**
	*Here, we're overriding the KeyListener event KeyTyped
	*/

	public void keyTyped(KeyEvent e){

	}

}
