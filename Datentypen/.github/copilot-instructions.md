# Copilot Instructions for SE_Python/Datentypen

## Project Overview
This is a German-language Python learning project focused on data types (`Datentypen`). The codebase contains educational examples demonstrating Python fundamentals including variable types, string formatting, and ASCII character manipulation.

## Code Patterns & Conventions

### Language & Comments
- **German comments and documentation**: All comments and explanatory text are in German
- Use German variable names and comments when extending the codebase
- Example: `erstelle ein kleine python programm` (create a small Python program)

### String Formatting Techniques
The project demonstrates multiple Python string formatting approaches:
- **Legacy concatenation**: `'text ' + str(variable) + ' more text'`
- **f-strings (preferred)**: `f'text {variable} more text'`  
- **Mixed print statements**: `print('text', variable, 'more text')`

### ASCII Table Generation Pattern
Key pattern in `main.py` for educational ASCII tables:
```python
for i in range(start, end):
    print(f"{i:3} {i:02X} {chr(i)} | ...")  # Decimal, Hex, Character format
```
- Uses `:3` for right-aligned 3-digit decimal formatting
- Uses `:02X` for uppercase hexadecimal with zero-padding
- Creates columnar output with `|` separators

### Educational Code Structure
- Simple, linear progression from basic concepts to more complex
- Extensive inline comments explaining ASCII ranges (65-90 A-Z, 97-122 a-z, etc.)
- Demonstrates character encoding knowledge with specific Unicode points

## Development Workflow
- **Single file execution**: Run `python main.py` directly
- **No external dependencies**: Pure Python standard library only
- **Educational focus**: Code prioritizes clarity and demonstration over efficiency

## Key Files
- `main.py`: Main educational script demonstrating data types and ASCII tables

## AI Assistant Guidelines
- Maintain German comments and educational tone
- When adding ASCII examples, follow the established columnar format
- Preserve the learning progression from simple variables to formatted output
- Keep code simple and educational rather than production-optimized