"""Java test runner module for LeetCode solutions"""
import json
import os
import subprocess
import tempfile


def compile_solution(folder):
    """Compile the Java solution file"""
    java_file = os.path.join(folder, "Solution.java")
    
    if not os.path.exists(java_file):
        print("❌ Solution.java not found")
        return False
    
    try:
        result = subprocess.run(
            ["javac", os.path.abspath(java_file)],
            capture_output=True,
            text=True,
            cwd=folder
        )
        if result.returncode != 0:
            print(f"❌ Java compilation failed:")
            print(result.stderr)
            return False
        return True
    except FileNotFoundError:
        print("❌ javac not found. Please install Java JDK.")
        return False


def run_test(folder, input_data):
    """Run Java solution with given input data"""
    # Get all parameters
    params = []
    for param_name, param_value in input_data.items():
        param_type, value_str = get_param_type_and_value(param_value)
        params.append((param_name, param_type, value_str))
    
    # Detect the method name and class name from Java file
    method_name, class_name = detect_method_name(folder)
    if not method_name:
        print("   Could not detect method name in Java class")
        return None
    
    # Generate test runner code
    runner_code = generate_runner_code(params, method_name, class_name)
    
    # Write runner to file
    runner_path = os.path.join(folder, "TestRunner.java")
    with open(runner_path, 'w') as f:
        f.write(runner_code)
    
    try:
        # Compile TestRunner along with Solution
        solution_java = os.path.join(folder, "Solution.java")
        compile_result = subprocess.run(
            ["javac", os.path.abspath(runner_path), os.path.abspath(solution_java)],
            capture_output=True,
            text=True,
            cwd=folder
        )
        
        if compile_result.returncode != 0:
            print(f"   TestRunner compilation error: {compile_result.stderr}")
            return None
        
        # Run Java
        result = subprocess.run(
            ["java", "TestRunner"],
            capture_output=True,
            text=True,
            cwd=folder,
            timeout=5
        )
        
        if result.returncode != 0:
            print(f"   Java execution error: {result.stderr}")
            return None
        
        # Parse output - handle multi-line output
        output = result.stdout.strip()
        if not output:
            return None
            
        # Get only the last line (in case there are debug prints)
        lines = output.split('\n')
        last_line = lines[-1].strip()
        
        try:
            return eval(last_line)
        except:
            print(f"   Could not parse output: {last_line}")
            return None
            
    except subprocess.TimeoutExpired:
        print("   Java execution timed out")
        return None
    except Exception as e:
        print(f"   Error running Java: {e}")
        return None
    finally:
        # Clean up temp files
        cleanup_files(folder)


def get_param_type_and_value(param_value):
    """Determine Java type and value string from Python value"""
    if isinstance(param_value, bool):
        return "boolean", "true" if param_value else "false"
    elif isinstance(param_value, int):
        return "int", str(param_value)
    elif isinstance(param_value, float):
        return "double", str(param_value)
    elif isinstance(param_value, str):
        return "String", f'"{param_value}"'
    elif isinstance(param_value, list):
        if not param_value:
            return "int[]", "{}"
        elif all(isinstance(x, int) for x in param_value):
            return "int[]", "{" + ", ".join(map(str, param_value)) + "}"
        elif all(isinstance(x, str) for x in param_value):
            return "String[]", "{" + ", ".join(f'"{x}"' for x in param_value) + "}"
        elif all(isinstance(x, float) for x in param_value):
            return "double[]", "{" + ", ".join(map(str, param_value)) + "}"
    return "Object", str(param_value)


def detect_method_name(folder):
    """Detect the public method name and class name in the Java file"""
    java_file = os.path.join(folder, "Solution.java")
    try:
        with open(java_file, 'r') as f:
            content = f.read()
        
        # Find class name
        import re
        class_pattern = r'(?:public\s+)?class\s+(\w+)'
        class_match = re.search(class_pattern, content)
        class_name = class_match.group(1) if class_match else "Solution"
        
        # Find public methods (not constructor)
        # Updated pattern to handle array return types like int[], String[], etc.
        method_pattern = r'public\s+[\w\[\]]+\s+(\w+)\s*\('
        matches = re.findall(method_pattern, content)
        
        # Filter out constructor (same name as class)
        methods = [m for m in matches if m != class_name]
        
        if methods:
            return methods[0], class_name  # Return first public method and class name
        return None, class_name
    except Exception as e:
        print(f"   Error detecting method name: {e}")
        return None, "Solution"


def generate_runner_code(params, method_name, class_name):
    """Generate Java test runner code"""
    # Generate variable declarations
    declarations = "\n        ".join([f"{param_type} {param_name} = {value_str};" for param_name, param_type, value_str in params])
    
    # Generate method call arguments
    method_args = ", ".join([param_name for param_name, _, _ in params])
    
    return f"""public class TestRunner {{
    public static void main(String[] args) {{
        {class_name} solution = new {class_name}();
        {declarations}
        Object result = solution.{method_name}({method_args});
        
        if (result == null) {{
            System.out.println("None");
        }} else if (result instanceof Boolean) {{
            System.out.println((Boolean)result ? "True" : "False");
        }} else if (result instanceof Integer) {{
            System.out.println(result);
        }} else if (result instanceof Long) {{
            System.out.println(result);
        }} else if (result instanceof Double) {{
            System.out.println(result);
        }} else if (result instanceof String) {{
            System.out.println("'" + result + "'");
        }} else if (result instanceof int[]) {{
            System.out.print("[");
            int[] arr = (int[])result;
            for (int i = 0; i < arr.length; i++) {{
                if (i > 0) System.out.print(", ");
                System.out.print(arr[i]);
            }}
            System.out.println("]");
        }} else if (result instanceof String[]) {{
            System.out.print("[");
            String[] arr = (String[])result;
            for (int i = 0; i < arr.length; i++) {{
                if (i > 0) System.out.print(", ");
                System.out.print("'" + arr[i] + "'");
            }}
            System.out.println("]");
        }} else if (result instanceof double[]) {{
            System.out.print("[");
            double[] arr = (double[])result;
            for (int i = 0; i < arr.length; i++) {{
                if (i > 0) System.out.print(", ");
                System.out.print(arr[i]);
            }}
            System.out.println("]");
        }} else {{
            System.out.println(result);
        }}
    }}
}}
"""


def cleanup_files(folder):
    """Clean up generated test files"""
    files_to_remove = [
        "TestRunner.java",
        "TestRunner.class",
        "Solution.class"
    ]
    
    for filename in files_to_remove:
        filepath = os.path.join(folder, filename)
        if os.path.exists(filepath):
            try:
                os.unlink(filepath)
            except Exception:
                pass  # Ignore cleanup errors
