fn main() {

	let suffix_notation = 42i8; 

	println!("Hello World!");
	println!("{} in decimal, {:b} in binary", suffix_notation, 42);
	println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");
	println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");

	let pi = 3.141592; 
	println!("{:.2}", pi);

/*	#[allow(dead_code)]
	struct Structure(i32); 
	println!("{}", Structure);*/


}