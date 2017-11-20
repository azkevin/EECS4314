import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Scanner;

public class InitialMutualDependnecy {

	public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException 
	{
		String file1 = args[0];
		String file2 = args[1];
		String output_file = args[2];

		Scanner file1_scanner = new Scanner(new File(file1));
		PrintWriter writer = new PrintWriter(output_file, "UTF-8");

		while(file1_scanner.hasNextLine())
		{
			String line_f1 = file1_scanner.nextLine();
			if(!line_f1.isEmpty())
			{
				Scanner file2_scanner = new Scanner(new File(file2));
				boolean found = false;
				while(file2_scanner.hasNextLine() && !found)
				{
					String line_f2 = file2_scanner.nextLine();
					if(line_f1.equals(line_f2))
					{
						writer.println(line_f1);
						found = true;
					}
				}
				file2_scanner.close();
			}
		}

	}

}
