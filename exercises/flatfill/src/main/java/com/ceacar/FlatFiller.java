import java.util.Arrays
public class FlatFiller(){
  /*
   *
   * Input : mat[][] = 
   * {{1, 1, 0, 0, 0},
   *  {0, 1, 0, 0, 1}, 
   *  {1, 0, 0, 1, 1},
   *  {0, 0, 0, 0, 0}, 
   *  {1, 0, 1, 0, 1}}
   */

  public FlatFiller(){
  
  }

  public int countIsland(int[][] matrix_input) throws Exception{
    if (matrix_input.length < 1){
      throw Exception;
    }
    int counter = 0;
    int length_x = matrix_input[0].length;
    int length_y = matrix_input.length;

    ArrayList<Integer[]> matrix_seen = new ArrayList<Integer[]>();
    for (int y = 0; y < length_y; y++){
      ArrayList<Integer> arryTemp = ArrayList<Integer>();
      for (int x = 0; x < length_x; x++){
	arryTemp.add(0)
      }
      matrix_seen.add(arryTemp)
    }
    System.out.printf("matrix ready: %s", matrix_seen);



    for (int y = 0; y < length_y; y++){
      for (int x = 0; x < length_x; x++){
	if (matrix_input[y][x] == 1){
	  System.out.println(String.format("matrix_input %s %s is %d", x, y, matrix_input[y][x]));
	  counter++;
	}
      
      }
    }
  }
  
  public void traverseIsland(string[][] matrix_input, string[][] matrix_seen){
  
  }


}
