# Table of Contents

- [Table of Contents](#table-of-contents)
- [Automatic Readme file generator](#automatic-readme-file-generator)
  - [Example usage](#example-usage)
    - [License](#license)
    - [Contributing](#contributing)
    - [Authors](#authors)

# Automatic Readme file generator 

It parses Verilog code and automatically adds comments, reducing the time spent on manual commenting by up to 70%. This feature not only improves code readability but also facilitates collaboration among team members.

By analyzing code comments, it generates a standardized README file for the entire project. This README is updated dynamically with each commit, ensuring that project documentation remains comprehensive and up-to-date.

## Example usage

```python
verilog_path = "../test/input.v"
output_path = "../test/output.v"

analyzer = VerilogAnalyzer(verilog_path)
analyzer.analyze()
analyzer.print_results()

# To get the component dictionary
component_dict = analyzer.get_component_dict()
pprint.pprint(component_dict)

# To add comments to the Verilog code and write it to a new file
code_lines = analyzer.read_verilog_code()
analyzer.hardware_component.update_comments_in_dict(code_lines)
analyzer.hardware_component.remove_duplicate_line_entries()
analyzer.hardware_component.update_size_in_comment()
comment_writer = VerilogCommentWriter(analyzer.hardware_component)
comment_writer.add_comments_to_code(code_lines, output_path)
```

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

### Authors

  Mahmoud Amiri