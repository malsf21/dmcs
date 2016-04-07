/*
Mr. Hoel's Game.java
Creates a window!
Downloaded October 14

*/


//imports
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import javax.swing.JFrame;
import javax.swing.JPanel;

@SuppressWarnings("serial")
//class branch, class extends JPanel 
public class Game extends JPanel {
  //public integers x and y utilised throught the entire
  int x = 0;
  int y = 0;
  //private class that adds one to x and y
  private void movement() { 
    x = x + 1;
    y = y + 1;
  }
  @Override
  //paint function, takes input graphics g
  public void paint(Graphics g) {
    super.paint(g);
    Graphics2D g2d = (Graphics2D) g;
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
    RenderingHints.VALUE_ANTIALIAS_ON);
    //does the actual drawing
    g2d.fillOval(x, y, 30, 30);
  }
  //main function, auto-runs on program startup
  public static void main(String[] args) throws InterruptedException {
    //creates new JFrame
    JFrame frame = new JFrame("Sample Frame");
    Game game = new Game();
    frame.add(game);
    frame.setSize(300, 400);
    //Important, setVisible makes the frame visible!
    frame.setVisible(true);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    //while loop that repaints the frame every 10 seconds
    while (true) {
      game.movement();
      game.repaint();
      Thread.sleep(10);
    }
  }
}