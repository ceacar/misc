package com.ceacar;
import java.util.Arrays;
import java.util.ArrayList;
import java.awt.Point;
public class FlatFiller{
  /*
   *
   * Input : mat[][] = 
   * {{1, 1, 0, 0, 0},
   *  {0, 1, 0, 0, 1}, 
   *  {1, 0, 0, 1, 1},
   *  {0, 0, 0, 0, 0}, 
   *  {1, 0, 1, 0, 1}}
   */
	private int length_x;
	private int length_y;
	private ArrayList<ArrayList<Integer>> matrix_seen;

	public FlatFiller(){

	}

	public void init_parameters(int[][]matrix_input){
		this.length_x = matrix_input[0].length;
		this.length_y = matrix_input.length;
		this.matrix_seen = new ArrayList<ArrayList<Integer>>();

		for (int y = 0; y < this.length_y; y++){
			ArrayList<Integer> arryTemp = new ArrayList<Integer>();
			for (int x = 0; x < this.length_x; x++){
				arryTemp.add(0);
			}
			matrix_seen.add(arryTemp);
		}
		System.out.printf("matrix ready: %s\n", matrix_seen);
		this.matrix_seen = matrix_seen;
	}

	public int countIsland(int[][] matrix_input) throws Exception{
		if (matrix_input.length < 1){
			Exception exp = new Exception("matrix_input too short");
			throw exp;
		}
		this.init_parameters(matrix_input);
		int counter = 0;
		for (int y = 0; y < this.length_y; y++){
			for (int x = 0; x < this.length_x; x++){
				System.out.println(String.format("matrix_input x:%s y:%s is %d", x, y, matrix_input[y][x]));
				if (matrix_input[y][x] == 1){
				  counter++;
				  this.traverseIsland(matrix_input, x, y, this.matrix_seen);
				}
			}
		}
		return counter;
	}

	public ArrayList<Point> getNeighbors(int[][] matrix_input, int x, int y){
		ArrayList<Point> neighbor = new ArrayList<Point>();
		if (x - 1 > 0){
			neighbor.add(new Point(x - 1, y));
		}
		if (x + 1 <= this.length_x){
			neighbor.add(new Point(x + 1, y));
		}
		if (y - 1 > 0){
			neighbor.add(new Point(x, y - 1));
		}
		if (y + 1 <= this.length_y){
			neighbor.add(new Point(x, y + 1));
		}

		return neighbor;
	}

	public int arrayListHelper(ArrayList<ArrayList<Integer>> arrArrList, int x, int y){
		ArrayList<Integer> subArrayList = arrArrList.get(y); 	
		int res = subArrayList.get(x);
		return res;
	}

	public int setArrayListHelper(ArrayList<ArrayList<Integer>> arrArrList, int x, int y, int newValue){
		ArrayList<Integer> subArrayList = arrArrList.get(y); 	
		return subArrayList.set(x, newValue);
	}


	public void traverseIsland(int[][] matrix_input, int x, int y, ArrayList<ArrayList<Integer>> matrix_seen){
		ArrayList<Point> neighbors = this.getNeighbors(matrix_input, x, y);
		System.out.println("neighbors:");
		System.out.println(neighbors);

		for (Point pt: neighbors){
			if (this.arrayListHelper(matrix_seen, x, y) == 0) {
				if (matrix_input[pt.y][pt.x] == 1){
					System.out.println(">>");
					this.setArrayListHelper(matrix_seen, x, y, 1);
				}
			}
		}
	}


}
