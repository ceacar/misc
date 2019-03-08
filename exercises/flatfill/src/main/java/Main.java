import com.ceacar.ClockAngel;
import com.ceacar.FlatFiller;
//package com.ceacar;
public class Main { 
	public static void main(String [] args)
	{
	  int h = 12;
	  int m = 30;
	  ClockAngel ca = new ClockAngel();
	  int angle = ca.getAngel(h, m);
	  System.out.println(angle);

   
   
   


	  //test flat fill
	  int[] array0 = {1, 1, 0, 0, 0};
	  int[] array1 = {0, 1, 0, 0, 1}; 
	  int[] array2 = {1, 0, 0, 1, 1};
	  int[] array3 = {0, 0, 0, 0, 0}; 
	  int[] array4 = {1, 0, 1, 0, 1};
	  int[][] input_matrix = {array0, array1, array2, array3, array4};
	  try{
		  FlatFiller  islandCounter = new FlatFiller();
		  int total_island = islandCounter.countIsland(input_matrix);
		  System.out.println(String.format("total_island is %s",total_island));
	  } catch(Exception e){
		  System.out.println("oops");
	  }
	}

}
