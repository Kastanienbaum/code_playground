use std::io; 
use std::cmp::Ordering; 
use rand::Rng; 

/// This is some comment starting with three slashes 
//* This is some comment starting with //*

fn main() {
	println!("Guess the number!");

	let secret_number = rand::thread_rng().gen_range(1,11);
	println!("secret_number = {}", secret_number);

	loop {
		println!("Please input guess:");

		let mut guess = String::new(); 

		io::stdin().read_line(&mut guess)
				   .expect("Failed to read line"); 

		//let guess: u8 = guess.trim().parse().expect("Please type a number!");
		let guess: u8 = match guess.trim().parse() {
			Ok(num) => num, 
			Err(_)  => continue, 
		}; 
		
		println!("You guessed {}", guess); 

		match guess.cmp(&secret_number) {
			Ordering::Less    => println!("Too small"),
			Ordering::Greater => println!("Too big"),
			Ordering::Equal   => {
				println!("You win!");
				break; 
			}
		}	
	}
}

// EOF 