public class HiddenWord{
  private String name = "";
  public HiddenWord(){
    name = "HARPS";
  }
  public HiddenWord(String hiddenWord){
    name = hiddenWord;
  }
  public String getHint(String hint){
    if (name.length() != hint.length()){
      return "Invalid Input";
    }
    else{
      String response = "";
      for (int i = 0; i < hint.length(); i++){
        if(hint.substring(i,i+1).equals(name.substring(i, i+1))){
          response += hint.substring(i,i+1);
        }
        else if (name.indexOf(hint.substring(i,i+1)) >= 0){
          response += "+";
        }
        else{
          response += "*";
        }
      }
      return response;
    }
  }
  public static void main(String[] args){
    HiddenWord puzzle = new HiddenWord("HARPS");
    String answer = puzzle.getHint("HELLO");
    System.out.println(answer);
  }
}
