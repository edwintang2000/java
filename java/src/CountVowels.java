import java.util.Scanner;
public class CountVowels {

	public CountVowels() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("Please input a sentence:");
		String str = in.nextLine();
		str = str.toLowerCase();	
		in.close();
		int vowels = 0;
		int consonants=0;
		for (int i = 0 ; i < str.length(); i++) {
			if ((str.charAt(i) == 'a') || (str.charAt(i) == 'e') || (str.charAt(i) == 'i') || (str.charAt(i) == 'o') || (str.charAt(i) == 'u') || (str.charAt(i) == 'y')) {
				vowels++;
			}
			else if (str.charAt(i) != ' ') {
				consonants++;
			}
		}
		System.out.println("There are " + vowels + " vowels");
		System.out.println("There are " + consonants + " consonants");
	}
}
