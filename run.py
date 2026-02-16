#!/usr/bin/python3
import glob
import importlib.util
import os
import re
import sys

import java_runner


def find_problem_folder(problem_number):
    matches = glob.glob(f"leetcode/*/{problem_number}_*/")
    if not matches:
        raise FileNotFoundError(f"No folder found for problem {problem_number}")
    return matches[0]


def load_solution_class(folder):
    path = os.path.join(folder, "main.py")
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()


def get_last_method(instance):
    # use last method
    # we can just "privatize" the other methods.
    return [fn for fn in dir(instance) if not fn.startswith("__")][-1]


def parse_leetcode_style_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    input_data = {}
    expected_output = None

    for line in lines:
        line = line.strip()
        if line.startswith("Input:"):
            input_str = line.replace("Input:", "").strip()
            pairs = re.split(r", (?=\w+ *=)", input_str)
            for pair in pairs:
                name, val = pair.split("=", 1)
                input_data[name.strip()] = eval(val.strip())
        elif line.startswith("Output:"):
            expected_output = eval(line.replace("Output:", "").strip())

    return input_data, expected_output


def run_datastructures_tests(folder):
    import ast

    tests_folder = os.path.join(folder, "tests")
    input_files = sorted(glob.glob(os.path.join(tests_folder, "test*.txt")))
    if not input_files:
        print(f"⚠️ No test files found in {tests_folder}")
        return

    # Load the solution module
    path = os.path.join(folder, "main.py")
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    passed = 0
    total = 0

    for input_path in input_files:
        case_id = os.path.basename(input_path).replace("input", "").replace(".txt", "")

        with open(input_path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        # Expecting:
        # Input
        # [operations]
        # [parameters]
        # Output
        # [expected_output]
        try:
            op_idx = lines.index("Input")
            out_idx = lines.index("Output")

            def fix_json_literals(s):
                return (
                    s.replace("true", "True")
                    .replace("false", "False")
                    .replace("null", "None")
                )

            operations = ast.literal_eval(fix_json_literals(lines[op_idx + 1]))
            parameters = ast.literal_eval(fix_json_literals(lines[op_idx + 2]))
            expected_output = ast.literal_eval(fix_json_literals(lines[out_idx + 1]))
        except Exception as e:
            print(f"❌ Test {case_id} failed to parse: {e}")
            continue

        # Get the class by name from the module
        class_name = operations[0]
        cls = getattr(module, class_name)
        obj = cls(*parameters[0])
        results = [None]  # Constructor always returns None/null

        for op, args in zip(operations[1:], parameters[1:]):
            method = getattr(obj, op)
            res = method(*args)
            # If the method returns None, append None (to match null in expected output)
            results.append(res if res is not None else None)

        total += 1
        if results == expected_output:
            print(f"✅ Test {case_id} passed")
            passed += 1
        else:
            print(f"❌ Test {case_id} failed")
            print(f"   Operations: {operations}")
            print(f"   Parameters: {parameters}")
            print(f"   Expected  : {expected_output}")
            print(f"   Got       : {results}")

    print(f"\n🧪 Summary: {passed}/{total} tests passed.")

    # Generate LeetCode URL
    folder_name = os.path.basename(os.path.normpath(folder))
    _, slug = folder_name.split("_", 1)
    leetcode_url = f"https://leetcode.com/problems/{slug}/description/"

    print(f"🔗 LeetCode Link: {leetcode_url}\n")


def run_all_tests(problem_number, language="python"):
    folder = find_problem_folder(problem_number)
    
    # Validate language choice
    if language not in ["python", "java"]:
        print(f"❌ Unsupported language: {language}")
        print("   Supported languages: python, java")
        return
    
    # Check if the language file exists
    lang_file = "main.py" if language == "python" else "Solution.java"
    if not os.path.exists(os.path.join(folder, lang_file)):
        print(f"❌ {lang_file} not found in {folder}")
        return
    
    # Special case for datastructures
    if os.path.normpath(folder).startswith(os.path.normpath("leetcode/datastructures")):
        if language == "java":
            print("❌ Java support for datastructures not yet implemented")
            return
        run_datastructures_tests(folder)
        return

    tests_folder = os.path.join(folder, "tests")
    
    if language == "python":
        solution = load_solution_class(folder)
        method_name = get_last_method(solution)
        method = getattr(solution, method_name)
    else:  # java
        # Compile Java file
        if not java_runner.compile_solution(folder):
            return

    input_files = sorted(glob.glob(os.path.join(tests_folder, "test*.txt")))
    if not input_files:
        print(f"⚠️ No test files found in {tests_folder}")
        return

    passed = 0
    total = 0

    for input_path in input_files:
        case_id = os.path.basename(input_path).replace("input", "").replace(".txt", "")
        input_data, expected_output = parse_leetcode_style_file(input_path)

        if language == "python":
            # deep copy inputs to preserve original data
            test_args = {
                k: v.copy() if isinstance(v, list) else v for k, v in input_data.items()
            }
            result = method(**test_args)
        else:  # java
            result = java_runner.run_test(folder, input_data)
            if result is None:
                print(f"❌ Test {case_id} failed to execute")
                total += 1
                continue
        
        total += 1
        if result == expected_output:
            print(f"✅ Test {case_id} passed")
            passed += 1
        else:
            print(f"❌ Test {case_id} failed")
            print(f"   Input   : {input_data}")
            print(f"   Expected: {expected_output}")
            print(f"   Got     : {result}")

    print(f"\n🧪 Summary: {passed}/{total} tests passed.")

    # Generate LeetCode URL
    folder_name = os.path.basename(os.path.normpath(folder))
    _, slug = folder_name.split("_", 1)
    leetcode_url = f"https://leetcode.com/problems/{slug}/description/"

    print(f"🔗 LeetCode Link: {leetcode_url}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <problem_number> [language]")
        print("  language: python (default) or java")
    else:
        problem_number = sys.argv[1]
        language = sys.argv[2] if len(sys.argv) > 2 else "python"
        run_all_tests(problem_number, language)
