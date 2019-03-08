import com.ceacar.ClockAngel;
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
	  String[] array0 = {1, 1, 0, 0, 0};
	  String[] array1 = {0, 1, 0, 0, 1}; 
	  String[] array2 = {1, 0, 0, 1, 1};
	  String[] array3 = {0, 0, 0, 0, 0}; 
	  String[] array4 = {1, 0, 1, 0, 1};
	  string[][] input_matrix = {array0, array1, array2, array3, array4};



	}

}
