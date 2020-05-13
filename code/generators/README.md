One of the things I wanted to do was build a tool for cleaning the Project Gutenberg corpora I was using. There is an extant library called, appropriately, (gutenberg)[https://github.com/c-w/Gutenberg], that handles the header and footer boilerplate quite well. And from whom I borrow quite liberally in this particular project.

At the same time, I was writing an article about generators for DataQuest. Most of the tutorials out there on generators focus on Project Euler-type problems like Fibonacci. And that's all well and good when you just want to see a generator in action. But I wanted to be able to demonstrate their use. Since generators go, in this case, line by line until there are no more lines, which is how I originally cleaned up these texts, I thought they would be the right tool for this job.

The object is to automatically write to a file any line that does not need human evaluation, bring to attention those that do. But it is to do so line by line. In pseudocode:
```for line in text:
      if line is clean:
        write line to file
      elif line is not clean:
        
