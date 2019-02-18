public class Stack{
	private int maxSize;
	private int[] intArray;
	private int index = 0;
	public Stack(int maxSize){
		maxSize = maxSize;
		intArray = new int[maxSize];
	}	

	public void push(int newElement){
		intArray[index] = newElement;
		index ++;
	}
	
	public int pop(){
		try{
			return intArray[--index];
		}
		catch(IndexOutOfBoundsException e){
			System.out.println("index is out of bond");
			return -99999999;
		}
	}

	public boolean isEmpty(){
		if (index == 0 ){
			return true;
		}
		return false;
	}

}
