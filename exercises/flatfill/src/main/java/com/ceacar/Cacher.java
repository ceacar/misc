package com.ceacar;
import java.util.HashMap;

public class Cacher{

  private HashMap<String, String> internalCache;

  public Cacher(){
    this.internalCache = new HashMap<String, String>();
  }

  public String get(String key){
    return this.internalCache.get(key);
  }

  public void set(String key, String value){
    System.out.println("before");
    this.internalCache.put(key, value);
    System.out.println(this.internalCache);
  }
}
