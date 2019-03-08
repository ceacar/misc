package com.ceacar;
import java.lang.*;

public class ClockAngel{
  public ClockAngel(){
    System.out.println("wtf"); 
  }
  public int getAngel(int hour, int minute){
    int hour_angle = hour * 30;
    int minute_angel = minute * 6;

    return Math.abs(hour_angle - minute_angel);
  }

}
