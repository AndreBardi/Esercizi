//La nostra implementazione di una Linked List
public class NostraLL<T> {
	private T data; //Il primo elemento della lista usa solo il puntatore
	private NostraLL<T> first;
	private NostraLL<T> next;
	
	public NostraLL() {
		first = null;
	}
	
	void AddFirst (T info) {
		NostraLL<T> l = new NostraLL<T>();
		l.data = info;
		l.next = null;
		
		if (first == null) {
			//la lista è vuota
			first = l;
		}else {
			l.next = first;
			first = l;
		}
	}

	
	void AddLast (T info) {
		NostraLL<T> l = new NostraLL<T>();
		l.data = info;
		l.next = null;
		
		if (first == null) {
			first = l;
		}else {
			while (next.next != null) {
				next = next.next;				
			}
		}
	}
}