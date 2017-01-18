public class HiddenWord{
  private String name = "";
  public HiddenWord(){
    name = "test";
  }
  public HiddenWord(String hiddenWord){
    name = hiddenWord;
  }
  public String getHiddenWord(){
    return name;
  }
  public String getHint(String hint){
    String response = "";
    if (name.length() != hint.length()){
      return "Invalid Input";
    }
    else{
      for (int i = 0; i < hint.length(); i++){
        if (String.valueOf(hint.charAt(i)).equals(String.valueOf(name.charAt(i)))){
          response = response.concat(String.valueOf(hint.charAt(i)));
        }
        else{
          int set = 0;
          outerloop:
          for (int j = 0; j < hint.length(); j++){
            if (String.valueOf(hint.charAt(i)).equals(String.valueOf(name.charAt(j)))){
              response = response.concat("+");
              set = 1;
              break outerloop;
            }
          }
          if (set == 0){
            response = response.concat("*");
          }
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
