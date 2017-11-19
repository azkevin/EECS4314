import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Scanner;

public class MutualDependnecy {

	public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException 
	{
		HashSet<String> deps = new HashSet<String>();
		HashSet<String> common = new HashSet<String>();
		
		String file1 = args[0];
		String file2 = args[1];
		String output_file = args[2];
		
		PrintWriter writer = new PrintWriter(output_file, "UTF-8");
		Scanner file1_scanner = new Scanner(new File(file1));
		
		while(file1_scanner.hasNextLine())
		{
			String line = file1_scanner.nextLine();
			if(!line.isEmpty())
				deps.add(line);
		}
		
		file1_scanner.close();
		
		Scanner file2_scanner = new Scanner(new File(file2));
		
		while(file2_scanner.hasNext())
		{
			String line = file2_scanner.nextLine();
			if(!line.isEmpty())
			{
				if(deps.contains(line))
					common.add(line);
			}
		}
		file2_scanner.close();
		
		Iterator<String> it = common.iterator();
		while(it.hasNext())
		{
			writer.println(it.next());
		}
		
		writer.close();
		

	}

}
